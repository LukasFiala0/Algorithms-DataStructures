# Fibonnacci sequence using for loop:
def fibonnacci_1(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[i-1] + seq[i-2])
    return seq
print(fibonnacci_1(100)[99])
# Fibonnacci sequence using recursion
def fibonnacci_2(seq=list, n=int):
    if n == 0:
        return [0]
    if n == 1:
        return [0, 1]
    if len(seq) == n:
        return seq
    fibb = seq[-1] + seq[-2]
    seq.append(fibb)

    return fibonnacci_2(seq, n)

seq = [0, 1]
n = 100
print(fibonnacci_2(seq, n)[99])


def F(n):
    if n <= 1:
        return n
    else:
        return F(n - 1) + F(n - 2)

print(F(1))