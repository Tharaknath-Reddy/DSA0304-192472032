# Program 1: Rule-Based Morphological Processing

words = ["analyzing", "analysis", "analytical"]

print("=" * 95)
print("{:<15}{:<15}{:<15}{:<18}{:<18}{:<15}".format(
    "Original", "Root", "Affix", "Transformation", "Normalized", "Structure"))
print("=" * 95)

for word in words:

    if word.endswith("ing"):
        root = word[:-3]
        affix = "-ing"
        ttype = "Inflectional"
        normalized = "analyze"
        structure = root + " + ing"

    elif word.endswith("sis"):
        root = "analyze"
        affix = "-sis"
        ttype = "Derivational"
        normalized = "analyze"
        structure = "analy + sis"

    elif word.endswith("ical"):
        root = "analyze"
        affix = "-ical"
        ttype = "Derivational"
        normalized = "analyze"
        structure = "analytic + al"

    else:
        root = word
        affix = "-"
        ttype = "Base"
        normalized = word
        structure = word

    print("{:<15}{:<15}{:<15}{:<18}{:<18}{:<15}".format(
        word, root, affix, ttype, normalized, structure))