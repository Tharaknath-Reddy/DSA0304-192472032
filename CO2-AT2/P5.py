# Program 5: Inflectional Morphology

words = ["create", "creates", "creating"]

print("=" * 120)
print("{:<15}{:<10}{:<25}{:<15}{:<18}{:<15}".format(
    "Original", "Suffix",
    "Grammar Category", "Root",
    "Normalized", "Representation"))
print("=" * 120)

for word in words:

    if word == "create":
        suffix = "-"
        grammar = "Base Form"
        root = "create"

    elif word.endswith("s"):
        suffix = "-s"
        grammar = "3rd Person Singular"
        root = "create"

    elif word.endswith("ing"):
        suffix = "-ing"
        grammar = "Present Participle"
        root = "create"

    normalized = "create"

    print("{:<15}{:<10}{:<25}{:<15}{:<18}{:<15}".format(
        word, suffix,
        grammar, root,
        normalized,
        root + suffix))