# Select base image from Docker
FROM python:3.12-alpine

# Add metadata
LABEL author="Poldrack Lab" version="1.0" description="Hi from Docker!"

# Set working directory
WORKDIR /code

# Copy over scripts
COPY main.py /code

# Define environmental variables
ENV NAME=World

CMD ["python", "/code/main.py"]