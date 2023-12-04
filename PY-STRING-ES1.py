# outsafe
#1. Write a function that counts the NOT vowels in a string;
def function1(s):
    return len([x for x in s if x.lower() not in "aeiou"])

# devsmachna
# Esercizio 8

def multi_list(l):
    return [
        [x for x in l if isinstance(x, str)],
        [x for x in l if isinstance(x, (int, float, complex)) and not isinstance(x, bool)],
        [x for x in l if isinstance(x, bool)]
    ]
    

