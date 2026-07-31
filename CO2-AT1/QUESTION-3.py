# -----------------------------------------------------------
# Experiment 3: Stemming-Based Preprocessing
# -----------------------------------------------------------

from prettytable import PrettyTable

words = ["played", "player", "playing"]

table = PrettyTable()

table.field_names = [
    "Original",
    "Stem",
    "Removed Affix",
    "Transformation",
    "Normalized Form"
]

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        trans = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        trans = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        trans = "Derivational"

    else:
        stem = word
        affix = "-"
        trans = "-"

    normalized = "play"

    table.add_row([
        word,
        stem,
        affix,
        trans,
        normalized
    ])

print("\nStemming Based Preprocessing\n")
print(table)