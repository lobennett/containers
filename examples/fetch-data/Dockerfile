# Select base image from Docker
FROM python:3.12-alpine

# Add metadata
LABEL author="Poldrack Lab" "version"="1.0" "description"="Fetching RDoC data from Expfactory for RMR report!" \
MAINTAINER="Logan Bennett"

# Set working directory
WORKDIR /code

# Copy over scripts
COPY src/main.py /code/main.py
COPY src/utils.py /code/utils.py
COPY src/fetch.py /code/fetch.py
COPY requirements.txt /code/requirements.txt

# Define environmental variables
ARG API_TOKEN

ENV API_TOKEN=${API_TOKEN}

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/code/main.py"]