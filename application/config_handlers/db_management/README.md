# Database Preparation

Before work could be done with the dashboard application, it is assumed that for this instance there is no database that would hold information that could be retrieved, displayed and analyzed. Therefore, the process of preparing a database is automated.

Several things to note in order to prepare a working database:

1. Automated creation happens using `python3` in order to be consistent with how this project is structured in the first place.
2. The database will be constructed on top of `SQLite` in the given instance in order to maintain a light database for example purposes. As well, because `python3` comes with a pre-exiting module for it.
3. The databases are populated based on the information from the excel files, that should be present in the `application/excel_files/` path. To use the same files, as have been used to develop the project and for its' specific use case, please refer to the README.md file in the `application/database/` path.

## How to populate the database

Please follow the following instructions, to get the database created and populated with information.

1. Make sure you have a folder named `excel_files` in your `application` base directory.
2. The folder `excel_files` should contain only the excel files. The source where they can be retrieved from and in what format saved is indicated in the README.md file located in the database folder. 
3. Make sure that you have isntalled modules, or an environment set up with installed modules, indicated in the requirements.txt file. You can install them by running:

```shell
# Depending on the version of python 2 or 3
pip install -r requirements.txt
pip3 install -r requirements.txt
```
