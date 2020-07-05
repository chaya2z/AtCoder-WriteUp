N = int(input())
table = [input() for _ in range(N)]

print("AC x " + str(table.count('AC')))
print("WA x " + str(table.count('WA')))
print("TLE x " + str(table.count('TLE')))
print("RE x " + str(table.count('RE')))
