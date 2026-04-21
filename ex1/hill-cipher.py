import numpy as np

def text_to_numbers(text):
    return [ord(c.upper()) - ord('A') for c in text if c.isalpha()]

def numbers_to_text(numbers):
    return "".join(chr(int(n) + ord('A')) for n in numbers)

def hill_cipher_encrypt(text, key_matrix):
    n = len(key_matrix)
    # Padding with 'X' if text length isn't a multiple of n
    while len(text) % n != 0:
        text += 'X'
    
    nums = text_to_numbers(text)
    result = []
    
    # Process in blocks of n
    for i in range(0, len(nums), n):
        block = np.array(nums[i:i+n])
        # Matrix multiplication: C = (K * P) mod 26
        transformed = np.dot(key_matrix, block) % 26
        result.extend(transformed)
        
    return numbers_to_text(result)

# Example Usage
# Key matrix must be invertible modulo 26
key = np.array([[6, 24, 1], 
                [13, 16, 10], 
                [20, 17, 15]])

message = "ACT"
encrypted = hill_cipher_encrypt(message, key)

print(f"Key Matrix:\n{key}")
print(f"Original Message: {message}")
print(f"Encrypted: {encrypted}")