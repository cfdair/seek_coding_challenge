# SEEK Coding Challenge

## Description

This coding challenge contains a PDF(not linked) referring to some 
dataset, and posing some questions regarding that data.

This project is setup to answer those questions.

The main assumption of this project is that the environment will
have access to Docker.

Various make targets will be provided for simplicity, however,
the specific bash commands will be provided to adhere to the docker requirement.

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

To download the data, execute the following script:
```bash
export $(cat .env | xargs) && bash bin/download_dataset.bash
```
from the root directory, or execute:
```bash
make download
```