class DatabasePopulation():
    """
    Class meant to help in populating sqlite database with information
    """

    def __init__(self):
        import sqlite3
        import os
        self.db_name = "prices.db"

        # Name under which the Time column will be noted
        self.df_timeName = "Time_record"

        # Set up a reusable connection to the database
        self.location = str(os.getcwd()) + "/database/" + self.db_name
        try:
            self.conn = sqlite3.connect(self.location)
        except Exception as e:
            print(e)
        self.c = self.conn.cursor()


    def delete_database(self):
        """
        If you run the self.handler method to handle all of the database creation steps
        Do note that this method will be called as well, in order to delete the old database
        will all the stored information in it. This Class is meant for population of data
        from complete scratch, and is not for appending of new information.

        The new file will also be created, in a read and write mode.

        Input:
            None

        Return:
            None
        """
        import os

        # Delete the database
        os.remove(self.location)
        print(f"The old database in the location {self.location} has been deleted")

        # Create a new database holding file
        # In some attempts, noticed that an error occurs, if sql query is left to
        # decide whether a .db file needs to be created or not, also creating it in
        # a read-only mode and crashing the whole system all together.
        with open(self.location, "w+") as new_db:
            pass
        print(f"A new database in the location {self.location} has been created")


    def files_walk(self):
        """
        Walk through the directory where the excel_files are stored and find all of them.
        Make sure the excel files are closed.

        Return:
            filenames (list<str>) - names of files from which the information will populate the databases
            clean_filenames (list<str>) - names of files cleaned, that can be re-used for creating and naming new tables
        """
        import os
        filenames=[]
        clean_filenames=[]

        # Walk through the directory and get all the file names
        path = str(os.getcwd()) + "/excel_files/"
        for _, _, filename in os.walk(path):
            filenames = filename

        # Clean the names of the files, to reuse them as names of future tables
        clean_filenames = [name[:name.find("_hourly")].replace("-", "_") for name in filenames]
        
        return filenames, clean_filenames


    def dataframe_cleaning(self, file_name):
        """
        A function that does the cleaning of information and allows for it to be subsequently
        pre-processed into the format in which the sqlite database will be formated.

        Input:
            file_name (str) - filename that needs to be pre-processed before its' information
            is loaded into the sqlite database.

        Return:
            A dataframe will be returned that holds all the cleaned data from the excel file,
            that now can populate the database.
        """
        import pandas as pd 
        import os

        file_path = str(os.getcwd()) + r"/excel_files/" + file_name

        # Read the file and skip first 2 rows, as they have no relevant information to us
        df = pd.read_excel(io=file_path, index_col=None, skiprows=2, engine="xlrd")

        # I'm already aware that there are some duplicate instances that exist for time variables
        # Removing duplicates seems to not work...can't figure out why
        # df["Unnamed: 0"] = df["Unnamed: 0"].astype("str")
        # df["Hours"] = df["Hours"].astype("str")
        # df.drop_duplicates(subset=["Unnamed: 0", "Hours"], keep="last", inplace=True)

        # Pre-process Days and Hours information and put it back into the original dataframe
        days = df["Unnamed: 0"]
        hours = df["Hours"].astype(str).str[:2]
        for i, value in enumerate(hours): hours[i] = " " + value + ":00:00"
        time = days + hours
        time.name = self.df_timeName
        df_time = pd.Series.to_frame(time)

        df = df.drop(["Unnamed: 0", "Hours"], axis=1)
        df.insert(0, self.df_timeName, df_time)

        # One more attempt at cleaning the duplicates
        df[self.df_timeName] = pd.to_datetime(df[self.df_timeName], dayfirst=True)
        # df = df.sort_values(self.df_timeName)
        df = df.drop_duplicates()

        # I have no clue why this works by this moment, but somehow, 
        # Only in this chain of events the dates actually properly delete if they are duplicates...
        # Please don't touch it
        df[self.df_timeName] = df[self.df_timeName].astype("str")
        df.drop_duplicates(subset=[self.df_timeName], keep="last", inplace=True)

        return df


    def create_table(self, table_name, dataframe):
        """
        A function that will create a table in the sqlite database. 

        Inputs:
            table_name (str) - name of the table that will have to be features.
            dataframe (pandas.DataFrame) - DataFrame with column names which will server as data
            to build a query to create said tables.

        Return:
            None
        """
        import pandas as pd
        import sqlite3
        import os
        # Now a query will be build based on the column names that are unique (and there is a different quanity of which)
        # For each individual table instance, except for the Time that is present in all.
        
        # Initializing the query with the base components
        sql_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({self.df_timeName} text PRIMARY KEY, "

        # Going through all the columns of a specific dataframe and adding info from them as REAL
        for column_name in dataframe.columns[1:]:
            column_name_replaces = column_name.replace(".", "_").replace("-", "_")
            sql_query += f"{column_name_replaces} REAL, "

        # Close of the query request when all of the columns have been added
        # Because we add a space and a comma in the end of each column name - they are also removed

        sql_query = sql_query[:len(sql_query) - 2] + ")"

        # Execute the query to build the table
        self.c.execute(sql_query)
        self.conn.commit()


    def populate_table(self, table_name, dataframe):
        """
        A method that will populate the database with the information from the dataframe.

        Inputs:
            table_name (str) - name of the table that will have to be features.
            dataframe (pandas.DataFrame) - DataFrame with column names which will server as data
            to build a query to create said tables.

        Return:
            None
        """
        import pandas as pd 
        from sqlalchemy import create_engine
        import sqlite3

        # Set the path showing the connection to the sqlite database
        engine_connection = "sqlite:///" + self.location

        # Replace column names as was done previously, otherwise, the INSERT VALUE call
        # Gets confussed (we did replace all . with _)
        new_columns = {}
        for column_name in dataframe.columns:
            new_columns[column_name] = column_name.replace(".", "_").replace("-", "_")

        dataframe = dataframe.rename(columns=new_columns)

        engine = create_engine(engine_connection)
        dataframe.to_sql(name=table_name, con=engine, if_exists="append", index=False, chunksize=200)

        print(f"The [{table_name}] table has been updated!")
        # REDACTED: LEFT IN CASE OF AN EMERGENCY
        # Because of the issues deleting duplicates this is a temporary solution
        # Due to lack of time:
        # for i in range(len(dataframe)):
        #     if (i%200==0): print(f"Updating record [{i}]")
        #     try:
        #         dataframe.iloc[i:i+1].to_sql(name=table_name, con=engine, if_exists="append", index=False)
        #     except:
        #         print(f"Record {i} couldn't be updated due to an Integrity Issue.")
        # # This will make the query beyond inneficient, but for a temporary measure this has to do


    def handler(self):
        """
        This method pretty much takes care of calling other methods and updating all
        of the tables at once, without the need for the user to interviene. It will
        also handle closing of the connection to the database.

        Inputs:
            None

        Return:
            None
        """
        import pandas as pd 
        import os
        import sqlite3
        import sqlalchemy

        # self.delete_database() # So far replaced with manual creation
        files, tables = self.files_walk()
        for i, _ in enumerate(files):
            output = self.dataframe_cleaning(files[i])
            self.create_table(tables[i], output)
            self.populate_table(tables[i], output)

        # The process has finished, so the connection can be closed
        self.conn.close()