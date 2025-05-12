import argparse

from crypto.hybrid import Hybrid
from fileshandler import FilesHandler


def get_arg() -> str:
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", type=str, help=""
                                                       "Changes mode of script:"
                                                       "generate - generates keys"
                                                       "encrypt - encrypts ur txt"
                                                       "decrypt - decrypts ur txt")
    arguments = parser.parse_args()
    return arguments.mode

def main() -> None:
    settings = FilesHandler.get_json("settings.json")
    print(settings["public_key"])
    mode = get_arg()
    hybrid = Hybrid()
    match mode:
        case "generate":
            hybrid.generate_keys(settings["public_key"],
                                 settings["private_key"],
                                 settings["symmetric_key"])
        case "encrypt":
            hybrid.encrypt_data(settings["plain_text"],
                                settings["private_key"],
                                settings["symmetric_key"],
                                settings["encrypted_text"])
        case "decrypt":
            hybrid.decrypt_data(settings["encrypted_text"],
                                settings["private_key"],
                                settings["symmetric_key"],
                                settings["decrypted_text"])


if __name__ == "__main__":
    main()


