# Dictionaries

## Why
So lets say we wanted to create a list of names and Github handles for each student in the class. If we wanted to look up a specific person's Github handle, how could we do that?

We could zip together those lists but it would be complicated and messy.

## There has got to be better way!
Dictionaries are another way of storing information in Python.

Dictionaries have two components: a key and its corresponding value.

Think of it like a phone book or contact list! If you know my name, (key) you can look up my number (value)

## Dictionaries like sets are unordered
The order of your dictionary may change as you add or remove items!

## What does a dictionary look like
The syntax for a dictionary is:
```
dictionary = {key: value}
```
Here is dictionary of GitHub handles:

```python
handles = {'Michael': 'michaelshore93', 'Daniel': 'danielrein', 'Andrew': 'andyschneider85'}
```

## Accessing data items with keys
If we want to isolate Daniel’s GitHub username, we can do so by calling the key of Daniel.

```python
print(handles['Daniel'])
```

# Accessing all the keys
.keys() will create a list of all of the keys in your dictionary.

```python
print(handles.keys())
```
```python
for key in handles.keys():
  print('{} is a student in our class'.format(key))
```

## While dictionaries are unordered, we can sort their keys.

```python
for name in sorted(handles.keys()):
  print(name)
```

# Accessing all the values
.values() will create a list of all of the keys in your dictionary.
```python
print(handles.values())
```

```python
for value in handles.values():
  print('GitHub: {}'.format(value))
```

## Access all the keys and values
If we are interested in all of the items in a dictionary, we can access them with the items() function.
```python
print(handles.items())
```
This creates a list of tuples (our new bff from the beginning of class).

We can loop over these values as well:

```python
for key, value in handles.items():
    print('{} is the key for the value {}'.format(key, value))
```

## Adding values
You can add values using the following syntax:
```
dict[key] = value
```
So if we wanted to add the following
```python
handles['Alex'] = 'alexng89'
print(handles)
```

## Dict update
We can also add and modify dictionaries by using the dict.update()
```python
handles.update({'Alex': 'newhandle'})
```

## Removing items
To delete items we can use del to remove items.

The syntax is follows:
```
del dict[key]
```
```python
del handles['Andrew']
```
## Let's say we wanted an empty dictionary
.clear removes your dictionary.

```python
handles.clear()
```
