# A generator function: uses 'yield' instead of 'return'
def serve_chai():
    yield "Masala chai"  # pauses here and gives value
    yield "Lemon chai"
    yield "Ginger chai"
    yield "john cena chai"


print(serve_chai())  # just shows a generator object, not values

stall = serve_chai()  # create generator

# for loop automatically calls next() on generator
for chai in stall:
    print(chai)


# Another generator
def get_chai_gen():
    yield "1chai"
    yield "2 chai"
    yield "3 chai"
    yield "4 chai"


chai_cup = get_chai_gen()  # generator created but not executed yet

# manually calling next() one by one
print(next(chai_cup))  # 1chai
print(next(chai_cup))  # 2 chai
print(next(chai_cup))  # 3 chai
print(next(chai_cup))  # 4 chai

# If you call next() again -> StopIteration error (no more values)
# print(next(chai_cup))
