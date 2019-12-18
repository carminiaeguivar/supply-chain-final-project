# Statistical Process Control

This is the task related to SPC with package `PySpc` for Python.

## Steps for Linux

- sudo apt-get install python3-tk
- sudo apt-get install python-pip
- python3.5 -m venv env
- source env/bin/activate
- python -m pip install --upgrade pip
- pip install pyspc
- python index.py

Press `Ctrl + C` to close app, and run `deactivate` to leave virtual environment.

# About Dataset

Below it is the dataset's linf from Kaggle, used for this task.

https://www.kaggle.com/pablomonleon/311-service-requests-nyc

This dataset contains information about the complaints made to the NY Police Deparment in 2015. What I am trying to do here is to show the time from complain registration until it gets closed, in few words response time.

The `311_Service_Requests_Response_Time.csv` file contains the processed dataset, the response time of the requests from January 14th, 2015. In `notebook` folder you can find the notebook used to get this final csv file, step by step.
