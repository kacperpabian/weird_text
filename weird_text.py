import re
from copy import copy
from random import shuffle


def encode(text):
    """Function to encode text"""
    # spliting sentence to list of words
    listed_words = text.split()
    encoded_sentence_word_list = []
    unshuffled_sorted_words = []
    for word in listed_words:
        # excluding words with 3 or less letters
        if len(word) <= 3:
            encoded_sentence_word_list.append(word)
        else:
            listed_chars = list(word)
            prefix = ""
            curr_char = ""
            counter_prefix = 0
            # this loop handles prefix for out word, starts from left, ends when finds first numeric char
            while not re.match("^[a-zA-Z0-9_]*$", curr_char) or curr_char == "":
                curr_char = listed_chars[counter_prefix]
                prefix += curr_char
                counter_prefix += 1
            suffix = ""
            curr_char = ""
            counter_suffix = len(listed_chars) - 1
            # this loop handles suffix for out word, starts from right, ends when finds first numeric char
            while not re.match("^[a-zA-Z0-9_]*$", curr_char) or curr_char == "":
                curr_char = listed_chars[counter_suffix]
                suffix += curr_char
                counter_suffix -= 1
            # reverse suffix
            suffix = suffix[::-1]
            # taking the middle of word to shuffle it. Using prefix and suffix indexes
            word_middle = [let for i, let in enumerate(listed_chars) if counter_prefix <= i <= counter_suffix]
            shuffled_word = copy(word_middle)
            # handles saving our key words
            if not ''.join(word_middle) == len(word_middle) * word_middle[0]:
                # pre and suf are suffixes without special signs
                pre = ''.join(char for char in prefix if char.isalnum())
                suf = ''.join(char for char in suffix if char.isalnum())
                # saving unshuffled word before shuffle
                unshuffled_sorted_words.append(pre + "".join(word_middle) + suf)
                # distinct words wanted, no need for copies
                unshuffled_sorted_words = set(unshuffled_sorted_words)
                unshuffled_sorted_words = list(unshuffled_sorted_words)
            # shuffle middle word while different and all letters not the same
            while shuffled_word == word_middle and not ''.join(word_middle) == len(word_middle) * word_middle[0]:
                shuffle(shuffled_word)
            # put encoded word together
            encoded_word_temp = prefix + ''.join(shuffled_word) + suffix
            encoded_sentence_word_list.append(encoded_word_temp)
    # sorting string list and ignoring case
    unshuffled_sorted_words = sorted(unshuffled_sorted_words, key=lambda s: s.lower())
    return " ".join(encoded_sentence_word_list), unshuffled_sorted_words


def decode(text, sorted_words_list):
    """Function to decode text"""
    listed_words = text.split()
    decoded_sentence_word_list = []
    # get middle from key words
    middle_sorted_words_list = [word[1:-1] for word in sorted_words_list]
    for word in listed_words:
        # half the same as encode
        if len(word) <= 3:
            decoded_sentence_word_list.append(word)
        else:
            listed_chars = list(word)
            prefix = ""
            curr_char = ""
            counter_prefix = 0
            while not re.match("^[a-zA-Z0-9_]*$", curr_char) or curr_char == "":
                curr_char = listed_chars[counter_prefix]
                prefix += curr_char
                counter_prefix += 1
            suffix = ""
            curr_char = ""
            counter_suffix = len(listed_chars) - 1
            while not re.match("^[a-zA-Z0-9_]*$", curr_char) or curr_char == "":
                curr_char = listed_chars[counter_suffix]
                suffix += curr_char
                counter_suffix -= 1
            suffix = suffix[::-1]
            word_middle = [let for i, let in enumerate(listed_chars) if counter_prefix <= i <= counter_suffix]
            word_found = False
            # crating list with only key words the same size as encoded word
            same_size_list = [s for s in middle_sorted_words_list if len(s) == len(word_middle)]
            # this variable will save our decoded word
            wanted_word = ""
            # do until word not with same letters and word not found yet
            while not ''.join(word_middle) == len(word_middle) * word_middle[0] and not word_found:
                for s in same_size_list:
                    count_good = 0
                    wanted_word = ""
                    # for every char in middle word key
                    for c in s:
                        # for every char in encoded word
                        for x in word_middle:
                            if x == c:
                                count_good += 1
                                # creating word if chars the same
                                wanted_word += c
                                # no need to iterate more if found
                                break
                    # if word length matches, no need to iterate more - word found
                    if count_good == len(word_middle):
                        word_found = True
                        break
            # put decoded word together
            decoded_word_temp = prefix + wanted_word + suffix
            decoded_sentence_word_list.append(decoded_word_temp)

    return " ".join(decoded_sentence_word_list)


sentence = 'This is a long looong test sentence,\n' \
           'with some big (biiiiig) words!'

sentence2 = 'A black hole is a region of spacetime exhibiting such strong gravitational effects ' \
            'that nothing—not even particles and electromagnetic radiation such as light—can escape ' \
            'from inside it. The theory of general relativity predicts that a sufficiently compact ' \
            'mass can deform spacetime to form a black hole. The boundary of the region from which ' \
            'no escape is possible is called the event horizon. Although the event horizon has an enormous ' \
            'effect on the fate and circumstances of an object crossing it, no locally detectable features ' \
            'appear to be observed. In many ways a black hole acts like an ideal black body, as it reflects ' \
            'no light. Moreover, quantum field theory in curved spacetime predicts that event horizons ' \
            'emit Hawking radiation, with the same spectrum as a black body of a temperature inversely proportional ' \
            'to its mass. This temperature is on the order of billionths of a kelvin for ' \
            'black holes of stellar mass, making it essentially impossible to observe.'

encoded_sentence, sorted_words_list = encode(sentence2)
print(encoded_sentence)
print(" ".join(sorted_words_list))
print(decode(encoded_sentence, sorted_words_list))
