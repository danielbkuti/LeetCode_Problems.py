def lengthOfLastWord(s):
    curr = s.__len__() - 1
    counter = 0
    while(s[curr] == ' '):
        curr -= 1
    while (s[curr] != ' ' and curr != -1):
            curr -= 1
            counter += 1
    return counter


print(lengthOfLastWord("H elloWorld!                "))
