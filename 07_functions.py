#Basic Shape
def greet(name):
    return f"Hello, {name}"

message = greet("Urek")
print(message)

# Parameters vs Arguments
# return vs print

def add_print(a, b):
    print(a + b)        # prints, returns None

def add_return(a, b):
    return a + b        # returns the value

x = add_print(2, 3)     # prints 5, but x is None
y = add_return(2, 3)    # y is 5

print(x)                # None
print(y)                # 5


# Default values:

def greet(name, greeting = "Hello"):
    return f"{greeting}, {name}"

print(greet("Urek"))
print(greet("Urek", "Good day"))


# Scope:

total = 0

def add_to_total(amount):
    total = amount              # this creates a NEW local var, total
    return total

print(add_to_total(5))          # 5
print(total)                    # 0 - global var, total unchanged!