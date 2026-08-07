# Program 2: Morphological Parser

words = ["disagree", "agreement", "agreeable"]

print("=" * 120)
print("{:<15}{:<10}{:<12}{:<12}{:<15}{:<25}{:<15}".format(
    "Original", "Prefix", "Root", "Suffix",
    "Type", "Semantic Meaning", "Normalized"))
print("=" * 120)

for word in words:

    if word.startswith("dis"):
        prefix = "dis-"
        root = "agree"
        suffix = "-"
        ttype = "Derivational"
        meaning = "Opposite of agree"
        normalized = "agree"

    elif word.endswith("ment"):
        prefix = "-"
        root = "agree"
        suffix = "-ment"
        ttype = "Derivational"
        meaning = "State of agreeing"
        normalized = "agree"

    elif word.endswith("able"):
        prefix = "-"
        root = "agree"
        suffix = "-able"
        ttype = "Derivational"
        meaning = "Capable of agreeing"
        normalized = "agree"

    else:
        prefix = "-"
        root = word
        suffix = "-"
        ttype = "Base"
        meaning = "-"
        normalized = word

    print("{:<15}{:<10}{:<12}{:<12}{:<15}{:<25}{:<15}".format(
        word, prefix, root, suffix,
        ttype, meaning, normalized))