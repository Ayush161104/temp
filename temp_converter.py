# temp_converter.py

def c_to_f(c):
    return c * 1.8 + 32

def f_to_c(f):
    return (f - 32) / 1.8 

print("25C in F:", c_to_f(25))
print("77F in C:", f_to_c(77))
