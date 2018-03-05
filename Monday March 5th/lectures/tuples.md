# Tuples
Tuples are immutable. Meaning they are an unchangeable, ordered sequence of elements. While they look similar to lists, the difference is you can't change these.

## So when would I use tuples?
We use tuples when you don't want things to be changed. Because these can't be changed in the same was list they are considered faster from an optimization perspective.

## We know tuples by the ()
Here is an example tuple:

```python
days_of_the_week = ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
```

## Why is the above example good?
Because the order of days is unchanging.

## An empty tuple looks like this
```python
no_show_for_class_today = ()
```

## Our good friend Len!
Also works for tuples.

```python
len(days_of_the_week)
```

## Slice it up
Slicing also works here too!

```python
days_of_the_week[0]
days_of_the_week[1]
days_of_the_week[2]
days_of_the_week[3]
days_of_the_week[4]
days_of_the_week[5]
days_of_the_week[6]
days_of_the_week[0:3]
days_of_the_week[:5]
days_of_the_week[2:6]
days_of_the_week[:2]
days_of_the_week[-3:-1]
```

## What happens if we multiply tuples
Remember when multiplied a variable that contained a string and it printed 3 times.
```python
print(days_of_the_week * 3)
```

## Min and Max
If you are using numeric tuples min allows you to grab the lowest value and max allows you to grab the highest.
```python
votes = (5, 23, 99, 6, 9, 10)
print(max(votes))
print(min(votes))
```

## Can you add tuples together in the way we did with lists to combine them together?
Yes you can.

```python
days_of_the_week + votes
```
