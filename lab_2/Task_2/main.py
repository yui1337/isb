from read_write import *
from tests import *


def main() -> None:
    settings = read_json("settings.json")
    cpp_seq = get_text(settings["cpp_sequence"])
    java_seq = get_text(settings["java_sequence"])
    p_const = settings["p_constants"]

    cpp_stats = {
        "frequency bit test": frequency_bit_test(cpp_seq),
        "identical bit sequence": identical_bit_sequence(cpp_seq),
        "longest run of ones": longest_run_of_ones(cpp_seq, p_const)
    }
    java_stats = {
        "frequency bit test": frequency_bit_test(java_seq),
        "identical bit sequence": identical_bit_sequence(java_seq),
        "longest run of ones": longest_run_of_ones(java_seq, p_const)
    }

    result = {"C++": cpp_stats, "Java": java_stats}
    save_json("result.json", result)


if __name__ == "__main__":
    main()
