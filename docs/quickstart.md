### Prerequisites

1. You need either of the following installed:
   1. Install via docker:
      1. Docker installed on your laptop
   2. Install Locally (optional):
      1. Python >= 3.8
      2. Install nodejs == 18.14.0
      3. Install terraform 1.3.1
      4. Install cerberus-python-client
2. Configure your github integration to your repos using [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).
3. Configure the databricks cli cfg file. `pip install databricks-cli` and then `databricks configure -t` which 
  will configure the databricks cli with a token. 


## Install Via Docker

We recommend to use docker container for development purposes as it's easier to have version upgrades by changing the docker version.

* Add the following alias to your profile or zsh_profile:
    
    ```shell
    alias bfs='docker run -it --rm --name brickflow -v "$PWD":/usr/src/brickflow -v ~/.databrickscfg:/root/.databrickscfg:ro -v ~/.ssh:/root/.ssh:ro -w /usr/src/brickflow <DOCKERHUB_URL_REPLACE>/brickflow:latest'
    ```

* Please change your directory to the root of your project. Then run the `bfs` command.

    ```shell
    bfs
    ```

* This will launch the bash shell inside the container. It will do the following:

     1. Mount your current working directory as read-write to the working directory in the container.
     2. Mount your `~/.ssh` directory as read-only to the `~/.ssh` in the container.
     3. Mount your `~/.databrickscfg` file as read-only to the `~/.databrickscfg` in the container.

* You will also need to install any required packages of your respective project inside the docker container.

### Upgrade the brickflow container
* If the brickflow version in your container is outdated and needed to upgrade then run the below command in your shell which pull the latest docker image
    
    ```shell
    docker pull <DOCKERHUB_URL_REPLACE>/brickflow:latest
    ```

## Install locally (optional if you choose not to use docker)

Alternatively instead of docker you can install locally but you will need to resolve all the deps.

The project relies on terraform and cdktf to deploy your python projects.

1. Install brew if not installed already using - [brew-install](https://brew.sh/)
2. Install node using `brew install node`
3. Install cdktf-cli via `npm install -g cdktf-cli`
4. Install the brickflow package via `pip install brickflows`

## Setup Project

* The first step is to initialize the project. It will do the following:

    1. Create the entrypoint.py file in your workflows module.
    2. Update your .gitignore file with the correct directories to ignore.

* To initialize the project inside the bfs shell run:

    ```shell
    bf init
    ```
  
* It will prompt you for the:
  
     1. Project Name
     2. Git https url of your project
     3. Workflows Directory Path
     4. Brickflow Version 
     5. Spark Expectations Version
  
