FROM python:3.8.9

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

COPY src /drf_src
COPY requirements.txt /drf_src/requirements.txt
COPY scripts /drf_src/scripts

# Set the working directory to /drf
# NOTE: all the directives that follow in the Dockerfile will be executed in
# that directory.
WORKDIR /drf_src

RUN ls .

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

VOLUME /drf_src

EXPOSE 8000

RUN python manage.py migrate

CMD scripts/run.sh