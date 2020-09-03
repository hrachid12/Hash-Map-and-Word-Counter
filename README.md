# Hash-Map-and-Word-Counter

Portfolio Project for CS261

The purpose of this project was to create a hash map that uses a hash table of buckets, each containing a linked list of hash links. Each hash link stores the key-value pair (string and integer in this case) and a pointer to the next link in the list. 

Word_count.py takes an input document, computes the number of times each word was used in the document, stores the words in a hash map, and returns the table load, the number of empty buckets in the hash map, top X words and associated counts.

## Usage

An example of how to use word_count.py to find the top 5 most used words in 'alice.txt' . It is required that both files are downloaded and in the same directory as 'example.py'.

```python
from word_count.py import top_words

top_words('alice.txt', 5)
```

