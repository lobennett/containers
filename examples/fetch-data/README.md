# fetch-data

> Overview: Python script with dependencies to download and clean data from server.
>
> Purpose: Shows how to handle dependencies in Dockerfile and continuously deploy a container to automatically preprocess data.

## Details

### GitHub action setup, see [fetch-data.yml](../../.github/workflows/fetch-data.yml).

This Docker container is automatically built and run when a commit is pushed to this GitHub repository or according to a cron schedule specified in `/.github/workflows/fetch-data.yml`. The example here generates a `.csv` in `./out/` with subject data from a Prolific acqusition to help us easily monitor and quality control incoming data at regular intervals.
