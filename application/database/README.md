# Database

The databas is recommended to be generated with the `database_init.py` file (and is indicated in the Set Up instructions in the main README.md file of this project), located in the root of the `Dashboard-Python/application/` directory. It will read information from the excel files, placed in the `Dashboard-Python/application/excel_files/` directory, clean them, and upload into an SQLite database that will be located here (the current file is empty, but has all the needed permissions set up, so that the python through connection to it, could modify it).

Do note, that excel_files for which the cleaning methodology is tailored are specific and cannot be easily interswapped for any kind of data. Please read the README.md file in the root of this project to learn more.

# Data

Data for this project has been retrieved from a publically available resource: [@Nord Pool](https://www.nordpoolgroup.com/historical-market-data/). To get the same data, please follow the following steps:

Search under criteria:
    - Elspot Prices (in the dropdown for Filter by category)
    - Hourly        (in the dropdown for filter by resolution)
        - Originally files retrieved were used with an indication `_EUR` at the end of their names.
        - Original files had an extension .xlsx, but sadly do not work with just the default .xls, that can be retrieved currently from the said source This is known and being worked on.

Retrieve files for the years that interest you. Store them in the `Dashboard-Python/application/excel_files/` path. These files are providing information on electrical prices Day-Ahead for the region of Europe and it is the data that has been used to generate the dashboard, visual examples of which are presented in the root path of this project.
