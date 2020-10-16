# Initiate the Python Image
FROM python:3.7.9-stretch

# Set the working directory to app
WORKDIR /app

# Copy the current directories contents into the container and /app folder
ADD . /app

# Install the dependencies
RUN pip install -r requirements.txt

# Run the generation of the directory.json file and the prices.db
RUN python basedir_init.py
RUN python database_init.py

# And make an entry point that will be handled by uWSGI
CMD ["uwsgi", "app.ini"]