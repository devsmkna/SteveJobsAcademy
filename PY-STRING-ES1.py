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

# 9. Write a function that given a list computes the arithmetic mean of the numbers in it;
def meanNumber(list) :
    return sum(list) / len(list)

# 10. Write a function that given a list of strings returns the mean length of the strings in it;
def meanString(list) :
    count = 0
    for element in list :
        for char in element :
            count += 1
    return count / len(list)
    # return sum(len(element) for element in list) / len(list)

# 11. Write a function that given a list of numbers returns the maximum;
def getMax(list) :
    return max(list)

# 12. Write a function that given a list of numbers returns the minimum;
def getMin(list) :
    return min(list)

# 13. Write a function that given a list of numbers returns the median;
def getMedian(list) :
    from statistics import median
    return median(list)

# 14. Write a function that given a list of numbers returns the quartiles;
def getQuartiles(list) :
    import numpy as np
    return np.percentile(list, 25)

# 15. Write a function that given a integer in decimal returns a list of characters with the single digits
# as elements.
def singleDigits(integer) :
    return [int(x) for x in str(integer)]

# 16. Write a function that given a string in roman literals returns the decimal value (use only
# “additive roman numerals”).
def romanNumeralsToDecimal(str) :
    romanNumerals = {"I" : 1,
                    "V" : 5,
                    "X" : 10, 
                    "L" : 50, 
                    "C" : 100, 
                    "D" : 500, 
                    "M" : 1000 }
    return sum(romanNumerals[romanSimbol] for romanSimbol in str)
    """ sum = 0
    for elements in str :
        sum += romanNumerals[elements]
    return sum """

# 18. Write a function that given two hours of a day in the format of strings like “06.34:15” computes
# how many seconds are included in between.
def secondsBetweenTwoHours(str1, str2) :
    arr1 = [int(x) for x in str1.replace(':', '.').split('.')]
    arr2 = [int(x) for x in str2.replace(':', '.').split('.')]
    return abs((3600 * arr2[0] - 3600 * arr1[0]) + (60 * arr2[1] - 60 * arr1[1] + (arr2[2] - arr1[2])))
    """ h1 = (3600 * arr1[0] +  60 * arr1[1] + arr1[2])
    h2 = (3600 * arr2[0] + 60 * arr2[1] + arr2[2])
    return h1 - h2 if h1 > h2 else h2 - h1 """

# 19. Write a function that given a number of seconds returnr the value in days, hours, minutes and
# seconds.
def fromSecondsToDHMS(number) :
    days = number // 86400 
    number -= 86400 * days
    hours = number // 3600
    number -= hours * 3600
    minutes = number // 60
    number -= minutes * 60
    return f"{days} Day/s - {hours}hh:{minutes}mm:{number}ss"

