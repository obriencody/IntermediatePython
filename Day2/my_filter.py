#!/usr/bin/env python3
"""
Author : t24 <me@wsu.com>
Date   : 8/10/2021
Purpose:
"""
from functools import reduce
from pprint import pp
import operator

def count_words(doc):
    """Count words in a document
    Produces a dictionary mapping words"""
    # normalize the string
    normalize_doc = ''.join(c.lower() if c.isalpha() else ' ' for c in doc)
    frequencies = {}
    for word in normalize_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_counts(d1, d2):
    """Combine words from two dictionaries"""
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d

# --------------------------------------------------
def main():
    """Make your noise here"""
    numbers = [2, 5, 8, -1, 90, -2, -33, 12]
    # Task: Create a list of all positive numbers
    # List Comprehension
    positives = [num for num in numbers if num >= 0]
    print(positives)
    # Generator
    positives = list((num for num in numbers if num >= 0))
    print(positives)
    # filter() and lamda
    # filter is also a lazy evaluation
    positives = list(filter(lambda x: x > 0, numbers))
    positives = filter(lambda x: x > 0, numbers)
    print(next(positives))
    positives = list(filter(lambda x: x > 0, numbers))
    negatives = filter(None, numbers)
    print(negatives)

    numbers = [-7, 2, 5, 8, -1, 90, -2, -33, 0, 12]
    # a + b = operator.add(a,b)
    accumulator = operator.add(numbers[0], numbers[1])
    for item in numbers[2:]:
        accumulator = operator.add(accumulator, item)
    print(accumulator)
    # Use reduce
    print(reduce(operator.add, numbers, 0))

    # Combine map() and reduce()
    document = "It was the best of times, it was the worst of times"
    print(count_words(document))
    documents = [
        'It was the best of times, it was the worst of times',
        'I went to the woods because I wished to live deliberately, to front only the essentials',
        'Friends, Romans, countrymen, lend me your ears; I come to bury trees for fruit',
        'I do not like green eggs and ham! I do not like them Sam I am.'
    ]

    counts = map(count_words, documents)
    total_counts = reduce(combine_counts, counts)
    pp(total_counts)



# --------------------------------------------------
if __name__ == '__main__':
    main()
