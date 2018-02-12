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
```bash
git config --global user.name JessicaGarson
git config --global email jessica.garson@gmail.com
git clone https://github.com/JessicaGarson/sample_to_be_forked.git
cd sample_to_be_forked
git remote add upstream https://github.com/jlg17nyu/sample_to_be_forked.git
git checkout master
git merge upstream/master
git push
```
