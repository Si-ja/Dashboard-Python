# Dashboard for Electricity Prices

This is a small dashboard built with python and Dash, using SQLite as a database.

## What is this application about

It allows for an interactive visualization of information that represent electrical Day-Ahead prices in Europe per hour.

You can see few examples of how the Dashboard currently looks.

The Default State of how the Dash Board initiates. It always loads the first table in the database, with their second column, no matter what it is. (Note: the first column is reserved to represent the dates).

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/DefaultState.png "Default State")

You can change the tables selected, and the column values.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/AddingCountries.png "Add more variables")

You can also change the range - increase or decrease it, in respect to how many data points there are. So far the renge was tailored to fit the sequential nature of the data used in the project.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/ChangingRange.png "Change Range")

## How to run

### Option 1 - On your Local Machine

If you decide to run on your own machine do the following:

1. Get familiar with the documentation by going through the following README.md files: [How the database is prepared](https://github.com/Si-ja/Dashboard-Python/tree/main/application/config_handlers/db_management), [How to prepare the database before running the application](https://github.com/Si-ja/Dashboard-Python/tree/main/application/database)
2. Download the repository
3. Make all of the needed preparations, indicated in the step 1.
4. Navigate to the `application/` folder. All of the following prepareation will be done from here. Install all the required modules to python indicated in the `application/requirements.txt`, if needed in a new dedicated virtual environment.
5. To prepare a .json file that will allow for the dashboard to navigate through the folder on your computer it is in (as the database folder, excel files and other things are broken into components...and I didn't use relatives paths due to shortage of time, which I am aware would have been much better in the long run), run 
```shell
python basedir_init.py
```
6. To take all of the files from the `application/excel_files/` path, pre-process them and populate a provided so far empty prices.db database, run: 
```shell
python database_init.py
```
7. Finally, run the following to start the application on the localhost 5000.
```shell
python app.py
```

### Option 2 - In a Docker Container

If you want to run everything in a prepared Docker environment - this can be done. Follow the following steps to prepare your set up:

1. Get familiar with the documentation by going through the following README.md files: [How the database is prepared](https://github.com/Si-ja/Dashboard-Python/tree/main/application/config_handlers/db_management), [How to prepare the database before running the application](https://github.com/Si-ja/Dashboard-Python/tree/main/application/database)
2. Download the repository
3. Make all of the needed preparations, indicated in the step 1.
4. Make sure you have `docker` and `docker-compose` installed on your machine.
5. Run the following command, while being located in the very root folder of the project, to build the continaer for the instance of the application and for the nginx (the containers also will automatically be served):
```shell
docker-compose up --build
```
6. Access `localhost:80`. You should be able to interact with the application.

#### Note of caution:

The containers are built under names `application` and `nginx`. If you already have continaers that run with such names, you need to perform modifications to the `docker-compose.yml` and `/nginx/nginx.conf` files, so you would not have any naming issues on your end with other running prepared and/or containers.

## Currently known issues that are being worked on to be fixed

- [ ] Major: when excel files are downloaded from the resource provided, they are in the .xls format. The code was tailored to work on .xlsx format. The build of the docker containers fails if you use the default files as is. This is noted as the most essentail issue. 

- [ ] When a database is attempted to be populated, the idea was that the file for the database would be generated automatically as well. Unfortunatelly, when this is attempted, the database sometimes doesn't allow access to it, as it creates only in the __read-only__ format. The current solution applied: the `.db` file is provided as an empty template with the needed permissions set up, to function properly. Still looking for proper ways to optimize this.

- [X] Dockerization so far failed. The application wouldn't launch properly, but provide no clear erros why. The only trace of the issue was the __Internal Server Error__ message when the `localhost:80` would be accessed.

__Solution found__: Dash is built on top of Flask. However, it seems to not work well on it's own in a Docker container. The issue got resolved, by chaing the configuration of how the app was being launched from:

```python
# in the ui/__init__.py file
app = dash.Dash(__name__)

# in the app.py file
from ui import app as application
```

to 

```python
# in the ui/__init__.py file
base_app = flask.Flask(__name__)
app = dash.Dash(__name__, server=base_app)

# in the app.py file
from ui import base_app as application
```

- [ ] Some of the app.callback functions that are present in the base app have slight shortcommings. For instance: when the dataframes from which the information is pulled changes, the time frame in the RangeSlider on the bottom of the page does not reset. It doesn't pose a serious issue, but user-wise can be annoying.

- [ ] Make the Dashboard look more pretty.

- [ ] Noticed that the time range available for specification on the bottom of the dashboard does not change depending on the table provided and takes the full range of the initial table that was loaded. In the given context it is not a big issue, as in all case the data ranges are planned to be years long. However, this behaviour is not desirable and should be fixed.

- [X] Fix the grammar in the README.md files. Some instances of text look quite poor due to writing them in a rush.

- [ ] Figure how to optimize the documentation, as in the current state, particularly the set up from the user side to run everything, can appear confusing.
