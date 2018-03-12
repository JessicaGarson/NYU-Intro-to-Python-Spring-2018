# Let's play around with everything we've been learning lately

# Part 1

## Make a repository called Pair-Programming-March-18th and clone into it
Let's first make new repository to put everything we're going to do in this session in it.

## Create a new environment
Make a virtual environment

## Install Jupyter into the new environment
Install jupyter into that environment

## Run a notebook
Get your notebook started.

## Solve the following problem in your notebook
- Create a dictionary with the name, favorite song, github handle, and twitter handle of you and your partner.

- Create a loop so that you get the following output:
```
Name: Name1
Song: Song1
GitHub: GitHub1
Twitter: Twitter1
Name: Name2
Song: Song2
GitHub: GitHub2
Twitter: Twitter2
```
## Add your changes to git.
You will want to add the jupyter notebook to python. Make sure you commit and push your file.

# Part 2
## Syncing your fork
Remember that fork we created in our first class. Let's try this again.

```
git clone https://github.com/yourname/name_of_repo.git
cd sample_to_be_forked
git remote add upstream https://github.com/repo_creator/name_of_repo.git
git fetch upstream
git checkout master
git merge upstream/master
git push
```

## Create a Jupyter Notebook
Create a notebook to solve the problem.

## Sets
Create a set of students who were at last class (just make this up) and another set of students who are in this class. Create a program which tells you who came to this class but not last, last class but not this one, and who came to both classes.

## Add this your fork
Add the code to your fork in today's repo under the pair_programming folder

## Submit a pull request
Submit a pull request when you are done.
