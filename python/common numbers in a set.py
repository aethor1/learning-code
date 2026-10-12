commonNumbers = 0

for n in range(1,2005):
    if (4 * n) % 6 == 0:
        commonNumbers = commonNumbers + 1

print(commonNumbers)
