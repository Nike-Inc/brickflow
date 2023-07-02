### Prerequisites

1. Install Locally (optional):
   1. Python >= 3.8
2. Configure the databricks cli cfg file. `pip install databricks-cli` and then `databricks configure -t` which 
  will configure the databricks cli with a token. 

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
  
## gitignore

* For now all the bundle.yml files will be code generated so you can add the following to your .gitignore file:

    ```shell
    **/bundle.yml
    ```


## Post Setup

* To deploy run the following command

    ```shell
    bf deploy --deploy-mode=bundle -p "<profile>" -wd <workflows directory>
    ```

* To destroy run the following command

    ```shell
    bf destroy --deploy-mode=bundle -p "<profile>" -wd <workflows directory>
    ```