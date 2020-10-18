# Dashboard for Electricity Prices

This is a small dashboard built with python and Dash, using SQLite as a database.

## What is this application about

It allows for an interactive visualization of information that represent electricity Day-Ahead prices in Europe per hour. Originally information has been retrieved from [Nord Pool](https://www.nordpoolgroup.com/historical-market-data/). To work with this dashboard you will have to retrieve the same information from the said source.

You can see few examples of how the Dashboard currently looks.

The Default State of how the Dash Board initiates. It always loads the first table in the database, with their second column, no matter what it is. (Note: the first column is reserved to represent the dates).

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/DefaultState.png "Default State")

You can change the tables selected, and the column values.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/AddingCountries.png "Add more variables")

You can also change the range - increase or decrease it, in respect to how many data points there are. So far the range was tailored to fit the sequential nature of the data used in the project.

![](https://github.com/Si-ja/Dashboard-Python/blob/main/application/visuals/ChangingRange.png "Change Range")

## How to run

### Option 1 - On your Personal Machine

Please follow the steps to make the dashboar work on your computer (originally the set up was done on Linux and might slightly differ from the Windows one):

__Prerequisits:__ It is assumed you have python and pip installed on your computer already. 

1. Download/Clone the repository.
2. Navigate to the `Dashboard-Python/application/` folder.
3. Open the terminal in the given folder and execute the following command to set up a new working environment:
```shell
python3 -m venv env
```
4. Make sure the new environment is selected for opperations:
```shell
source env/bin/activate
```
5. Install all the needed dependencies for python through:
```
pip install -r requirements.txt
```
6. To generate a .json file (it will appear in your Dashboard-Python/application/` folder that will help the dashboard navigate between the new database that will be generated from scratch and its UI, run:
```shell
python basedir_init.py
```
~~7. Populate the `Dashboard-Python/application/excel_files/` folder with the data you retrieved from [Nord Pool](https://www.nordpoolgroup.com/historical-market-data/). Originally, the files with which work was done were called `elspot-prices_2018_hourly_eur.xls.xlsx`, `elspot-prices_2019_hourly_eur.xls.xlsx`, `elspot-prices_2020_hourly_eur.xls.xlsx`. Unfortunatelly, in other formats, besides `.xlsx` the files are not read properly. This is noted as an issue, and is being worked on.~~

~~8. Delete the `DELETEME.txt` file in the `Dashboard-Python/application/excel_files/` path.

9. Populate an SQLite database, that is located in the `Dashboard-Python/application/database/` (do not navigate there, stay in the terminal at `Dashboard-Python/application/`) by running the following command:
```shell
python database_init.py
```
10. Run the following to start the application:
```shell
python app.py
```
11. Keep the terminal opened and open your browser of choice and navigate to the `localhost:5000`. You should be able to interact with the newly created dashboard.

__Additional:__ To stop the application running, either close the terminal or press `Ctrl+C` in the terminal.

### Option 2 - In a Docker Container (Please read the WARNING section of this instruction before performing the set up).

__Prerequisits:__ It is assmed you have `docker` and `docker-compose` installed on your computer.

1. Download/Clone the repository.
2. Navigate to the `/application/` folder.
~~3. Populate the `Dashboard-Python/application/excel_files/` folder with the data you retrieved from [Nord Pool](https://www.nordpoolgroup.com/historical-market-data/). Originally, the files with which work was done were called `elspot-prices_2018_hourly_eur.xls.xlsx`, `elspot-prices_2019_hourly_eur.xls.xlsx`, `elspot-prices_2020_hourly_eur.xls.xlsx`. Unfortunatelly, in other formats, besides `.xlsx` the files are not read properly. This is noted as an issue, and is being worked on.

4. Navigate to the `Dashboard-Python/` folder. 
5. Open the terminal from the said path.
6. Build and server 2 docker containers, that will allow for interactivity with the developed Dashboard by running:
```shell
docker-compose up --build
```
7. Open your browser of choice and navigate to the `localhost:80`. 

__Additional:__ Do not forget the close and if required delete the ruinning containers, after you are done working with them.

__WARNING:__ The 2 containers to run the dashboard and allow for interactions with it are built under names `application` and `nginx`. If you already have continaers that run with such names, you need to perform modifications to the `docker-compose.yml` and `Dashboard-Python/nginx/nginx.conf` files, so you would not have any naming issues on your end with other running and/or prepared containers.

## Currently known issues that are being worked on to be fixed

- [ ] Major: when excel files are downloaded from the resource provided, they are in the .xls format. The code was tailored to work on .xlsx format. The build of the docker containers fails if you use the default files as is. This is noted as the most essentail issue. 

- [ ] When a database is attempted to be populated, the idea was that the file for the database (i.e. `.db`) would have been generated automatically as well. Unfortunatelly, when such approach is attempted, the database sometimes doesn't allow access to it afterwards, as it creates only in the __read-only__ format. The current solution applied: the `.db` file is provided as an empty template with the needed permissions set up, to function properly. Still looking for proper ways to optimize this.

- [X] Dockerization so far failed. The application wouldn't launch properly and didn't provide clear erros to why. The only trace of the issue was the __Internal Server Error__ message when the `localhost:80` would be accessed.

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

- [ ] Some of the app.callback functions that are present in the base app have slight shortcommings. For instance: when the dataframes from which the information is pulled changes, the time frame in the RangeSlider on the bottom of the page does not reset to the new dataframes time period. This doesn't pose a serious issue, but user-wise can be annoying.

- [ ] Make the Dashboard look more pretty.

- [ ] Noticed that the time range available for specification on the bottom of the dashboard does not change depending on the table provided and only takes the full range of the initial table that was loaded. In the given context it is not a big issue, as in all cases the data ranges are planned to be of 1 years length. However, this behaviour is not desirable and should be fixed.

- [X] Fix the grammar in the README.md files. Some instances of text look quite poor due to writing them in a rush.

- [X] Figure how to optimize the documentation, as in the current state, particularly the set up from the user side to run everything, can appear confusing.
