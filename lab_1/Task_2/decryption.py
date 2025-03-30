from collections import Counter


def freq_analysis(text: str) -> dict[str, float]:
    """
    Creates relative frequency table for given text
    :param text: The text, which to create frequency table
    :return: Frequency table in form of a dict
    """
    cnt = Counter(text)
    freqs = {letter: count / len(text) for letter, count in cnt.items()}
    return dict(sorted(freqs.items(), key=lambda item: item[1], reverse=True))


def create_key(encrypted_text: str, ru_freqs: dict[str, float]) -> dict[str, str]:
    """
    Creates decryption key, based on a frequency analysis method
    :param encrypted_text: Text to decrypt
    :param ru_freqs: Frequency table for russian language
    :return: Decryption key in form of a dict
    """
    cur_text_freq = freq_analysis(encrypted_text)
    key = dict()
    for (letter_text, _), (letter_key, _) in zip(cur_text_freq.items(), ru_freqs.items()):
        key[letter_text] = letter_key
    return key


def decrypt(encrypted_text: str, key: dict[str, float]) -> str:
    """
    Decrypts text with given key
    :param encrypted_text: Text to decrypt
    :param key: key in form of a dict
    :return: Decrypted text
    """
    decrypted_text = ""
    for letter in encrypted_text:
        if letter in key:
            decrypted_text += key[letter]
        else:
            decrypted_text += letter
    return decrypted_text
