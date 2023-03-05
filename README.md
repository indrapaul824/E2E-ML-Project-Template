# End to End ML Project Template

A generic End-to-End Machine Learning project structure template which can be used to kickstart literally any ML Project.

## Steps followed to build this template

### Day 1: Project Setup

1. Create a new Project folder in your local machine with the following files:

    ```bash
    ├── README.md
    |── Makefile
    |── requirements
    |   |── dev.in
    |   |── prod.in
    |── environment.yml
    |── .gitignore
    |── setup.py
    |── src
    |   |── __init__.py
    ```

2. Open the terminal and navigate to the project folder and call the make command that you defined in the Makefile:

    ```bash
    make setup
    ```

3. This will create a conda environment. It will also build the package and install it in the environment. It will also install the dev and prod requirements.

4. Create a GitHub repository, init your local folder and add, commit and push the files to the repository.
