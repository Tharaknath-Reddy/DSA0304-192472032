# -----------------------------------------------------------
# Experiment 4: Finite State Morphological Parser
# -----------------------------------------------------------

from prettytable import PrettyTable

words = ["writes", "writing", "written"]

table = PrettyTable()

table.field_names = [
    "Word",
    "State Transition",
    "Morphological Components",
    "Pattern",
    "Root",
    "Normalized"
]

for word in words:

    if word == "writes":

        transition = "q0 -> q1(write) -> q2(+s) -> Accept"
        component = "write + s"
        pattern = "Regular Inflection"
        root = "write"

    elif word == "writing":

        transition = "q0 -> q1(write) -> q2(+ing) -> Accept"
        component = "write + ing"
        pattern = "Regular Inflection"
        root = "write"

    elif word == "written":

        transition = "q0 -> q1(write) -> q2(irregular: written) -> Accept"
        component = "write + irregular(en)"
        pattern = "Irregular Inflection"
        root = "write"

    table.add_row([
        word,
        transition,
        component,
        pattern,
        root,
        root
    ])

print("\nFinite State Morphological Parser\n")
print(table)