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
      * Run `git commit -m "Initial commit: Minimal resistor power calculator app."`
    * Create a remote repository
      * On GitHub create a new repository and give a description
    * Link your local repository to the remote repository
      * Run `git remote add origin https://github.com/.../<repository-name>.git`
    * Push the local state to the main branch of the remote repository
      * Run `git push -u origin main`

  ## 5. Deploying to Streamlit Community Cloud
  * Prepare GitHub repository
    * File `app.py` should be in the root directory or the repository
    * Create a requirements.txt file to track Python libraries the app needs
      * All installations are tracked in Pipfile
      * Generate requirements.txt from Pipfile
        * Run `pipenv run pip freeze > requirements.pip`
      * Commit and push the requirements to the remote repo
        * Stage changes and new requirements.txt
        * Review all changes
        * Commit changes including requirements.txt file
        Push the state to the remote repo
* Deploy to Streamlit Community Cloud
  * Create a Streamlit Community account (sign in with GitHub)
  * On Streamlit's dashboard, select 'Create app'
  * Select the GitHub repo
  * Set the branch to `main`
  * For 'Main file path" specify `app.py`
  * Click 'Deploy'

  Streamlit will use `requirements.txt` to install streamlit and then build and host the app. You get a URL to the app.

* Test the deployed app
  * Visit the URL Streamlit provides
  * Test the app
    * If it fails:
      * check the error logs
      * Fix locally, commit and push
      * It will auto-update



