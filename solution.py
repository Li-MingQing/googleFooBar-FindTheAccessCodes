def solution(l):
    # Your code here
    # Time complexity is O(n^2)
    res = 0
    for num in range(1,len(l)-1):
        left = l[:num]
        right = l[num+1:]
        leftNum = 0
        rightNum = 0
        for nums in left:
            if l[num] % nums == 0:
                leftNum +=1
            else:
                continue
        for nums in right:
            if nums % l[num] == 0:
                rightNum += 1
            else:
                continue
        res += leftNum*rightNum
    return res
