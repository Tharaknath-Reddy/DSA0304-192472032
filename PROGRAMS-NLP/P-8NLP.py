"""
EXPERIMENT 8: Stochastic Part-of-Speech Tagging Algorithm (Probabilistic Model)
Student: Gadwal Mohammad Muzammil | Reg No: 192424279
"""
import os
from collections import defaultdict, Counter

def train_stochastic_tagger(corpus):
    word_tag_counts = defaultdict(Counter)
    for sentence in corpus:
        for word, tag in sentence:
            word_tag_counts[word.lower()][tag] += 1
    return word_tag_counts

def tag_sentence(model, words):
    tagged = []
    for w in words:
        w_lower = w.lower()
        if w_lower in model:
            best_tag = model[w_lower].most_common(1)[0][0]
        else:
            best_tag = 'NN'
        tagged.append((w, best_tag))
    return tagged

def main():
    corpus = [
        [("The", "DT"), ("cat", "NN"), ("runs", "VB"), ("fast", "RB")],
        [("A", "DT"), ("dog", "NN"), ("barks", "VB")],
        [("Muzammil", "NNP"), ("reads", "VB"), ("a", "DT"), ("book", "NN")]
    ]
    
    test_sentence = ["The", "cat", "reads", "a", "book"]
    
    print("[INPUT TEST SENTENCE]")
    print(test_sentence)
    print("-" * 60)
    print("[OUTPUT]")
    
    model = train_stochastic_tagger(corpus)
    tagged_result = tag_sentence(model, test_sentence)
    
    print("Stochastic Tagging Result:")
    results = []
    for word, tag in tagged_result:
        print(f"  {word:<10} -> {tag}")
        results.append(f"{word} -> {tag}")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp08_output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
