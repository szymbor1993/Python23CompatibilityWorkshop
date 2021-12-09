# Snipping words

## Disclaimer

This code is intended to be non-optimal or use improper functions & statements, for the sake of the workshop.

## Description

User enters data to the program **written in Python 2**. Data is a dictionary in format: 

```text
{
    ...
    "<owner name>": "<words space-separated>",
    ...
}
```


However, program corrupts data in the way, that words, that are longer than average length (of the same owner), are being reversed. Also, all words are de-capitalized.

### Example

```text
I am with various words smaller and LARGER
```
is transformed into:
```text
i am htiw suoirav sdrow rellams and regral
```

## How to execute program

You can execute program in IDE by clicking green triangle near line with `if __name__ == '__main__':`, or just run the 
whole file as a script.
The exemplary output from the program:
```text
Enter number of entries: 3
Enter owner name: Tom
Enter his words separated with space: I am the best here
Enter owner name: Mary
Enter his words separated with space: I do not know what is going here
Enter owner name: Ralph
Enter his words separated with space: I have a bad feeling about this
Owner Ralph, his words: I have a bad feeling about this
Owner Mary, his words: I do not know what is going here
Owner Tom, his words: I am the best here

Loading entries finished. Now processing them...
Processing ended. Now you can access them.
Provide name, or type 'exit' to exit program: Tom
Owner Tom, his words: i ma eht tseb ereh
What now? Mary
Owner Mary, his words: i do ton wonk tahw is gniog ereh
What now? Ralph
Owner Ralph, his words: i evah a dab gnileef tuoba siht
What now? exit
Exiting

```

## Task

* Your task is to **rewrite** this program to work in **Python 3**,
* Don't use any modules and libraries for Python 2/3 compatibility,
* You can run prepared tests (file test_snipping_words.py) or write your own.


### Tests

You can use tests present in `test_snipping_words.py`. In order to do that, execute them from Pycharm IDE, or by issuing
the following command (replace `python` with appropriate command, if you have both versions):

```text
python -m unittest test_snipping_words.TestSnippingWords 
```