#  Dockerfile, Image, Container

# Use the official Python 3.11.1 image as the base image
FROM python:3.11.1

# Set the working directory within the container
WORKDIR /code

# Copy the necessary files and directories into the container
COPY ./requirements.txt /code/requirements.txt
COPY app /code/app

# Install Portaudio libraries for pyAudio dependencies
RUN apt-get update
RUN apt-get install libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev -y

# Upgrade pip and install Python dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Define the command to run the Flask application using python
CMD ["python", "app/app.py", "--port", "2005"]


#Build a Docker Image
#docker build -t api-flask .

#Start a Docker container and to run the container in detached mode, use -d.
#docker run -d -p 2005:2005 --name api-flask-container api-flask