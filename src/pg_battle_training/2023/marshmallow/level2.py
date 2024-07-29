S = input()
A, B = map(int, S.split("x^"))
print(f"{A*B}x^{B-1}")
