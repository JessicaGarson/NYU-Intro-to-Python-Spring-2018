# Pandas
So what is Pandas?

Pandas is a python library that allows for flexible data structures that makes data manipulation, file input, file output data cleaning, and simple computation easy.

For our purposes it makes working with csv and excel files really easy.

## How do I start?
To start you will need to install pandas.
```bash
pip install pandas
```

It's easier to see what's going inside of jupyter notebook. So you will need to install it and launch a notebook.
```bash
pip install jupyter
jupyter notebook
```

Once we have our notebook running we'll need to import the library of pandas in.
```python
import pandas as pd
```

## Yo Jess, What's that as, what does it do?
The as allows us to name an alias so it's easier to work with so we don't have to type pandas all the time.

## Reading flies in
To read files in we will use the method read_csv() to read in our file. Here we are reading in our file and saving it to a variable named df.

```python
df = pd.read_csv('name_score.csv')
```

For excel we would use the following syntax:
```python
read_excel('filename.xlsx')
```

## DataFrames the heart of pandas.
So you might have noticed that we named our variable df which is shorthand for data frame.

If you come from R, you might remember that a data frame in R is where each row of these grids corresponds to measurements or values of an instance, while each column is a vector containing data for a specific variable. This means that a data frame’s rows do not need to contain, but can contain, the same type of values: they can be numeric, character, logical, etc.

A data frame in pandas is similar. DataFrame is a 2-dimensional labeled data structure with columns of potentially different types. Similar to a spreadsheet or a SQL table.

# Let's make sure we loaded in our data correctly.
We can view the first 5 lines of our data by viewing the head of the DataFrame.

```python
df.head()
```

## Describe
This gives you descriptive statistics in a quick one line of code.  
```python
df.describe()
```

## Shape
Shape returns a tuple containing the shape of the DataFrame.
```python
df.shape
```

## Columns
We can see the columns with df.columns.
```python
df.columns
```
To rename the column with the trailing space we can use this code.
```python
df.rename(columns={'Name ':'name'}, inplace=True)
```

## Clean up the trailing spaces.
```python
df['Name'] = df['Name'].str.strip()
```

## Send to a csv
To send the python to a csv we can use this code:
```python
df.to_csv('cleaned_name_score.csv')
```

## What's the mean for scores?
Let's run this code to find out
```python
df['Score'].mean()
```
