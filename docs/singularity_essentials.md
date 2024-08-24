# Singularity - Essentials

#### Pulling a singularity image

Download a singularity image from a registry.

1. `docker://`: a container on Docker Hub
2. `shub://`: a container on Singularity Hub # deprecated
3. `[container_name].simg`: a container image file

```bash
$ singularity pull [IMAGE_NAME]

Example:
singularity pull docker://hello-world
```

#### Running a Singularity container

```bash
$ singularity run [IMAGE_NAME]

Example:
singularity run hello-world_latest.sif
```

#### Execute a command to the Singularity container

```bash
$ singularity exec [/path/to/container.simg] [/path/to/container_executable] [ARGS]

Example:
singularity exec $SCRATCH/.singularity/salad.simg /code/salad fork
```

#### Create an interactive shell instance inside the image

```bash
$ singularity shell [OPTIONS] [/path/to/container.simg]

Example:
singularity shell $SCRATCH/.singularity/hello-docker.simg
```
