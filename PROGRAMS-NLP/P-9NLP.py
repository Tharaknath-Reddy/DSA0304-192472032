"""
EXPERIMENT 9: Rule-Based POS Tagging System using Regular Expressions
Student: Gadwal Mohammad Muzammil | Reg No: 192424279
"""
import os, re

RULES = [
    (r'^-?\d+(?:\.\d+)?$', 'CD'),
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*s$', 'NNS'),
    (r'.*ly$', 'RB'),
    (r'^[A-Z][a-z]+$', 'NNP'),
    (r'^(the|a|an|this|that)$', 'DT'),
    (r'.*', 'NN')
]

def tag_word(word):
    for pattern, tag in RULES:
        if re.match(pattern, word, re.IGNORECASE if tag not in ('NNP',) else 0):
            return tag
    return 'NN'

def main():
    sentence = "Muzammil registered 192424279 students for running workshops"
    words = sentence.split()
    
    print("[INPUT SENTENCE]")
    print(f"\"{sentence}\"")
    print("-" * 60)
    print("[OUTPUT]")
    
    results = []
    print(f"{'Word':<15} | {'Regex Tag'}")
    print("-" * 30)
    for w in words:
        tag = tag_word(w)
        print(f"{w:<15} | {tag}")
        results.append(f"{w:<15} : {tag}")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp09_output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
