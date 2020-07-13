""""
author: Aniket Giriyalkar
email: giriyalkar.aniket@gmail.com

Problem:
Create an application that will prompt for a user to input a string.
Using the user’s inputted string, find the first letter that is not repeated.

For example: If given the string ‘Bubble’, the letter ‘u’ would be the first
character returned from the program. Once the first character is found and
displayed back to the user, rewrite the string in order of number of occurrences
and order from the inputted string. In the above example ‘Bubble’ would then be
rewritten as ‘uleBbb’. Display this to the user.

"""


def firstNonRepeatingChar(inputStr):
    """
    Function that returns the first non repeating character from the input
    string.
    :param inputStr: input string
    :return: returns the first repeating character from the given string
    """
    charDict = createCharCountDict(inputStr)
    for char in inputStr:
        if charDict[char.lower()] == 1:
            return char


def createCharCountDict(inputStr):
    """
    Function that creates a dictionary to maintain a count of all characters in
    the input string.
    :param inputStr: input string
    :return: Dictionary containing the character count of all the characters in
             the input string
    """
    charDict = {}
    for char in inputStr:
        charDict[char.lower()] = charDict.get(char.lower(), 0) + 1
    return charDict


def reorderStr(inputStr):
    """
    Function that reorders the input string to obtain the solution
    :param inputStr: input string
    :return: result string in order of number of occurrences and order from the
             input string.
    """
    charCountDict = createCharCountDict(inputStr)
    answer = ""
    minCount = min(list(charCountDict.items()), key=lambda x: x[1])[1]
    maxCount = max(list(charCountDict.items()), key=lambda x: x[1])[1]
    for charCount in range(minCount, maxCount + 1):
        for char in inputStr:
            if charCountDict[char.lower()] == charCount:
                answer += char
    return answer

if __name__ == '__main__':
    userInput = input("Enter a string: ")
    nonRepeatingChar = firstNonRepeatingChar(userInput)
    print("First non repeating character is:", nonRepeatingChar)

    reorderedStr = reorderStr(userInput)
    print("Reordered string is:", reorderedStr)
