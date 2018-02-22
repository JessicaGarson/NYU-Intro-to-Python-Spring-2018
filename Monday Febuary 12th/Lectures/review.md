# Review

## Command Line
We'll type these commands and we'll yell at what they do.
```bash
pwd
cd Documents
ls
ls -lrt
mkdir review
cd ..
cd Documents/review
touch hello_world.py
atom .
python hello_world.py
cd ~
```

## When does atom . work
Atom . only works when atom is open on your machine. Opening via atom is alright. We'll demo both methods.

## How to Sync a Fork
It's okay to be having trouble with git right now. We aren't going to dig deep into this until March 12th (a month from today).

```bash
git config --global user.name JessicaGarson
git config --global user.email jessica.garson@gmail.com
git clone https://github.com/JessicaGarson/sample_to_be_forked.git
cd sample_to_be_forked
git remote add upstream https://github.com/jlg17nyu/sample_to_be_forked.git
git fetch upstream
git checkout master
git merge upstream/master
git push
```

## A Note on 2 Factor Authentication
If you are using 2 factor authentication for GitHub (which you should be). If you are using HTTPS Git, instead of entering your password, enter a personal access token. These can be created by going to your
[personal access tokens page](https://github.com/settings/tokens).

## How to join the Python IRC Channel
Directions on joining the python IRC channel are [here](https://www.python.org/community/irc/).
