# Global variables in Python
print('Filename: 01-global-variables.py   Version: 1.0', '\n')


gvar = 1
print('gvar:', gvar, '  id(gvar):', id(gvar))
print()


def my_1fun():
    print('Gloval variable inside my_1fun() -> gvar:', gvar, 'id(gvar):', id(gvar))
    print()


def my_2fun():
    gvar = 2
    print('Local variable inside my_2fun() -> gvar:', gvar, 'id(gvar):', id(gvar))
    print()


def my_3fun():
    global gvar
    gvar = 3
    print('GLobal KEYWORD inside my_3fun() -> gvar:', gvar, 'id(gvar):', id(gvar))
    print()


my_1fun()

my_2fun()

print('Outside any function -> gvar:', gvar, '  id(gvar):', id(gvar))
print()

my_3fun()

print('Outside any function -> gvar:', gvar, '  id(gvar):', id(gvar))
print()

