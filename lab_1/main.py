from lab_1.Task_2.decryption import *
from read_write import *
from Task_1.encryption import *

def main():
    task1_settings = read_json("settings.json").get("task_1") #Task 1
    task1_text = get_text(task1_settings["plain_text"])
    task1_key = read_json(task1_settings["key"])

    encrypted_text = encrypt_text(task1_text, task1_key)
    save_text(task1_settings["encrypted_text"], encrypted_text)

    #Task 2 Work in progress
    task2_settings = read_json("settings.json").get("task_2")
    task2_coded_text = get_text(task2_settings["encrypted_text"])
    freq_analysis(task2_coded_text)
    decrypted_text = decrypt(task2_coded_text, read_json(task2_settings["key"]))
    save_text(task2_settings["decrypted_text"], decrypted_text)


if __name__ == "__main__":
    main()