# Loops
Using loops we can automate and repeat tasks in a very short amount of time.

# For Loop
A for loop lets you use each item one at a time, which is great for performing actions a certain number of times.

With for loops the repeated execution of code based on a loop counter or loop variable. This means that for loops are used most often when the number of iterations is known before entering the loop.

```
For each item:
		do something with that item
```

# Range
Range creates a list of numbers that we can loop over.

```python
for number in range(0,9):
   print(number)
```

You can pass in between 1 and three arguments into range.

## With Range Think Start, Stop, Step
Start states the integer value at which the sequence begins, if this is not included then start begins at 0.

Stop is always required and is the integer that is counted up to but not included.

Step sets how much to increase (or decrease in the case of negative numbers) the next iteration, if this is omitted then step defaults to 1.

```python
for number in range(10):
	print(number)
```
```python
for number in range(1, 100, 5):
  print(number)
```
```python
for number in range(100, 0, -10):
  print(number)
```
## For Loops + Lists  
We can use a for loop to go through a list one by and do something with each item.

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for day in days_of_the_week:
    print(day)
```

```python
attendees = ['Celestino', 'Yasha', 'Hamid']

for attendee in attendees:
  print('{} is a student in this class'.format(attendee))
```

```python
integers = []

for i in range(10):
    integers.append(i)

print(integers)
```

## There Has To Be a Better Way!
While doing the sleep in problem on the homework, you likely noticed there might be a better way to solve it. Here is a solution with lists and loops!

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def sleep_in():
    for day in days_of_the_week:
        if day == 'Saturday' or day == 'Sunday':
            print('Today is {}, I can sleep in today!'.format(day))
        else:
            print('Today is {}, I have to go to work :('.format(day))


def main():
    sleep_in()


if __name__ == '__main__':
    main()
```
# Nested For Loops
Loops can be nested inside other loops.

```
for first iterating variable in outer loop:
    do something
    for second iterating variable in nested loop:   
        do something
```

```python
days_of_the_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

for week in range(1, 5):
    print('Week {0}'.format(week))

    for day in days_of_the_week:
        print(day)
```

## While Loops
The cousins of conditionals.

You can think of the while loop as a repeating conditional statement. After an if statement, the program continues to execute code, but in a while loop, the program jumps back to the start of the while statement until the condition is False.

```
while a condition is True:
  do something
```

```python
bread = 35
while bread >= 2:
    print("I'm making a sandwich")
    bread = bread - 2
```

```python
password = ''

while password != 'jessisthebest123!':
    print('What is the password?')
    password = input()
```
