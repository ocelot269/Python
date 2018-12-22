"""X = 88  # Global X


def func():
    X = 99  # Local x:hides global,but we want this here

func()
print(X)  # Prints 88:unchanged

X = 88  # global


def func():
    global X  # Esto hace que la proxima X sea global
    X = 99  # Global X:Outside def

func()
print(X)  # Prints 99

y, z = 1, 2


def all_global():
    global x #Al hacer que x se ha global su contenido tmb es global
    x = y + z
all_global()
print(x)

# Global variables in module
# Declare globals assigned
# No need to declare y,z: LEGB rule

# x existe ahora en el ambito global con valor 3

# NESTED SCOPES

X = 99


def f1():
    X = 88

    def f2():  # Esta funcion no existe fuera de su funcion
        # Esto entiende que la variable es Global porque cuelga de la otra
        # funcion
        print(X)
    f2()

f1()
# Este print te permite entender que al salir de la funcion solo coge la X
# GLOBAL.
print(X)
"""
# Factory Functions: Closures

# a closure or a factory function, the former describing a functional programming technique, and the latter denoting a design pattern.
# the function object in question remembers values in enclosing scopes
# regardless of whether those scopes are still present in memory.


def f1():
    X = 88

    def f2():
        print(X)
    return f2

action = f1()
action()
