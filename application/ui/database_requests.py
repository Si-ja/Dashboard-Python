class DatabaseRequests:
    """
    A class that helps handle the most essential requests to the database in order
    to allow for the Dash application to work.
    """

    def __init__(self):
        import sqlite3
        from sqlalchemy import create_engine

        self.base_dir = self.read_location()
        self.db_name = "prices.db"
        self.db_path = self.base_dir + "/database/" + self.db_name

        # Some requests are easier to perform with the simple queries and other
        # With the SQLAlchemy assisting module

        # Make the connection for SQLite3 handler &
        # Make the connection for the SQLAlchemy handler
        self.engine_connection = "sqlite:///" + self.db_path
        self.conn = None
        self.c = None
        self.engine = None
        self.open_connection()

        # When loading the class, verify what tables can we work with
        self.existing_tables = self.available_tables()

        # As well, verify what sort of columns each table has except for the Time one
        self.existing_columns = self.available_columns()

        # Close the connection to the database
        self.close_connect()


    def open_connection(self):
        """
        Open a connection to the database - manage it in a more secure way.
        """
        import sqlite3
        from sqlalchemy import create_engine
        try:
            self.conn = sqlite3.connect(self.db_path)
        except Exception as e:
            print(e)
        self.c = self.conn.cursor()
        self.engine = create_engine(self.engine_connection)

    def close_connect(self):
        """
        Close connection to the database - manage it in a more secure way.
        """
        self.conn.close()


    def read_location(self):
        """
        Find the path of the base directory
        """
        import json
        base_dir = None
        # This is the only absolute path that creates one of the biggest amount
        # of issues if the app.py is moved. Treat carefully. .json should be located
        # Where the app.py is located, from whitch all the executions take place
        with open("directory.json") as json_file:
            data = json.load(json_file)
            base_dir = data["Directory"]
        return base_dir

    def available_tables(self):
        """
        Check what tables in the database are available, when the class is initiated.

        Return:
            List of tables in the SQLite database.
        """
        self.open_connection()
        results = self.conn.execute(f"SELECT name FROM sqlite_master WHERE type='table';")
        tables_collection = []
        for name in results:
            tables_collection.append(name[0])
        self.close_connect()
        return tables_collection

    def available_columns(self):
        """
        Check what sort of column all of our existing tables have.

        Return:
            dict of tables: [columns] identifiers
        """
        self.open_connection()
        answer = {}
        for table_name in self.existing_tables:
            results = self.conn.execute(f"SELECT * FROM {table_name} LIMIT 0")
            names = [description[0] for description in results.description]
            answer[table_name] = names
        self.close_connect()
        return answer

    def get_FormatedExistingTables(self):
        """
        A method that formats the information about the tables, in order to keep
        a consiten pattern with the Dash framework.
        """
        formated = []
        for table in self.existing_tables:
            temp_dict = {"label": table[-4:], "value": table}
            formated.append(temp_dict)
        return formated

    def get_FormatedExistingColumns(self, table_name):
        """
        Format the columns in a way that would be acceptable for the dash framework.

        Input:
            table_name (str) - pass a table name to the method to know from where to retrieve
            the column names
        """
        column_names = self.existing_columns[table_name][1:]
        collection = []
        for entry in column_names:
            temp_dict = {"label": entry, "value": entry}
            collection.append(temp_dict)
        return collection

    def get_Dataframe(self, table_name):
        import pandas as pd
        self.open_connection()
        df = pd.read_sql_query(sql=f"SELECT * FROM {table_name}", con=self.conn)
        self.close_connect()
        return df

    def get_ExistingColumns(self):
        return self.existing_columns

    def get_ExistingTables(self):
        return self.existing_tables