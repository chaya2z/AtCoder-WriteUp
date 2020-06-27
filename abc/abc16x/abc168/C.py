import numpy
import math
from decimal import Decimal

A, B, H, M = map(int, input().split())
H_angle = (H + (M / 60)) * 30
M_angle = M * 6
sum_angle = abs(H_angle - M_angle)

if sum_angle <= 180:
    pass
else:
    sum_angle = 360 - sum_angle

cos_sum = round(math.cos(Decimal(sum_angle)), 4)

ans = (A ** 2 + B ** 2) - (2 * A * B * cos_sum)

ans = numpy.sqrt(ans)
print(ans)
