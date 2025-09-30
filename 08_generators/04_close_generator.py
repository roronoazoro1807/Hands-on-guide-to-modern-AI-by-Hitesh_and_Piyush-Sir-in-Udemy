def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for Chai order"
    except:
        print("Stall Closed no more Chai")


stall = chai_stall()
print(next(stall))
stall.close()
