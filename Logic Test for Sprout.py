def nameValidator(name):
    listOfWord = name.split()
    if(len(listOfWord) < 2):
        return False
    #Check if name not a word. Minimum length must be 2 (ex: 'A.' or 'Ed'). Also capitalized only on first letter of each word
    for item in listOfWord:
        if (len(item) < 2) or (not item[0].isupper()):
            return False
    #Check if last word ends with '.' ex: 'Angelina Kesya.' or 'Angelina Kesya Putri.'
    if(listOfWord[-1].endswith('.')):
        return False
    if(len(listOfWord) == 2):
        if(listOfWord[0].endswith('.')):
            if(len(listOfWord[0]) > 2):
                return False
        if(listOfWord[1].endswith('.')):
            return False
    if(len(listOfWord) == 3):
        if(listOfWord[0].endswith('.')):
            if(len(listOfWord[0]) > 2):
                return False
            else:
                if(not listOfWord[1].endswith('.')):
                    return False
        if(listOfWord[0].endswith('.') and listOfWord[1].endswith('.')):
            if((len(listOfWord[0]) > 2) or (len(listOfWord[1]) > 2)):
                return False
    for item in listOfWord:
        if((len(item)>=2) and (item[-1]!='.')):
            if(not item[1:].islower()):
                return False
    return True

def findDisapperared(nums):
    n = len(nums)
    res = []
    for i in range(1,n+1):
        if(i not in nums):
            res.append(i)
    return res

#DRIVER

print(nameValidator("A. Kesya"))
print(nameValidator("A. K. Putri"))
print(nameValidator("Angelina K. Putri"))
print(nameValidator("Angelina Kesya Putri"))
print("\n===========================================\n")
print(nameValidator("Angelina"))
print(nameValidator("A kEsya"))
print(nameValidator("A. K Putri"))
print(nameValidator("a. Kesya"))
print(nameValidator("A. kesya"))
print(nameValidator("a. k. Putri"))
print(nameValidator("A. Kesya Putri"))
print(nameValidator("A. K. P."))
print(nameValidator("Angelina. K. Putri"))
print(nameValidator("Angelina K. PuTri"))
print(nameValidator("Angelina KesyA"))

print("\n\n===========================================\n\n")

print(findDisapperared([4,3,2,7,8,2,3,1]))
print(findDisapperared([1,1]))