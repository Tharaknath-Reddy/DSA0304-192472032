"""
EXPERIMENT 7: Part-of-Speech (POS) Tagging using NLTK
Student: Gadwal Mohammad Muzammil | Reg No: 192424279
"""
import os
import nltk

def main():
    sentence = "Muzammil studies Natural Language Processing at Saveetha University."
    
    print("[INPUT SENTENCE]")
    print(f"\"{sentence}\"")
    print("-" * 60)
    print("[OUTPUT]")
    
    tokens = sentence.replace('.', '').split()
    pos_tags = nltk.pos_tag(tokens)
    
    results = []
    print(f"{'Token':<15} | {'POS Tag'}")
    print("-" * 30)
    for word, tag in pos_tags:
        print(f"{word:<15} | {tag}")
        results.append(f"{word:<15} : {tag}")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp07_output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
