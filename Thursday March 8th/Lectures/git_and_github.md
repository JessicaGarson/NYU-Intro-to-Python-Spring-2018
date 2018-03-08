# Git and GitHub

## Git
Did you ever wish you could go back in time. With git you can. Git is a version control tool. Git keeps track of changes across a collection of files for us. When we use Git, we can see what changes we made and seamlessly merge them with changes from our coworkers.

This is a tool we are going to us daily as developers. This was why we introduced this concept on the very first day so that we already have some familiarity with the subject.

## GitHub
GitHub is a social wrapper for git. This allows us to fork and make pull requests as we did in the first class. We can therefore also host our code on GitHub.

## Repositories
Repositories are the central place where things are kept.

## How to create one
To create a repo you can go into GitHub and click on the bit + in the right hand corner.

## Cloning
Cloning allows us to bring our repository into our own environment

## Forking
Forking gives us our own version of repository that we can make changes and it can live independently of each other.

## How to create a repository and add files to it
1. Create a repository in GitHub
2. Clone it into your local environment
```
git clone <new repository>
```
You will likely be prompted to enter in your GitHub username and password. If you have 2 factor auth turned on which you should (two factor all the things), [If you are using HTTPS Git, instead of entering your password, enter a personal access token. These can be created by going to your
[personal access tokens page](https://github.com/settings/tokens)
3. Open this directory in an atom and write code!
```
atom .
```
4. Pull any changes
```
git status
git pull
```
5.  When you are reached a stopping point. Add your files to the stage area.
```
git status
git add name_of_file.py
```
If you want to commit all the files - be very careful with this you can use the following syntax
```
git add .
```
6. Commit it
```
git status
git commit -m "descriptive commit message"
```
7. Push the changes to directory.
```
git status
git push
```

## Resources
- [Create A Repo](https://help.github.com/articles/create-a-repo/)
- [Cheatsheet](https://git.generalassemb.ly/ga-wdi-lessons/git-intro/blob/master/cheatsheet.md)
- [How to undo almost anything with git](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/)
