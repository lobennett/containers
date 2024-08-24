# Containers 📦

> This repository contains demos for Docker & Singularity.

## What are containers?

### Defined

> "Containers are lightweight packages of your application code together with dependencies such as specific versions of programming language runtimes and libraries required to run your software services." - Google Cloud

### Benefits

#### Move fast

Containers make continuous integration and deployment much easier, avoiding concerns about dependencies and environments.

#### Run anywhere

Containers can run virtually anywhere: on Linux, Windows, and Mac operating systems; on virtual machines or physical servers; on a developer's machine or in data centers; or in the cloud.

#### Reproducible and portable

Avoid the "works on my machine" problem. This is especially an issue with Python, commonly called [dependency hell](https://medium.com/knerd/the-nine-circles-of-python-dependency-hell-481d53e3e025).

```shell
# Dependencies rely on different versions of pandas
- App v0.0.1
  - foo v0.4.1
    - pandas
      - v2.2.2
  - bar v0.2.1
    - pandas
      - v.1.4.4
```

### Containers vs Virtual Machines

A virtual machine (VM) is a "virtual" version of a computer with its own computing environment. It runs independent of the host machine and thus provides many of the same benefits as containers with regard to isolation and security. However, unlike containers, virtual machines emulate the user's hardware, making their boot up times much longer. VMs also require much more storage (GBs vs MBs) and are not easily version controlled by the developer.

## Docker 🐳

> Docker is a tool for packing applications into containers—isolated environments for distributing, testing, and executing applications.

### Related Reads 📚

> [Infrastructure Engineering: A Still Missing, Undervalued Role in the Research Ecosystem](https://arxiv.org/abs/2405.10473)
>
> [An introduction to docker for reproducible research.](https://arxiv.org/abs/1410.0846)
>
> [Ten Simple Rules for Writing Dockerfiles for Reproducible Data Science](https://www.researchgate.net/publication/340734163_Ten_Simple_Rules_for_Writing_Dockerfiles_for_Reproducible_Data_Science)

### Common Terms

#### Image

Template with instructions for creating a Docker container, like a blueprint.

#### Container

A runnable instance of an image, much like a house built from a blueprint.

#### Dockerfile

Text document containing commands for building a docker image.

#### Container registry

Storage system for creating, managing, and sharing images. The largest registry is [Docker Hub](https://hub.docker.com/) (basically `GitHub` for containers).

### Requirements

#### Operating system

Docker is supported on most modern operating systems including various Linux distributions, macOS, and Windows.

#### Software

1. Install Docker Desktop from [Docker Docs](https://docs.docker.com/desktop/).
2. Ensure it is running correctly. For more detail instructions, see [setup guide](docs/setup.md).

### [Docker Encyclopedia](docs/docker_essentials.md)

> Everything you need to know about pulling images and running containers with Docker.

---

## Singularity/Apptainer

> Simple, fast, and secure container platform designed for ease-of-use on shared systems and high performance computing (HPC) environments (like Sherlock).

### Related Literature

> Kurtzer GM, Sochat V, Bauer MW (2017) Singularity: Scientific containers for mobility of compute. PLoS ONE 12(5): e0177459. https://doi.org/10.1371/journal.pone.0177459

### [Singularity Encyclopedia](docs/singularity_essentials.md)

> Everything you need to know about pulling images and running containers with Singularity.

---
