"""
EXPERIMENT 10: Transformation-Based POS Tagging (Brill Algorithm)
Student: Gadwal Mohammad Muzammil | Reg No: 192424279
"""
import os

def apply_transformation_rules(words, baseline_tags):
    tags = list(baseline_tags)
    for i in range(1, len(words)):
        if tags[i-1] == 'DT' and tags[i] == 'VB':
            tags[i] = 'NN'
    for i in range(1, len(words)):
        if words[i-1].lower() == 'to' and tags[i] == 'NN':
            tags[i] = 'VB'
    return tags

def main():
    sentence = "They want to study in the run today"
    words = sentence.split()
    baseline_tags = ["PRP", "VBP", "TO", "NN", "IN", "DT", "VB", "NN"]
    
    print("[INPUT SENTENCE & BASELINE TAGS]")
    print("Words:   ", words)
    print("Baseline:", baseline_tags)
    print("-" * 60)
    print("[OUTPUT]")
    
    final_tags = apply_transformation_rules(words, baseline_tags)
    
    print(f"{'Word':<10} | {'Baseline Tag':<15} | {'Transformed Tag'}")
    print("-" * 45)
    results = []
    for w, b_tag, f_tag in zip(words, baseline_tags, final_tags):
        print(f"{w:<10} | {b_tag:<15} | {f_tag}")
        results.append(f"{w:<10} | {b_tag:<10} -> {f_tag}")

    os.makedirs("outputs", exist_ok=True)
    with open("outputs/exp10_output.txt", "w") as f:
        f.write("\n".join(results))

if __name__ == "__main__":
    main()
