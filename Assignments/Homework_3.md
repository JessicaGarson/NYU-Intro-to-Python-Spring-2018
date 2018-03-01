# Homework 3
## HTML States
Create a program that prints out an HTML drop down menu for all 50 states.

Here are the steps to complete this assignment.

## Step 1: Start with A List
Define your lists of states and list of state abbreviations. You can use [this resource to make it easier](http://www.liststates.com/).

## Step 2: Loop it Together
Essentially, you're telling Python:
```
for each state in my list:
  print this state.
```

## Step 3: Add the HTML Around It
Modify your loop to format the html code around the state name. The html for a state drop down is as follows:

```html
<select>
  <option value="state_abbreviation">Full state name</option>
</select>
```

The output of your file should look something like this:

```html
<select>
 	 <option value="AK">Alaskas</option>
 	 <option value="AZ">Arizonas</option>
 	 <option value="MD">Marylands</option>
</select>
```

## Save it to a File
Once your program runs the way you want it to. Make sure you save it to a file. 

***This assignment is due Thursday March 8th***
