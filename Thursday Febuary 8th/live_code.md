# Live Code - The Command Line

## Let's First Confirm Set Up
Go to your terminal or powershell and type python. If you don't see something similar to my screen come find me after class. After we are done let's exit. This is how to get into what's known as the interactive interpreter.

```bash
python
exit()
```

## This Might Look Familiar
If you are older, this might remind of you the old set up of a computer. This means you have a leg up for today's class.

## A New Way to Interact With Your Computer
Instead of interacting with your computer via finder on a Mac or File Explorer. We can use commands.

## Where Am I?
Print working directory.
```bash
pwd
```

## Take Me Back
How to Go Back to The Top Level Directory
```bash
cd ~
```

## Change Directory
Let's go to the documents directory.
```bash
cd documents
```

## Make A New Directory
To make a new directory we'll use `mkdir` to do so.
```bash
mkdir class_demo
```

## You Can Also Make Directories Inside of Directories
```bash
mkdir class_demo/demo_1
mkdir class_demo/files_for_demo
```

## Go Up One Directory
`cd ..` allows us to go up one directory.
```bash
cd ..
pwd
```

## Remove a Directory
This is one case where it depends on your computer how you can remove a directory.

For windows:
```bash
rmdir demo_1
```

For macs:
```bash
rm -rf demo_1
```

## Create a New File

For PCs:
```bash
pwd
New-Item new_file.txt -type file
New-Item hello.txt -type file
```

For Macs:
```bash
pwd
touch new_file.txt
touch hello.txt
```

## Remove a File
```bash
rm new_file.txt
```

## Move a File
This is also how you rename a file.

```bash
pwd
mv hello.txt whatsup.txt
mv whatsup.txt files_for_demo/whatsup.txt
```

## Let's Open Atom From The Command Line
```bash
atom .
```

## Let's Edit It
The file will now say - Hello what's up?

## Copy a file
```
cp whatsup.txt heywhatsup.txt
```

## View a file

Macs:

```
less heywhatsup.txt
```

Press q to quit this interface

PCs:
```
more heywhatsup.txt
```

## Stream a File
```
cat heywhatsup.txt
```

## Resources
- [Linux](https://opensource.com/resources/linux)
- [Bash Cheatsheet](https://learncodethehardway.org/unix/bash_cheat_sheet.pdf)
