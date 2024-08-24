# Getting started 🚀

## Setting up Docker

Download Docker Desktop from [Docker Docs](https://docs.docker.com/desktop/).

### Testing Docker Installation

Run the `hello-world` docker container.

```bash
# Open terminal and run this command
$ docker run hello-world
```

#### If Docker is installed, you should receive the following output:

```bash
####################################
        # Terminal output ##
####################################

# Docker couldn't find image locally
Unable to find image 'hello-world:latest' locally

# Docker pulling image from Docker Hub
latest: Pulling from library/hello-world
478afc919002: Pull complete
Digest: sha256:53cc4d415d839c98be39331c948609b659ed725170ad2ca8eb36951288f81b75
Status: Downloaded newer image for hello-world:latest

# Docker running the container
Hello from Docker!
This message shows that your installation appears to be working correctly.

# More information
To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (arm64v8)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/
```

#### The Docker image will now be on your machine:

```bash

$ docker image ls

# List `ls` all images on machine
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
hello-world   latest    ee301c921b8a   15 months ago   9.14kB

```

#### As well as the Docker container:

```bash
# List all (`-a`) containers on your machine.
$ docker ps -a
# You should see the `hello-world` container.
CONTAINER ID   IMAGE         COMMAND    CREATED          STATUS                      PORTS     NAMES
e0283dbf8241   hello-world   "/hello"   26 minutes ago   Exited (0) 15 minutes ago             loving_galileo
```
