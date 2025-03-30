from collections import Counter

from ..read_write import *


def freq_analysis(text: str) -> dict[str, float]:
    cnt = Counter(text)
    length = len(text)
    freqs = {letter: count / len(text) for letter, count in cnt.items()}
    return dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))


def create_key(encrypted_text: str, ru_freqs: dict) -> dict:
    cur_text_freq = freq_analysis(encrypted_text)
    key = dict()
    for (letter_text, _), (letter_key, _) in zip(cur_text_freq.items(), ru_freqs.items()):
        key[letter_text] = letter_key
    save_json("key.json", key)
    return key

def decrypt(encrypted_text: str, key: dict) -> str:
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in key:
            decrypted_text += key[letter]
        else:
            decrypted_text += letter
    return decrypted_text



