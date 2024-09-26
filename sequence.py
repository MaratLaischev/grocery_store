def sequence(n):
    return ''.join(str(i) * i for i in range(1, int(n) + 1))


print(sequence(5))
