def plural(noun):
    if noun.endswith("y"):
        return noun[:-1] + "ies"
    else:
        return noun + "s"

word = input("Enter a noun: ")
print("Plural:", plural(word))

