# Homework 4 Steps
If you are feeling a bit lost, this document will walk you through how to set up to create a repository, and virtualenv for solving this assignment.

## Steps
If you need some guidance in solving this assignment. Here are some steps you can follow.  

### Step 1 - Make the repository
Make the repository inside of GitHub.

### Step 2 - Clone your repository

This is an example using a repo we created called name_of_repo you will change this to your username and your repository name.
```
git clone https://github.com/your_github_user_name/name_of_repo.git
cd name_of_repo
```

### Step 3 - Create a virtualenv
You can now create a virtual environment so that you can have fresh environment to upload new packages to.

For macs:
```
virtualenv env
source env/bin/activate
```

For PCs:
```
virtualenv env
source env/Scripts/activate
```

### Step 4 - Install jupyter notebook. Install jupyter notebook in your new environment.
Might just be pip instead of pip3 depending on your set up.
```
pip3 install jupyter
```

### Step 5-  Start the notebook
```
jupyter notebook
```

### Step 6 - Solve the Problems
In the notebook, solve the problems above. Make sure you save the notebook. You might choose to have 3 notebooks for each problem.

### Step 7 - End the Notebook
Go back into your terminal end your your notebook session.
```
control-c
say y when prompted to end the notebook
```

### Step 8 - Add, Commit, and push your code to GitHub.
```
git add .
git status
git commit -m "adding new notebooks"
git status
git push
```

### Step 9 - Send me a link
Send me a link to your new notebook.
