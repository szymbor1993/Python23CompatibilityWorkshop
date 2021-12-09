import sys


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


def _calculate_word_int_avg_length(words_list):
    length_sum = 0
    for i in xrange(len(words_list)):
        length_sum += len(words_list[i])
    return length_sum / len(words_list)


def _snip_words(words):
    words_list = map(lambda single_word: single_word.lower(), words.split())
    avg_length = _calculate_word_int_avg_length(words_list)
    for index, word in enumerate(words_list):
        if len(word) >= avg_length:
            words_list[index] = word[::-1]
    return ' '.join(words_list)


def main(owner_words):
    """Non-interactive version of the program
    :param owner_words: Dictionary with structure: <owner name>: <words space-separated>
    :type owner_words: dict
    :return the dictionary with transformed words wrapped in WordContainer object
    """
    reload(sys)
    sys.setdefaultencoding('utf8')

    for owner, words in owner_words.iteritems():
        owner_words[owner] = WordContainer(_snip_words(words))

    return owner_words


def main_interactive():
    """Main function of the program

    Program asks user for number of entries. Then, each entry consists of owner's name and some words, space-separated.
    User should type them consecutively.
    After that, program transforms some words (reverses them) and user can access the data by providing owner's name.
    If user wants to exit the program, just type 'exit'.
    """
    owner_words = {}

    entries = input("Enter number of entries: ")
    if entries <= 0 or entries > 100:
        print "Invalid number of entries (1-100)"
        exit(1)

    for i in xrange(entries):
        owner = raw_input("Enter owner name: ")
        words = raw_input("Enter his words separated with space: ")
        owner_words[owner] = WordContainer(words)

    for owner, _ in owner_words.iteritems():
        print "Owner %s, his words: %s" % (owner, owner_words[owner].words)

    print "\nLoading entries finished. Now processing them..."
    for owner, word_container in owner_words.iteritems():
        owner_words[owner].words = _snip_words(word_container.words)

    print "Processing ended. Now you can access them."
    choice = raw_input("Provide name, or type 'exit' to exit program: ")
    while choice != "exit":
        if choice not in owner_words.keys():
            choice = raw_input("There is no such owner. Try again: ")
            continue

        print "Owner %s, his words: %s" % (choice, owner_words[choice].words)
        choice = raw_input("What now? ")

    print "Exiting"
    exit(0)


if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')

    main_interactive()
