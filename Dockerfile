# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.10.12

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# RUN git config --global --unset http.proxy
# RUN git -config -global --unset https.proxy

# RUN git config --global http.sslverify false

RUN mkdir /supplychainapi

RUN ls /

# Get the Real World example app
RUN git clone https://github.com/martinMutuma/SupplyChainApi.git /supplychainapi

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /supplychainapi

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt


VOLUME /supplychainapi

EXPOSE 80

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]