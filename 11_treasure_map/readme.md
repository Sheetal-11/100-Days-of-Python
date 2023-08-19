# Treasure Map

This program marks a spot with an X.

The variable `map` contains a nested list that looks like this:
```python
['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']
```

Using new lines `\n` to format the three rows into a square, like this:
```python
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
['⬜️', '⬜️', '⬜️']
```

This is to try and simulate the coordinates on a real map.

This program allows you to mark a square on the map using a two-digit system. 

> - The first digit for the input will specify the column (the position on the horizontal axis). 
> 
> - The second digit in the input will specify the row number (the position on the vertical axis).

#### Example Input 1:
column 2, row 3 would be entered as:

> 23


#### Example Output 1:
> ['⬜️', '⬜️', '⬜️']
>
> ['⬜️', '⬜️', '⬜️']
>
> ['⬜️', 'X', '⬜️']


#### Example Input 2:
column 3, row 1 would be entered as:

> 31


#### Example Output 1:
> ['⬜️', '⬜️', 'X']
>
> ['⬜️', '⬜️', '⬜️']
>
> ['⬜️', '⬜️', '⬜️']



