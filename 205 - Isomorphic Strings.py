def isIsomorphic(s, t):
    mapDict1 = {}
    mapDict2 = {}
    isIsomorphic = True
    for i in range(s.__len__()):
        if mapDict1.__contains__(s[i]):
            if mapDict1[s[i]] != t[i]:
                isIsomorphic = False
                break
        elif mapDict2.__contains__(t[i]):
            if mapDict2[t[i]] != s[i]:
                isIsomorphic = False
                break
        else:
            mapDict1[s[i]] = t[i]
            mapDict2[t[i]] = s[i]

    return isIsomorphic

print(isIsomorphic("egcd", "adfd"))