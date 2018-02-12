# How to Keep a Fork Current

## Configure your environment with your GitHub user info
Use the directions found [here](https://services.github.com/on-demand/github-cli/git-configuration) to make sure you have your environment set with your GitHub information.

## 1. Clone your fork:

You will need to first clone your fork which brings your fork from your github into your own computer.

```
git clone git@github.com:YOUR-USERNAME/YOUR-FORKED-REPO.git
```

## 2. Add remote from original repository in your forked repository:

```
cd into/cloned/fork-repo
git remote add upstream git://github.com/ORIGINAL-DEV-USERNAME/REPO-YOU-FORKED-FROM.git
git fetch upstream
git checkout master
git merge/upstream master
git push
```

## 3. Updating your fork from original repo to keep up with their changes:

```
git pull upstream master
```
