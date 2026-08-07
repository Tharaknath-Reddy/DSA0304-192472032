# Program 4: Morphological Parsing

words = ["activate", "activation", "reactivation"]

print("=" * 135)
print("{:<18}{:<10}{:<12}{:<12}{:<25}{:<18}{:<20}".format(
    "Original", "Prefix", "Root", "Suffix",
    "Derivation Sequence", "Normalized", "Parsed"))
print("=" * 135)

for word in words:

    if word == "activate":
        prefix = "-"
        root = "activate"
        suffix = "-"
        sequence = "Base"
        normalized = "activate"

    elif word == "activation":
        prefix = "-"
        root = "activate"
        suffix = "-ion"
        sequence = "activate -> activation"
        normalized = "activate"

    elif word == "reactivation":
        prefix = "re-"
        root = "activate"
        suffix = "-ion"
        sequence = "activate -> activation -> reactivation"
        normalized = "activate"

    parsed = prefix + " " + root + " " + suffix

    print("{:<18}{:<10}{:<12}{:<12}{:<25}{:<18}{:<20}".format(
        word, prefix, root, suffix,
        sequence, normalized, parsed))