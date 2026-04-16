## Python Flask Skeleton for Google App Engine

Make sure gcloud init has been called to set up google credentials.
Also points to project: artistannamir

### Using pyenv 3.12
% pyenv install 3.12
% pyenv local 3.12
% python -m venv env
% source env/bin/activate
% pip install -r requirements.txt

2. Run locally:

% gunicorn -b 127.0.0.1:8080 main:app
# (or simply: % python main.py)

3. To deploy the application:

% gcloud config set project festive-flight-109023

% gcloud app deploy

You can stream logs from the command line by running:
  $ gcloud app logs tail -s default

To view your application in the web browser run:
  $ gcloud app browse

  