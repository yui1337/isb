from math import sqrt
from scipy import erfc


def frequency_bit_test(sequence: str)-> float:
    summ = (sequence.count("1") - sequence.count("0")) / sqrt(len(sequence))
    pvalue = erfc(abs(summ) / sqrt(2))
    return pvalue
