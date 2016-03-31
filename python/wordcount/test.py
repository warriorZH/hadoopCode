from itertools import groupby


def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends)
print friends
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))
