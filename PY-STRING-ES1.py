# outsafe
#1. Write a function that counts the NOT vowels in a string;
def function1(s):
    return len([x for x in s if x.lower() not in "aeiou"])

# 2. Write a function that given a long string (a text) counts the words in it;
def countsWords(str) :
    return len(str.split())

# 3. Write a function that given a long string (a text) computes the frequencies of the vowels in it;
def countsVowels(str) :
    return len([char for char in str if (char in 'aeiou')])

# 4. Write a function that given a list returns a string representation of it;
def returnsString(list) :
    return " ".join(list)

# 5. Write a function that given a list of numbers gives back the product of all its elements;
def sumNumbers(list) :
    return sum(list)

# 6. Write a function that given two lists checks if they have common elements;
def twoList(list1, list2) :
    return len(set(list1).intersection(set(list2))) != 0 

# 7. Write a function that capitalizes all (and only) the vowels in a string;
def allVowels(str) :
    return "".join([char.upper() if (char in 'aeiou') else char for char in str])

# devsmachna
# Esercizio 8

def multi_list(l):
    return [
        [x for x in l if isinstance(x, str)],
        [x for x in l if isinstance(x, (int, float, complex)) and not isinstance(x, bool)],
        [x for x in l if isinstance(x, bool)]
    ]

