# Docker - Essentials

## Dockerfile

Text document containing commands for building a docker image.

### FROM

```bash
FROM <image>
FROM <image>:<tag>
FROM <image>@<digest>

Example:
FROM ubuntu:18.04
```

### RUN

1. Shell Form: RUN <command>

```cmd
RUN python main.py
```

2. Exec form RUN ["<executable>", "<param1>", "<param2>"]

```cmd
RUN [ "python", "main.py" ]
```

### COPY

Copy new files or directories from source and adds them to the destination filesystem of the container

```cmd
COPY main.py /code
```

### ENV

Sets environmental variables <key> <value>

```cmd
ENV token "API_KEY"
```

### WORKDIR

Define working directory of container

```cmd
WORKDIR /code
```

### LABEL

Adds metadata to image

```cmd
LABEL version="0.1"
LABEL description="This is an example \
description for my application."
```

---

## Commands

### Search image

Search for an image in Docker Hub

```bash
$ docker search [OPTIONS] TERM

Example:
docker search hello-world
docker search --filter stars=100 hello-world
```

### Pull image

Pull an image from a registry to local machine

```bash
$ docker image pull [OPTIONS] NAME[:TAG|@DIGEST]

Example:
docker image pull debian:bookworm
```

### Push image

Push an image to the registry from local machine.

```bash
$ docker image push [OPTIONS] NAME[:TAG]

Example:
docker image push myapp:0.1
```

### List images

Display all Docker images stored on your local machine.

```bash
$ docker images [OPTIONS]

Example:
# List all images
docker images
# Only images from ubuntu repository
docker images ubuntu
```

### Remove an image

Remove Docker image by image id.

```bash
$ docker rmi [image_id]

Example:
# remove single id
docker rmi 894cac1e0c2d
# remove all images, uses Go text/template syntax
docker rmi $(docker images -q)
```

### Run container

Create and run a container from an image.

```bash
$ docker run [OPTIONS] [IMAGE_NAME]

Example:
docker run hello-world
```

### List containers

List all Docker containers.

```bash
$ docker ps [OPTIONS]

Example:
# List all containers, running.
docker ps
# List all containers, running and stopped.
docker ps -a
```

### Run container

Create and run a container from an image.

```bash
$ docker run [OPTIONS] [IMAGE_NAME]

Example:
docker run hello-world
# Run interactive bash terminal, automatically remove the container when it exits.
docker run --rm -it ubuntu bash
```

### Start or stop an existing container

Start or stop an existing container by name or container id.

```bash
$ docker start|stop [CONTAINER_NAME|CONTAINER_ID]

Example:
docker stop nginx
```
