def finite_state_automaton(s):
    if s.endswith("ab"):
        return "Accepted"
    else:
        return "Rejected"

string = input("Enter a string: ")
print(finite_state_automaton(string))