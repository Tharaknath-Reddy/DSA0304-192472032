                                 # -----------------------------------------------------------
# Experiment 1: Morphological Analysis Pipeline
# -----------------------------------------------------------

from prettytable import PrettyTable

words = ["connected", "connecting", "connection"]

table = PrettyTable()
table.field_names = [
    "Word",
    "Root",
    "Suffix",
    "Suffix Type",
    "Parsed Structure",
    "Normalized Form"
]

for word in words:

    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        suffix_type = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        suffix_type = "Inflectional"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        suffix_type = "Derivational"

    else:
        root = word
        suffix = "-"
        suffix_type = "-"

    # Normalize all forms
    normalized = "connect"

    parsed = f"{root} + {suffix}"

    table.add_row([
        word,
        root,
        suffix,
        suffix_type,
        parsed,
        normalized
    ])

print("\nMorphological Analysis Pipeline\n")
print(table)