# WordLee-Solver

Python script to help us to solve WordLee daily challenge 

<img src="https://raw.githubusercontent.com/FernandezEnrique/.github/main/WordLee-Solver/wordle-img.png" width="300"/>

# How to run it

You need to have python installed, and only one module is required.
```python3
pip3 install random2
```

Now, we can just run it in a terminal

```python3
python3 main.py
```

# How to use it

Once we have ran it, we will see a menu to choose the length of the word and languaje.

Once it's started, we will be able to choose between 6 options.

Word example: `april`

We will choose option 5, to give us a random word. We get `apert`, p will be green.

It means that we know that it exists and its position. Option 1.
```
Letter: a
Position: 2
```

`r` will be yellow. It means that it exists but this is not the correct position. Option 2.
```
Letter: r
```

`t` and `e` will be grey. It means that they do not exist. Option 3.
```
Letter: t e
```

Option 5 to get a random word.
```
Option: 5
```

# Bibliography

Spanish words file: [olea GitHub](https://github.com/olea/lemarios/)

English words file: [dwyl GitHub](https://github.com/dwyl/english-words)
