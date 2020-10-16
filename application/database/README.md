# Database

The databas is recommended to be generated with the `database_init.py` file, located in the root of the application directory. It will read information from the excel files, placed in the application/excel_files directory, clean them, and upload into an sqlite database that will be located here. 

Do note, that excel_files as examples are already provided and the cleaning methodology is tailored to accomodate that particular format.

To create the database, run the following command in the root of the application directory with no extra parameters/arguments:

```python3
python database_init.py
```

# Data

Data has been retrieved from publically available databases: https://www.nordpoolgroup.com/historical-market-data/

Search under criteria:
    - Elspot Prices
    - Hourly
        - Originally files were used with an indication `_EUR` at the end of their names.

Representing Electrical prices Day-Ahead for the region of Europe.