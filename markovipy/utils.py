#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import codecs


def fix_caps(word):
    """Used to compare words, irrespective of their capitalisation

    :param word: the word to be fixed
    :type word: <str>
    :return: <str>
    """
    articles = ['a', 'an', 'of', 'the', 'is']
    return ' '.join
        (
        [
            word.capitalize() if  paragraph.index(word) == 0 else word.lower()
            for word in paragraph.split(" ")
        ]
        )



def get_word_list(file):
    """Used to get the words inside the corpus file and generate a list of
    words by parsing it

    Something like = ["once", "upon", "a", ...]

    Check the regex on https://regex101.com/ with any file inside the
    corpus/ dir

    \w matches any word character (equal to [a-zA-Z0-9_])
    ' matches the character ' literally (case sensitive)
    .,!?; matches a single character in the list .,!?; (case sensitive)

    :param file: the file being passed to create the list of words
    :type file: <str>
    :return: <list>
    """
    try:
        # fixes UnicodeDecodeError while reading files instead of using the
        # normal open()
        with codecs.open(file, 'r', encoding='utf-8') as f:
            words_list = \
                [fix_caps(w) for w in re.findall(r"[\w']+|[.,!?;]", f.read())]
        return words_list
    except OSError:
        return "Did you pass a valid file name/path?"
