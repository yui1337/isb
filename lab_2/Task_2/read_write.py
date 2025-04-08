def get_text(dir: str) -> str:
    """
    Opens text file from given directory
    :param dir: Directory (Direct path to the .txt file)
    :return: String with file's content
    """
    try:
        with open(dir, mode='r', encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError as e:
        print(f"File does not exist or you entered wrong path: {e}")