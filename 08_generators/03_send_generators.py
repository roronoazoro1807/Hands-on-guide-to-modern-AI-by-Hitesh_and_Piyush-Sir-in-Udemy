def chai_customer():
    print("Welcome ! What chai would you like?")
    order = yield  # pause & wait for first order from send()
    while True:
        print(f"Preparing : {order}")
        order = yield  # pause again and wait for next order


stall = chai_customer()
next(stall)  # Start generator → runs until first yield

# Now generator is waiting for a value at "order = yield"
stall.send("Ginger Chai")  # sends "Ginger Chai", prints "Preparing : Ginger Chai"
stall.send("Masala Chai")  # sends "Masala Chai", prints "Preparing : Masala Chai"
