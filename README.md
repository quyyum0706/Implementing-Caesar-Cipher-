
---

# **🔐 Caesar Cipher Program**
A Python implementation of the **Caesar Cipher**, one of the earliest encryption techniques that shifts characters forward or backward by a fixed key value.

## **📜 Overview**
This program allows users to:
- Encrypt and decrypt messages using a shift key.
- Preserve **non-alphabet characters** (spaces, punctuation, numbers).
- Accept **valid key values (1-25)** for secure encryption.

## **🧠 Algorithm Explanation**
The Caesar Cipher works by shifting letters in the alphabet by a specified **key value**. For example:
- If the **shift key = 3**, then:
  - `"A"` → `"D"`
  - `"B"` → `"E"`
  - `"C"` → `"F"`
- During **decryption**, the shift moves in the **opposite direction** to restore the original text.

## **🛠 Code Breakdown**
### **1️⃣ Letter Mapping**
The program uses:
```python
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)
```
to define the alphabet and determine its length for modular arithmetic.

### **2️⃣ Encryption Process**
Each letter is shifted forward using:
```python
new_index = (index + shift_key) % num_letters
```
This ensures wrap-around for letters near the end (e.g., `"Z"` → `"C"` with a shift of `3`).

### **3️⃣ Decryption Process**
To reverse encryption, the program shifts backward:
```python
new_index = (index - shift_key) % num_letters
```

### **4️⃣ Handling Uppercase and Non-Alphabet Characters**
- **Uppercase letters** retain their original case after encryption.
- **Spaces, punctuation, and numbers** remain unchanged.

## **💻 Usage Instructions**
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/caesar-cipher.git
cd caesar-cipher
```

### **2️⃣ Run the Program**
```bash
python caesar_cipher.py
```

### **3️⃣ Follow On-Screen Prompts**
- `"e"` → Encrypt a message.
- `"d"` → Decrypt a message.
- `"q"` → Quit the program.

## **📌 Example Usage**
```bash
Enter the key (1 through 25): 4
Enter the text to encrypt: Hello World!
CIPHERTEXT: Lipps Asvph!
```
```bash
Enter the key (1 through 25): 4
Enter the text to decrypt: Lipps Asvph!
PLAINTEXT: Hello World!
```

## **🚀 Customization & Future Enhancements**
- ✅ **Adjust the key range** (e.g., allow shifts beyond `25`).
- ✅ **Implement frequency analysis** to decrypt unknown messages.
- ✅ **Add a GUI interface** with **Tkinter** for better usability.
- ✅ **Enable multi-language encryption** beyond `A-Z` characters.

## **📄 License**
This project is open-source and available for educational use.

---



