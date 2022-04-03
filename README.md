# SEEK Coding Challenge

## Description

This coding challenge contains a PDF(not linked) referring to some
dataset, and posing some questions regarding that data.

This project is setup to answer those questions.

The main assumption of this project is that the environment will
have access to Docker.

Various make targets will be provided for simplicity, however,
the specific bash commands will be provided to adhere to the docker requirement.

### Assumptions
It is assumed that each profile relates to a unique person within the dataset.

Such that if two profile share a `firstName` and `lastName` they will be
considered different people who just happen to have the same name.

## Getting Started

This project assumes the following about the environment:
- that docker is installed
- that bash is installed
- (optionally) that GNU make is installed

### Setting up the credentials

The dataset download requires some credentials set
to unzip it.

To setup the .envrc file, execute the script:
```bash
bash bin/setup_envrc.bash
```
from the root directory, or execute:
```bash
make .envrc
```

### Downloading the data

To download the data, from the root directory execute the following script:
```bash
export $(cat .envrc | xargs) > /dev/null && bash bin/download_dataset.bash
```
or execute:
```bash
make download
```

### Executing the answers to the questions

To have the scripts print out the questions
and the associated answers, from the root directory execute the following command:
```bash
docker build . --build-arg UID=$$(id -u) --tag seek_coding_challenge && docker run -it -v $$(pwd):/opt/app/ -e UID=$$(UID) seek_coding_challenge
```
or execute:
```bash
make run
```

### Running the tests

To run the tests, from the root directory execute the following command:
```bash
docker build . --build-arg UID=$$(id -u)--build-arg POETRY_DEV_OPTION= --tag seek_coding_challenge_dev && docker run -it seek_coding_challenge_dev pytest
```
or execute:
```bash
make test
```
