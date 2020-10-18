# Database Preparation

Before work could be done with the dashboard application, it is assumed that for this instance there is no database that would hold information that could be retrieved, displayed and analyzed. Therefore, the process of preparing a database is automated.

Several things to note in order to prepare a working database:

1. Automated creation happens using `python3` in order to be consistent with how this project is structured in the first place.
2. The database will be constructed on top of `SQLite` in the given instance in order to maintain a light database for example purposes. As well, because `python3` comes with a pre-exiting module for it.
3. The database is populated based on the information from the excel files, that should be present in the `application/excel_files/` path.
