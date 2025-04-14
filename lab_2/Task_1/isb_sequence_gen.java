import java.security.SecureRandom;


/**
 * Class for generating cryptographically secure 128-bit sequences
 * and outputting them as binary-formatted strings.
 */
public class Main {

    /**
     * Main method that generates and prints a 128-bit binary sequence
     *
     * @param args Command-line arguments (not used in this implementation)
     *
     * @implSpec
     * Uses SecureRandom for cryptographically strong random number generation.
     * Generates 128 bits represented as '0'/'1' characters in a StringBuilder.
     * Outputs the resulting binary string to standard output.
     */
    public static void main(String[] args) {
        final SecureRandom random = new SecureRandom();
        final StringBuilder binaryString = new StringBuilder(128);

        // Generate 128 cryptographically secure random bits
        for (int i = 0; i < 128; i++) {
            final boolean bit = random.nextBoolean();
            binaryString.append(bit ? '1' : '0');
        }

        System.out.println(binaryString.toString());
    }
}