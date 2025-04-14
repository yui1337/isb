#include <fstream>
#include <iostream>
#include <random>
#include <string>


/**
 * @brief Generates a random 128-bit sequence represented as a binary string.
 *
 * The function uses a Mersenne Twister pseudo-random number generator (std::mt19937)
 * with a hardware-based seed from std::random_device. Produces a string of 128 '0' and '1' characters.
 *
 * @return std::string - 128-character string consisting of '0's and '1's
 */
std::string generate_128_bit_sequence() {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<size_t> number(0, 1);

    std::string result;
    for (size_t i = 0; i < 128; ++i) {
        result += std::to_string(number(gen));
    }
    return result;
}

/**
 * @brief Saves a string to a specified file path.
 *
 * @param dir std::string - Path where the file will be created/overwritten
 * @param string_to_save std::string - Content to write to the file
 * @throws std::ios_base::failure If file operations fail (exceptions enabled on output stream)
 */
void save_string(std::string dir, std::string string_to_save) {
    std::ofstream out;
    out.open(dir);
    out << string_to_save << std::endl;
    out.close();
}

/**
 * @brief Main program that generates a 128-bit sequence and saves it to a file
 *
 * Generates a binary sequence using generate_128_bit_sequence(), saves it to "cpp_sequence.txt",
 * and prints the sequence to standard output.
 */
int main() {
    std::string seq = generate_128_bit_sequence();
    save_string("cpp_sequence.txt", seq);
    std::cout << seq;
}