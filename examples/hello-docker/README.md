# hello-docker

> Overview: Simple python script with no dependencies.
>
> Purpose: Shows simple Dockerfile setup and data permanence with Docker and Singularity.

## Instructions

### Build the image from the Dockerfile.

```bash
# Build image with `-t` tag that describes the application.

$ docker build -t "hello-docker" .
```

### Run the container

```bash
# Optional: Include an environmental variable `-e "name=Russ"` to pass to the script.

$ docker run -e "NAME=Russ" hello-docker
```

### Other things you can try

<details>
<summary>Create another instance of the container and see what happens.</summary>

Each time you `docker run hello-docker` a new container is spun up with a different name.

To remove all stopped containers, run `docker container prune`

Note: the data is no longer accessible from the container container after it stops. If you want the data to be accessible after the container exits, you must mount a partition using `-v`, such as: `docker run -e "NAME=Russ" -v ./log/:/code/log hello-docker`.

</details>

### Sherlock

Singularity is natively available on Sherlock.

To build this script to be used on Sherlock, you must specify the build platform as `amd64` and then push to Docker Hub: `docker buildx build --platform linux/amd64,linux/arm64 -t devloganbennett/test:latest --push .` Finally, from Sherlock, pull and run the image.

```bash
# Pull the image!
$ singularity pull docker://devloganbennett/hello-docker:latest
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
...
INFO:    Creating SIF file...

# Run the image!
$ singularity run --env NAME=RUSS hello-docker_latest.sif
```
