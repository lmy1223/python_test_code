# !/usr/bin/python
#-*- coding: UTF-8 -*-

from __future__ import print_function
import sys
from collections import Counter


scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def get_word_list(file_name):
    word_list = []
    with open(file_name) as f:
        for line in f:
            word_list.append(line.strip('\n'))
    return word_list

def get_valid_words(word_list, rack):
    c = Counter(rack)
    return [ word for word in word_list if not (Counter(word) - c) ]

def lower_valid_words(words):
    return [ word.lower() for word in words ]

def get_scores(words):
    d = {}
    for word in words:
        d[word] = sum(scores[c] for c in word)
    return d

def main():
    if len(sys.argv) != 2:
        raise SystemExit('Usage: scrabble_change.py RACK')

    rack = sys.argv[1]

    word_list = get_word_list('sowpods.txt')
    valid_words = get_valid_words(word_list, rack.upper())

    valid_words = lower_valid_words(valid_words)

    d = get_scores(valid_words)
    for val, key in sorted(zip(d.values(), d.keys()), reverse=True):
        print(val, key)

if __name__ == '__main__':
    main()
