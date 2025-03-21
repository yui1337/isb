from read_write import *
from Task_1.encryption import *

def main():
    task1_settings = read_json("settings.json").get("task_1") #Task 1
    task1_text = get_text(task1_settings["plain_text"])
    task1_key = read_json(task1_settings["key"])

    encrypted_text = encrypt_text(task1_text, task1_key)
    save_text(task1_settings["encrypted_text"], encrypted_text)

    #Task 2 Work in progress


if __name__ == "__main__":
    main()