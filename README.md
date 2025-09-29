# Creating a Streamlit App
This documents the process to create and deploy a Streamlit application with the Streamlit Community Cloud.

## 1. Create a project folder
* Create a new project folder inside a Streamlit Apps repository on your machine.

## 2. Initialize the project
* Create a virtual environment for the project.
  * `cd` to the project folder
  * Run `pipenv shell` to create a virtual environment
* Install Streamlit in the virtual environment
  * `pipenv install streamlit
  * Run `streamlit hello` to verify the installation

## 3. Write application logic
* Create an `app.py` file in the root directory.
* Write application code in `app.py`.
  * Iterate on the code
    * Update
    * Test
* Create a README to document the application.

## 4. Initialize version control and commit initial version
* Run `git init` from the root directory.
* Commit initial version
  * Stage `app.py` and any other related files
    * `git add app.py README.md`
  * Commit the initial code
    * Review code
    * Commit the code to the local repository
      * Run `git commit -m "Initial commit: Minimal resistor power calculator app."