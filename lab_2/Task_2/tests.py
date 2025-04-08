from math import sqrt, erfc
from scipy.special import gammainc


def frequency_bit_test(sequence: str) -> float:
    """
    Tests if the sequence is randomly generated
    using frequency bit testing
    Reference: NIST SP 800-22, Section 2.1.
    :param sequence: Sequence to test
    :return: PValue
    """
    summ = (sequence.count("1") - sequence.count("0")) / sqrt(len(sequence))
    p_value = erfc(abs(summ) / sqrt(2))
    return p_value

def identical_bit_sequence(sequence: str) -> float:
    """
    Tests if the sequence is randomly generated
    using Runs Test, where a run is an uninterrupted sequence
    of identical bits
    Reference: NIST SP 800-22, Section 2.3.
    :param sequence: Sequence to test
    :return: PValue
    """
    dzeta = (sequence.count("1") / len(sequence))
    if abs(dzeta - 1 / 2) >= (2 / sqrt(len(sequence))):
        return 0
    v_n = 0
    for k in range(0, len(sequence) - 1):
        if sequence[k] != sequence[k + 1]:
            v_n += 1
    p_value = erfc(abs(v_n - 2 * len(sequence) * dzeta * (1 - dzeta)) /
                   (2 * sqrt(2 * len(sequence)) * dzeta * (1 - dzeta)))
    return p_value

def longest_run_of_ones(sequence: str) -> float:
    """
    Tests if the sequence is randomly generated
    using Test for the Longest Run of Ones in a Block
    (block size is 8, length of sequence is 128 bit)
    Reference: NIST SP 800-22, Section 2.4.
    :param sequence: Sequence to test
    :return: PValue
    """
    blocks = [sequence[i:i + 8] for i in range(0, len(sequence), 8)]
    v = [0, 0, 0, 0]
    for block in blocks:
        max_len = max(map(len, block.split("0"))) if block else 0
        match max_len:
            case max_len if max_len <= 1:
                v[0] += 1
            case 2:
                v[1] += 1
            case 3:
                v[2] += 1
            case max_len if max_len >= 4:
                v[3] += 1
    p = [0.2148, 0.3672, 0.2305, 0.1875]
    chi_square = sum(((v[i] - 16 * p[i]) ** 2) / (16 * p[i]) for i in range(0, 4))
    p_value = gammainc(3 / 2, chi_square / 2 )
    return p_value

