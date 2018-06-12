# A few solutions on unpacking tuples
Here are a few ways to go about unpacking tuples.

## Formatting *
Since tuples are in an order you can use `.format(*task)` to grab each task in an order and bring it into your formatting.

```python
tasks = ('Wake up', 'Eat breakfast', 'Coding', 'Go boxing', 'Eat lunch',  'Go to class',  'Eat dinner', 'Watch TV series', 'Sleep')

def daily(major_tasks):
        print("Usually, I'll {} at 10 and {}, and I'll begin {} when having my breakfast. Then I'll leave home at 12 to {}, and after boxing I'll return home to {}. My class start at 3 so I'll leave at 2 to {}, and after the class I {} and {}. Usually, I {} at 2 am.".format(*major_tasks))


daily(major_tasks=tasks)
```

## Looping
You can also loop through a python as follows:
```python
DailyTasks = ('wake up', 'wash up', 'dress up', 'go to work', 'get breakfast', 'chug coffee',
              'work work work', 'eat lunch', 'work work work', 'chug another coffee',
              'work work work', 'leave work (finally!)', '(try to) go to the gym',
              'eat dinner', 'shower', 'watch TV', 'sleep',
              'dream about not finishing my Python homework',
              'realize the Python homework was just a dream', 'sleep soundly')

print("This is what I do on a daily basis:")
for i in DailyTasks:
    print("I {}.".format(i))
```
