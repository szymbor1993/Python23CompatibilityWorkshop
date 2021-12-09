# Snipping words - foreign signs and symbols

## Disclaimer

This code is intended to be non-optimal or uses improper functions & statements, for the sake of the workshop.

## Description

This is the extension of the previous exercise. To make things more descriptive, let's say, that authors received some
new requirements and some "improvements":

* program needs to store data (words) in raw bytes (`bytes` type),
* data returned to the user should be of text type (`str` or `unicode`),
* words will be stored in a container, which will take responsibility to encode/decode words,
* all `range` calls are now need to be replaced with `xrange`, because performance ;) ;) ;)

Words are still being reversed and de-capitalized. The main function also remains unchanged, so you can use this program
in the same way as the previous one.

### Container for words

Authors have implemented a class `WordContainer` to wrap words, to mark them as `property` and then, implement both
getter and setter, in which words are being encoded/decoded. Also, an equality operator is overloaded to make comparison
simple.

```python
class WordContainer(object):
    def __init__(self, given_words):
        self._words = b""
        self.words = given_words

    def __eq__(self, other):
        return self.words == other.words

    @property
    def words(self):
        return self._words.decode(encoding="utf-8")

    @words.setter
    def words(self, new_words):
        if type(new_words) not in (str, unicode):
            raise TypeError, "Given input is of invalid type: %s" % type(new_words)

        self._words = new_words.encode(encoding="utf-8")
```

### How to execute program

You can execute this program in the same way, as in the previous exercise. Please keep in mind, that since we can now
operate on non-ascii characters (utf-8), we can have some problems with encoding of the console. Therefore, if you have 
weird symbols on the console when reading owner's words, don't worry - it can be bad console's encoding.


## Task

* Your task is to **rewrite** this program to be **cross-compatible**,
* It means, that your code should be able to run both on Python 2 and Python 3,
* You can (and should) use modules, like `six`,
* You can run prepared tests (file test_snipping_words.py) or write your own, but due to non-ASCII characters, there are
some problems when running them. Please refer to the next section for more details on how to run them properly.
  

### Tests

You can use tests present in `test_encoding_snipping.py`. If you want to run them from the console, you can do it the
same way as in the previous example (replace `python` with appropriate command, if you have both versions):

```text
python -m unittest test_encoding_snipping.TestEncodingSnipping
```

However, if you want to do it with Pycharm IDE, things are getting complicated, because there is a bug when running
unittest on Pycharm and is somehow related to `utf-8`. For more details, please refer to 
[this issue on JetBrains site](https://intellij-support.jetbrains.com/hc/en-us/community/posts/360000019990-Unittest-Error-AttributeError-file-object-has-no-attribute-getvalue-)

To summarize this, you need to edit test run configuration and add an environment variable `JB_DISABLE_BUFFERING` 
(it is a flag and thus, has no value). Then, you should be able to run these tests normally.
