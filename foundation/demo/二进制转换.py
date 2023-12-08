m = ""


while number:
    m += str(number % 2)
    number //= 2
print(m[::-1], len(m), 2**12)

for i in range(0, 13):
    print(i, "=", 2 ** i)