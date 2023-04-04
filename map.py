# a function and an iterable
nums = [2, 4, 6, 8]
doubles = list(map(lambda x: x*2, nums))
print(doubles)


people = ["adam", "badam", "tadam"]
peeps = list(map(lambda name: name.title(), people))
print(peeps)


def double(x): return x*2


doubles2 = map(double, nums)
print(list(doubles2))
