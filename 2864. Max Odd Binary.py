class Solution(object):
    def maximumOddBinaryNumber(self, s):
        newStr = ""
        position = 0
        for i in range(len(s)):
            if (len(newStr) > 0):
                if (s[i] == '1'):
                    if newStr[-1] != '1':
                        newStr += s[i]
                    else:
                        newStr = ''.join([s[i], newStr])
                        position += 1
                else:
                    newStr = newStr[:position] + s[i] + newStr[position:]
            else:
                newStr += s[i]
        return newStr
