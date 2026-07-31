# -----------------------------------------------------------
# Experiment 5: Porter Stemmer
# -----------------------------------------------------------

from nltk.stem import PorterStemmer
from prettytable import PrettyTable

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

table = PrettyTable()

table.field_names = [
    "Original Word",
    "Applied Rule",
    "Intermediate Form",
    "Final Stem"
]

for word in words:

    intermediate = word

    if word.endswith("ational"):
        intermediate = word.replace("ational", "ate")
        rule = "ational → ate"

    elif word.endswith("ation"):
        intermediate = word.replace("ation", "ate")
        rule = "ation → ate"

    elif word.endswith("ate"):
        intermediate = word[:-1]
        rule = "remove e"

    else:
        rule = "Porter Rule"

    final = ps.stem(word)

    table.add_row([
        word,
        rule,
        intermediate,
        final
    ])

print("\nPorter Stemmer\n")
print(table)