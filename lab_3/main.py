from lab_3.crypto.asymmetric import Asymmetric
from lab_3.crypto.symmetric import Symmetric

symmetric = Symmetric()
symmetric.generate_key(128)
symmetric.serialization_symmetric_key("crypto/keys/symmetric_key.txt")
symmetric.encrypt_text("text_files/plain_text.txt", "text_files/cipher_text.txt")
symmetric.decrypt_text("crypto/keys/symmetric_key.txt", "text_files/cipher_text.txt",
                       "text_files/decipher_text.txt")

asymmetric = Asymmetric()
asymmetric.generate_asymmetric_keys()
asymmetric.serialization_public_key("crypto/keys/public_key.txt")
asymmetric.serialization_private_key("crypto/keys/private_key.txt")
asymmetric.encrypt_symmetric_key("crypto/keys/public_key.txt", "crypto/keys/symmetric_key.txt",
                                 "crypto/keys/encrypted_symmetric_key.txt")

