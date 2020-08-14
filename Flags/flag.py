# Different ways to test multiple
# flags at once in Python
w, x, y, z = 0, 1, 0, 3

if x == 1 or y == 1 or z == 1 or w == 2:
    print('passed')
else:
    print("X")

if 1 in (w, y, z):
    print('passed')
else:
    print("X")

# These only test for truthiness:
if x or y or z:
    print('passed')
else:
    print("X")

if any((x, y, z)):
    print('passed')
else:
    print("X")
