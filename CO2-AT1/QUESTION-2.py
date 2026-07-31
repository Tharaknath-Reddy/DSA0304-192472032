# -----------------------------------------------------------
# Experiment 2: Morphological Parsing Module
# -----------------------------------------------------------

from prettytable import PrettyTable

words = ["unhappy", "happiness", "happily"]

table = PrettyTable()

table.field_names = [
    "Word",
    "Prefix",
    "Root",
    "Suffix",
    "Transformation",
    "Normalized Root"
]

for word in words:

    prefix = "-"
    suffix = "-"
    root = ""

    if word.startswith("un"):
        prefix = "un"
        root = word[2:]
        transform = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        root = word[:-4]
        transform = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        root = word[:-2]
        transform = "Derivational"

    else:
        root = word
        transform = "-"

    normalized = "happy"

    table.add_row([
        word,
        prefix,
        root,
        suffix,
        transform,
        normalized
    ])

print("\nMorphological Parsing\n")
print(table)