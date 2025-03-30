from dataclasses import replace


def encrypt_text(plain_text: str, key: dict[str,str]) -> str:
    """
    Encrypts text with given key
    :param plain_text: The text to encrypt
    :param key: Key(dictionary)
    :return: Encrypted text
    """
    result = ""
    key = {k.lower(): v for k, v in key.items()}
    for letter in plain_text:
        replacement = key.get(letter.lower())
        if replacement is not None:
            result += replacement
        else:
            result += letter
    return result
