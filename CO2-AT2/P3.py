# Program 3: Morphology-Based Normalization

words = ["govern", "government", "governance"]

print("=" * 110)
print("{:<15}{:<12}{:<12}{:<20}{:<18}{:<15}".format(
    "Original", "Root", "Affix",
    "Derivation Level", "Normalized", "Representation"))
print("=" * 110)

for word in words:

    if word == "govern":
        root = "govern"
        affix = "-"
        level = "Level 0"
        normalized = "govern"

    elif word.endswith("ment"):
        root = "govern"
        affix = "-ment"
        level = "Level 1"
        normalized = "govern"

    elif word.endswith("ance"):
        root = "govern"
        affix = "-ance"
        level = "Level 1"
        normalized = "govern"

    print("{:<15}{:<12}{:<12}{:<20}{:<18}{:<15}".format(
        word, root, affix,
        level, normalized,
        root + affix))