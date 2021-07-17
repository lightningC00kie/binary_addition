

def binary_addition(n, a1, a2):

    carry = []
    answer = []

    for i in range(n-1, -1, -1):
        a = a1[i]
        b = a2[i]
        if len(carry) == 0:
            if a == 0 and b == 0:
                c = 0
            if a == 1 and b == 1:
                c = 0
                carry.append(1)
            if a == 1 and b == 0:
                c = 1
            if a == 0 and b == 1:
                c = 1
            answer.append(c)
        else:
            if a == 0 and b == 0:
                c = 1
            if a == 1 and b == 1:
                c = 1
                carry.append(1)
            if a == 1 and b == 0:
                c = 0
                carry.append(1)
            if a == 0 and b == 1:
                c = 0
                carry.append(1)
            carry.pop()
            answer.append(c)

    if len(carry) != 0:
        answer.append(1)
    else:
        answer.append(0)
    
    answer = answer[::-1]
    return answer
a1 = [0,1,1,1,1,0,0,1]
a2 = [1,1,0,1,0,1,0,1]
print(binary_addition(8, a1, a2))