import java.security.SecureRandom;

public class Main {
	public static void main(String[] args) {
		SecureRandom random = new SecureRandom();
        StringBuilder binaryString = new StringBuilder();

        for (int i = 0; i < 128; i++) {
            boolean bit = random.nextBoolean();
            binaryString.append(bit ? '1' : '0');
        }
        System.out.println(binaryString);
	}
}