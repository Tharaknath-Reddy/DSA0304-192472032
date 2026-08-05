"""
EXPERIMENT 6: Basic N-gram Model for Text Generation (Bigram Model)
Student: Gadwal Mohammad Muzammil | Reg No: 192424279
"""
import os
from collections import defaultdict, Counter

def build_bigram_model(text):
    words = text.lower().split()
    model = defaultdict(Counter)
    for i in range(len(words) - 1):
        model[words[i]][words[i+1]] += 1
    return model

def generate_text(model, start_word, length=8):
    current = start_word.lower()
    result = [current.capitalize()]
    for _ in range(length - 1):
        if current in model:
            next_word = model[current].most_common(1)[0][0]
            result.append(next_word)
            current = next_word
        else:
            break
    return " ".join(result)

def main():
    corpus = "natural language processing is fun natural language processing allows computers to learn natural language text processing"
    seed = "natural"
    
    print("[INPUT CORPUS]")
    print(f"Corpus: \"{corpus}\"")
    print(f"Seed Word: \"{seed}\"")
    print("-" * 60)
    print("[OUTPUT]")
    
    model = build_bigram_model(corpus)
    generated = generate_text(model, seed, length=10)
    
    print(f"Generated Bigram Text: \"{generated}\"")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp06_output.txt", "w") as f:
        f.write(f"Corpus: {corpus}\nSeed: {seed}\nGenerated Text: {generated}")

if __name__ == "__main__":
    main()
