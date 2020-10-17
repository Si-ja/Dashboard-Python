# Database

Navigate first to the following path: [How the database is prepared](https://github.com/Si-ja/Dashboard-Python/blob/main/application/config_handlers/db_management/README.md) and get familiarized with the documentation on it. It should give a more clear explanation to what the next steps that are done here mean.

The databas is recommended to be generated with the `database_init.py` file, located in the root of the `application` directory. It will read information from the excel files, placed in the `application/excel_files/` directory, clean them, and upload into an SQLite database that will be located here. 

Do note, that excel_files for which the cleaning methodology is tailored are specific and cannot be easily interswapped for any kind of data. Please read further to know where to get them and in what format to store.

# Data

Data for this project has been retrieved from a publically available resource: https://www.nordpoolgroup.com/historical-market-data/ To get the same data, please follow the following steps:

Search under criteria:
    - Elspot Prices (in the dropdown box for Filter by category)
    - Hourly        (in the dropdown box for filter by resolution)
        - Originally files retrieved were used with an indication `_EUR` at the end of their names.
        - Original files had an extension .xlsx, but sadly do not work with just the default .xls, if you download them as is. This is being worked on.

Retrieve files for the years that interest you. Store them in the aforementioned `application/excel_files/` path. These files are providing information on electrical prices Day-Ahead for the region of Europe.

# Database Set Up

After you download all the needed excel files and save them, to create the database run the following command in the root of the application directory:

```shell
python database_init.py
```
