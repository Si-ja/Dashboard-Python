# Dashboard for Electricity Prices

This is a small dashboard built with python and Dash, using SQLite as the database holder. Information on the database and files where they come from is inicated in the readme file in the application/database.

## What is this database about

It allows for an interactive visualization of information that is taken from 3 different excel files, placed into an SQLite database and queries are given to it for the dash to visualize.

Further you can see few examples of how the Dashboard currently looks.

The Default State of how the Dash Board initiates. It always loads the first table in the database, with their first column, no matter what it is. (Note: the column can also not exist, which should not pose an issue).

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/DefaultState.png "Default State")

You can change the tables selected, and the column values.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/AddingCountries.png "Add more variables")

You can also change the range - increase or decrease it, in respect to how many data points there are. So far the renge was tailored to fir the sequential nature of the data.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/ChangingRange.png "Change Range")


# How to run

If you decide to run on your own machine do the following:

1. Download the repository
2. Install all the required modules to python indicated in the application/requirements.txt
3. Run 
```python
python basedir_init.py
```
Which will prepare a .json file that will allow for the dashboard to navigate through the files in your repository
4. Run 
```shell
python database_init.py
```
This will take all of the files from the application/excel_files folder, pre-process them and populate a provided so far empty prices.db database. 

5. Navigate to the application/ui folder
6. Run 
```shell
python app.py
```
This will start the dashboard in your localhost environment.

## Currently known issues that are in plans to being fixed
- [ ] When a database is generated, it was supposed to be created and populated automatically. Unfortunatelly, when the file is created, it is made into a _read-only_ format. This makes it immpossible to fully populate in one go. Therefore, the file initially is provided empty. Currently looking for a solution, but initially the .db file is made empty, but in a "Read-And-Write format"

- [ ] Dockerization of the files so far was not fully implemented. The application does dockerize, through `docker-compose.yml` file, but when it is launched on the localhost:80, the user is greated with the __Internal Server Error__ message. Currently looking for what is causing the issue.

- [ ] Some of the app.callback functions that are present in the base app have slight shortcommings. For instance: when the dataframes from which the information is pulled change, the time frame in the RangeSlider on the bottom of the page does not reset. It doesn't pose a serious issue, but user-wise can be annoying.

- [ ] Make the Dashboard look more pretty

- [ ] Noticed that the range does not change depending on the table provided and takes the full range of the initial table that was loaded. In the given context it is not a big issue, as in all case the data ranges are planned to be years long. But can be problematic, as with the table representing year 2020, where after the dates of october there is no information and the Range gets a bit confussed on how the data needs to be presented then


## Important note about the data files

Originally the data files are not included in the project. But they are freely available online, and in the application/database/README.md file it is indicated where they can be downloaded. After downloading them - place them in the application/excel_files folder.