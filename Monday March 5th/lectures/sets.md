# Sets
Sets have been defined as a unordered bag of values. Sets have curly brackets around them.

## An empty set looks like this
```python
people_who_didnt_do_homework_2 = {}
```

## What does a set look like
```python
colors = {'blue', 'green', 'purple', 'orange', 'yellow'}
print(colors)
```

## So Jess, in one example I saw you defined a set as 'aeiou' but you didn't have the curly brackets around it. What is going on here?
```python
vowels = set('aeiou')
print(vowels)
```

## Our friend Len again!
```python
len(vowels)
len(colors)
```

## Slicing
Because of the fact that sets are unordered slicing won't work here.

## Adding one value to a set
.add() allows you to add one value to the set.
```python
colors.add('teal')
print(colors)
colors.add('purple')
print(colors)
```

## Whoa! Why didn't purple appear here when we printed it?
Because we can only have one value that is the same.

## Adding more values to a set
.update() allows us to add more values to a set.
```python
a_set = {1, 2, 3}
a_set.update({2, 4, 6})

colors.update({'pink', 'white', 'black', 'silver'})
print(colors)
```

## Removing items from a set
.discard() removes one item at a time.
```python
a_set.discard(1)
print(a_set)
colors.discard('black')
print(colors)
```
.pop() will remove a random item from the list
```python
a_set.pop()
colors.pop()
```

## True/False sets
```python
'black' in colors
'green' in colors
```
## Adding sets together
You can't use the plus operator on sets like we did with tuples.

## Common set methods
- The union() method returns a new set containing all the elements that are in either set.
```python
a_set = {5, 6, 9 , 10, 14}
b_set = {9, 4, 3, 10, 19, 14}
a_set.union(b_set)
```
- The intersection() method returns a new set containing all the elements that are in both sets.
```python
a_set.intersection(b_set)
```
- The difference() method returns a new set containing all the elements that are in a_set but not b_set.
```python
a_set.difference(b_set)
```
- The symmetric_difference() method returns a new set containing all the elements that are in exactly one of the sets.
```python
a_set.symmetric_difference(b_set)   
```
