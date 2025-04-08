#include <fstream>
#include <iostream>
#include <random>
#include <string>


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

void save_string(std::string dir, std::string string_to_save) {
	std::ofstream out;
	out.open(dir);
	out << string_to_save << std::endl;
	out.close();
}

int main()
{
	std::string seq = generate_128_bit_sequence();
	save_string("cpp_sequence.txt", seq);
	std::cout << seq;
}

