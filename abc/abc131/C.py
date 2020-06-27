import fractions

A, B, C, D = map(int, input().split())

lcm = C * D // fractions.gcd(C, D)

multiple_C_under_A = (A - 1) // C
multiple_D_under_A = (A - 1) // D
multiple_CD_under_A = (A - 1) // lcm

multiple_C_under_B = B // C
multiple_D_under_B = B // D
multiple_CD_under_B = B // lcm

total = B - A + 1

print(total - (multiple_C_under_B - multiple_C_under_A + multiple_D_under_B - multiple_D_under_A - (
            multiple_CD_under_B - multiple_CD_under_A)))
