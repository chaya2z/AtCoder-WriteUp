W, H, x, y = map(int, input().split())

area = (W * H) / 2
div = 0
if W * H != 0 and W / 2 == x and H / 2 == y:
    div = 1

print(area, div)
