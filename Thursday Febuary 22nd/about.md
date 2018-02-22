# Thursday February
We're going to review functions and practice writing functions.

Slides are found [here](http://jessicagarson.com/NYU-Intro-to-Python-Feb-22/#/).

## Agenda
### 6:30 - 6:35
A note on learning python in 2018
### 6:35 - 7:00
Review of functions
### 7:00 - 8:00
Working on activities

## A Note
With many different resources out there and may different ways to learn how to code these days, it's very easy to find resources that teach in a different order than I do. We also all have different backgrounds and may have been exposed to a more advanced way of solving the problem. One of my favorite things about code is that there are many different ways to accomplish a goal. I know we all come from different backgrounds and that temptation to jump ahead can be great, but please try to practice and make sure we fully master a concept before trying things using concepts we haven't introduced yet. We are here to make sure we have a strong foundation that we'll later build off of. If you quickly master a concept, this is your opportunity to help out another student who might not.

## Outside Problems
Right now is the best time to learn how to code, with hundreds of free resources at our fingers anyone can have the resources to become a developer and this is very exciting. This class is designed to cover the basics so we can conquer harder problems in the future. If you get lost with another resource, that's okay where we are now. However my job as your instructor for this class is to guide you on a journey as I have seen works the best for my students in the past and based on my own journey as a developer. As of today, I'll only be helping with problems as it relates to the assigned materials and concepts that we have covered in this class.

## Atom Shell Commands
You might need to install shell commands for atom to make this work properly.

## A Note on Conditionals
A note on conditionals. If we only have 2 conditionals, an if and an else is preferred.

```python
if len(sentence) <= 280:                               
    print ('Congrats!, your sentence fits in a tweet')
else:
    print ('Sorry, you need to trim your sentence')
```

Try to avoid double if statements, and for multiple conditions use elif. This is the best practice for 3 or more conditions. You can have as many elifs as you need.

```
if condition:
    do something
elif other_condition:
    do something else
elif another_condition:
    do something else too
else:
    do another thing
```

## A Note on the Homework
The homework is due Monday at 6:30pm. Please email me a .py file attached to an email.

Since a few folks have asked about the make tags assignment. I figured I'd go over it.

Your job is to create a function that looks something like this:
```
def make_tags(tag, word):
  # your code here
  return formatted with tags around it
```

So if you run make_tags('i', 'Yay') you will get the following:
```python
make_tags('i', 'Yay')
# result would be <i>Yay</i>
```

## How to Prep for the Next Class
- [Loops Python Tutorial](https://www.datacamp.com/community/tutorials/loops-python-tutorial)
- [Lists - Automate the Boring Stuff](https://automatetheboringstuff.com/chapter4/)
- [Lists Dive into Python 3](http://www.diveintopython3.net/native-datatypes.html#lists)
