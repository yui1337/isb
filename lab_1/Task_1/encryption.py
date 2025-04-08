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
        match replacement:
            case None:
                result += letter
            case _:
                result += replacement
    return result


def decrypt_atbash(encrypted_text: str, alphabet: str) -> str:
    """
    Decrypts text that is encrypted with Atbash method
    :param encrypted_text: Encrypted text to decrypt
    :param alphabet: Alphabet of language, that is text encrypted in
    :return: Decrypted text
    """
    decrypted_text = ""
    alphabet = alphabet.casefold()
    for letter in encrypted_text:
        letter = letter.casefold()
        match letter in alphabet:
            case True:
                letter_index = alphabet.index(letter)
                decrypted_text += alphabet[-letter_index - 1]
            case False:
                decrypted_text += letter
    return decrypted_text




