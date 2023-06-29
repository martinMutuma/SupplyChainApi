# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.12-bookworm

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# RUN git config --global --unset http.proxy
# RUN git -config -global --unset https.proxy

# RUN git config --global http.sslverify false

RUN apt-get -y update \
    # Cleanup apt cache
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
RUN mkdir /opt/app/supplychainapi

COPY requirements.txt  /opt/app/
COPY .pip_cache /opt/app/pip_cache/
COPY SupplyChainApi /opt/app/supplychainapi/

# Get the Real World example app

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR  /opt/app

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN chown -R www-data:www-data /opt/app



EXPOSE 80

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]