from math import sqrt
from scipy import erfc, gammainc


def frequency_bit_test(sequence: str) -> float:
    summ = (sequence.count("1") - sequence.count("0")) / sqrt(len(sequence))
    pvalue = erfc(abs(summ) / sqrt(2))
    return pvalue

def identical_bit_sequence(sequence: str) -> float:
    dzeta = (sequence.count("1") / len(sequence))
    if abs(dzeta) >= (2 / sqrt(len(sequence))):
        return 0
    v_n = 0
    for k in range(len(sequence) - 1):
        if sequence[k] != sequence[k+1]:
            v_n += 1
    pvalue = erfc(abs(v_n - 2 * len(sequence) * dzeta * (1 - dzeta)) /
                  2 * sqrt(2 * len(sequence)) * dzeta * (1-dzeta) )
    return pvalue

def longest_run_of_ones(sequence: str) -> float:
    blocks = [sequence[i:i + 8] for i in range(0, len(sequence), 8)]
    v = [0, 0, 0, 0]
    for block in blocks:
        max_len = max(map(len, block.split("0"))) if block else 0
        print(f"Current block: {block} Max_len: {max_len}")
        match max_len:
            case max_len if max_len <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[3] += 1
            case max_len if max_len >= 4:
                v[4] += 1
    p = [0.2148, 0.3672, 0.2305, 0.1875]
    chi_square = sum(((v[i] - 16 * p[i]) ** 2) / (16 * p[i]) for i in range(0, 4))
    pvalue = gammainc(3 / 2, chi_square / 2 )
    return pvalue