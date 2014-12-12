import string
import random


def text_prep(word):
    """Prepare selected text by removing irrelevant parts"""
    word = word.strip(string.punctuation + string.whitespace)
    word = word.lower()


def get_words(sher_text):
    """Open the file and add the prepped words to a list"""
    words = open(sher_text, 'r')
    for items in range(61):
        words.readline()
    text = words.read()
    all_words = []
    for word in text.split():
        text_prep(word)
        all_words.append(word)
    return all_words


def create_trigram(all_words):
    """Using the list made before, create trigrams by adding to dictionary"""
    trigram = {}
    for i in range(len(all_words) - 2):
        dict_key = (all_words[i], all_words[i + 1])
        if dict_key not in trigram:
            dict_value = [all_words[i + 2]]
            trigram[dict_key] = dict_value
        else:
            trigram[dict_key].append(all_words[i + 2])
    return trigram


def new_text():
    """Create trigrams from the text provided earlier"""
    tri_text = ""
    for dict_key, dict_value in trigram.items():
        dict_value = dict_value[random.randint(0, len(dict_value) - 1)]
        tri_text += " " + dict_value
    return tri_text

if __name__ == '__main__':
    all_words = get_words('sherlock.txt')
    trigram = create_trigram(all_words)
    tri_text = new_text()
    print tri_text
