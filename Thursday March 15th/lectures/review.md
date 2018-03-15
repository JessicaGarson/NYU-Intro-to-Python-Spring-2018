## Review
We're going to review some recent concepts we've covered.

## Git
- Git vs GitHub  
- Clone vs Forking

## How do we add files
```
git status
git add <file_name>
git status
git commit -m "adding new file"
git status
git push
```

## What are virtualenvs
They are a fresh start without the weight of the baggage of your computer so you can install packages in isolation.

For macs:
```
virtualenv newvenv
source newvenv/bin/activate
```
For PCs:
```
virtualenv newenv
source first_env/Scripts/activate
```

Another option:
```
virtualenv newenv
. .\newenv\Scripts\activate.ps1
```
If you get a permission error while running this. Try this: 
```
Set-ExecutionPolicy RemoteSigned
```
