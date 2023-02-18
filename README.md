# README

This document details the steps on how to run this project.

## Requirements
1.
    ```
    poetry install
    ```

## Running the project
To set it up for the first time, do the following:

1. First, copy `.env.template` to `.env` and set the vars for env, prd or both.
2. Test connectivity to the server:
    ```
    poetry run python airflow-cli.py --env prd connections list
    ```
3. Navigate through command line with the `--help` flag to see what commands are available.
