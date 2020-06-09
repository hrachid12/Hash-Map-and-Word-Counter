# word_count.py
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. The word
# counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap, hash_function_2

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")


def sort_words(key_val_list):
    """Sorts the list of words from top words from greatest to least

    Args:
        key_val_list (list): A list of touples from top_words. The touple is in the form of (key, value)
    """
    for index in range(1, len(key_val_list)):
        val = key_val_list[index]
        pos = index
        while pos > 0 and key_val_list[pos-1][1] < val[1]:
            key_val_list[pos] = key_val_list[pos-1]
            pos -= 1
        key_val_list[pos] = val


def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    result = []

    ht = HashMap(2500, hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)
            for w in words:
                lw = w.lower()

                # If the word is not in the hash map, add it with a value of 1
                if not ht.contains_key(lw):
                    ht.put(lw, 1)
                else:
                    # Otherwise, update the value by increasing it by 1
                    ht.put(lw, ht.get(lw) + 1)

    for bucket in ht._buckets:
        cur = bucket.head
        while cur is not None:
            result.append((cur.key, cur.value))
            cur = cur.next

    print(ht.table_load())
    print(ht.empty_buckets())

    sort_words(result)
    return result[:number]

