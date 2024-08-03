import numpy as np
from phe import paillier

def encrypted_computation(data1, data2):
    public_key, private_key = paillier.generate_paillier_keypair()
    encrypted_data1 = [public_key.encrypt(x) for x in data1]
    encrypted_data2 = [public_key.encrypt(x) for x in data2]

    encrypted_sum = [x + y for x, y in zip(encrypted_data1, encrypted_data2)]
    decrypted_sum = [private_key.decrypt(x) for x in encrypted_sum]

    return decrypted_sum

if __name__ == "__main__":
    data1 = np.random.randint(0, 100, 10).tolist()
    data2 = np.random.randint(0, 100, 10).tolist()

    print("Data1:", data1)
    print("Data2:", data2)

    result = encrypted_computation(data1, data2)
    print("Decrypted Sum:", result)