import json

def main():
    with open('phonetic_alphabet.json', 'r', encoding='utf-8') as f:
        phonetic_alphabet = json.load(f)
    
    word = input("Word? ").strip()
    
    spelled_list = []
    for char in word.lower():
        if char in phonetic_alphabet:
            spelled_list.append(phonetic_alphabet[char])
        else:
            spelled_list.append(char)
    
    print("-".join(spelled_list))

if __name__ == "__main__":
    main()
