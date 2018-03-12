# Homework 4
Due Monday March 19th

## Goal
The goal of this assignment is to solve a problem inside of a jupyter notebook and upload that notebook to a repository on GitHub.

## How to submit this assignment
Create a repository called "Name - Homework 4" and please put the code from this assignment there and send me the link.

## Due Date
This assignment is due March 19th

## Problem 1 - Dictionaries
Inside of a Jupyter notebook create a dictionary with a one sentence definition of  all the concepts we covered.

Use a loop to create an output that looks something like this:

```
Dictionary: A collection of key-value pairs.

String: A series of characters.

Boolean Expression: An expression that evaluates to True or False.

Comment: A note in a program that the Python interpreter ignores.

Value: An item associated with a key in a dictionary.

Loop: Work through a collection of items, one at a time.

List: A collection of items in a particular order.

Key: The first item in a key-value pair in a dictionary.

Float: A numerical value with a decimal component.
```

## Problem 2 - Sets
Create 2 sets one of your favorite movies and one of another person in your life's favorite movies.

- What favorite movies do you have in common with the other person?

- What movies are your favorite but aren't the other persons?

## Problem 3 - Tuples
Create a tuple of many of the major tasks you have to complete for the day in the order you have to complete them. So for example the tasks for me are as follows:

- wake up
- eat breakfast
- go to work
- eat lunch
- leave work
- go the gym
- eat dinner
- read
- sleep

Create a program that goes through this tuple and tells the story of a typical day for you.

## Steps
If you are feeling lost or need some guidance in solving this assignment. Here are some steps you can follow.  

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
