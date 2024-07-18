def findPairs(a, K): 
    res = []
    while a:
        num = a.pop()
        diff = K - num
        if diff in a:
            res.append((diff, num))
    res.reverse()
    return res
     
a = [1, 5, 3, 7, 9]
K = 12
print(findPairs(a, K))