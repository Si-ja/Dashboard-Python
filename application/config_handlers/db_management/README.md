# Database Preparation

Before work could be done with the dashboard, it is assumed that for this instance there is no database that would hold information similar to the one we have in provided excel files. Therefore, files here help automate creating of the database for such case.

Several things to note:

1. Automated population happens using `python3` in order to be consistent with how this project is structured in the first place. Running of such files would have to be done manually, as it is not known beforehand, if all users who will take a look into this use Windows or Linux. Therefore batch and shell files are not developed, however could be helpful.
2. The database will be constructed on top of `SQLite` in order to maintain a light database for example purposes. As well, because `python3` comes with a pre-exiting module for it. However, afterwards if anything will be put into production - it could be swapped for a larger and more production-friendly one, such as `MySQL`, `MSSQL` or `PostgreSQL`, potentially utilizing the __SQLAlchemy__ module to `python`. Therefore, as all the basic queries will be made with `SQL` based command - swapping should not be of a too complicated nature.

## How to populate the database

Please follow the following instructions, to get the database created and populated with information.

1. Make sure you have a folder named `excel_files` in your application base directory.
2. The folder `excel_files` should contain the files provided already. Sources where they are retrieved are indicated in the README.md file located in the database folder.
3. Make sure that you have isntalled modules, or an environment set up with installed modules, indicated in the requirements.txt file. They are used through out the whole project, so only 1 set up would be required. You can also install all of them by running:
```shell
# Depending on the version of python 2 or 3
pip install -r requirements.txt
pip3 install -r requirements.txt
```
