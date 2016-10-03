from helloworld import HelloWorld, HelloWorld2

hw = HelloWorld()
r1 = 2
r2 = 3
hw.set(r1, r2)
s = hw.get()
print("Hello, World! sin({} + {}) = {}".format(r1, r2, s))
hw.print_()

hw2 = HelloWorld2()
hw2.set(r1, r2)
s = hw2.gets()
print("Hello, World2! sin({} + {}) = {}".format(r1, r2, s))
