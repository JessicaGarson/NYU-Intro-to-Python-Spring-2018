# Lists
What are they?
- Lists are containers that can hold multiple pieces of information.
- Lists are commonly used to hold strings (ex: list of attendees’ names) or numbers (ex: number of attendees for each class).
- Sometimes called arrays.

## This would be annoying
```python
attendee1 = 'Celestino'
attendee2 = 'Yasha'
attendee3 = 'Hamid'
```
## There's got to be a better way!
There is! Lists are a data structure that allows us to hold multiple values.
- Lists are are created by placing items inside of [ ] 
- They are comma separated

Example from before as a list:
```python
attendees = ['Celestino', 'Yasha', 'Hamid']
```

An empty list looks like this:
```python
homework_2_not_turned_in = []
```

## How long is my list?
Our friend len works on lists too!
```python
print(len(attendees))
```

## Slicing does too! Whoa!
```python
attendees[0]
attendees[1]
attendees[2]
attendees[0:3]
attendees[2]
attendees[3]
```

## Adding one item to a list
.append() allows us to add one item to the end of the list
```python
attendees.append('Peony')
print(attendees)
```

## Changing list items
We can use slicing to change list items
```python
attendees[0] = 'Ayla'
print(attendees)
```

## Let's get rid of the last list item
```python
attendees.pop()
print(attendees)
```

## How do you sort a list?
```python
votes = [5, 4, 6, 3, 9, 1, 2]
votes.sort()
print(votes)

attendees.sort()
print(attendees)
```

## What if I don't want the last list item but another place?
We can specify the index(the slicing number) to remove whatever attendee we'd want.
```python
attendees.pop(1)
print(attendees)
```
## What if I want to add more than one item to the end of my list.
.extend() allows us to add a list of extra list elements to our list.
```python
attendees.extend(['Daniel', 'Joyce', 'Kelly'])
print(attendees)
```

## We can also reverse a list
```python
print(attendees.reverse())
```

## .split()
You can use .split() to take things from a string and turn it into a list.
```python
fruits = 'Apples, Oranges, Pears, Bananas'
fruit_list = fruits.split(',')
```

## What about removing more than one item?
Items can be removed from lists by using the del statement. In the same way as it can with .pop(). This will delete the value at the index number you specify within a list but you can also use a range.
```python
del attendees[0:2]
print(attendees)
```

## Combining 2 lists together
We can use the + operator to add lists together.
```python
print(votes + attendees)
```
