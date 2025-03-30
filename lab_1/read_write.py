import json

def read_json(dir: str) -> dict:
    """
    Reads JSON file from given directory
    :param dir: Path to the JSON file
    :return: JSON file as a dictionary
    """
    try:
        with open(dir, mode='r', encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"File does not exist or you entered wrong path: {e}")
    except PermissionError as e:
        print(f"Can't access this file: {e}")
    except Exception as e:
        print(f"Something weird happened:{e}")


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


def save_text(dir: str, text: str) -> None:
    """
    Saves string to .txt file
    :param dir: Path to save .txt file
    :param text: String to save
    :return: None
    """

    try:
        with open(dir, mode='w', encoding="utf-8") as file:
            file.write(text)
    except Exception as e:
        print(f"Something went wrong: {e}")


def save_json(dir: str, data: dict) -> None:
    """
    Saves dictionary as json file
    :param dir: Path to save .json file
    :param data: Dictionary to save
    :return: None
    """
    try:
        with open(dir, mode='w', encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)
    except Exception as e:
        print(f"Something went wrong: {e}")



