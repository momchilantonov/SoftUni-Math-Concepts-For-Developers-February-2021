from math import gcd
from sympy import randprime
from secrets import randbelow


def get_prime_num(start_num, end_num):
    return randprime(start_num, end_num+1)


def is_primitive_root(coprime_set, n, modulo):
    return coprime_set == {pow(n, power, modulo) for power in range(1, modulo)}


def get_primitive_root(modulo):
    coprime_set = {n for n in range(1, modulo) if gcd(n, modulo) == 1}
    primitive_roots = [n for n in range(1, modulo) if is_primitive_root(coprime_set, n, modulo)]
    return min(primitive_roots)


def get_secret_num(num):
    return randbelow(num+1)


def get_shared_num(mod_p, root_g, secret_num):
    return (root_g ** secret_num) % mod_p


def get_shared_key(mod_p, secret_num, shared_num):
    return (shared_num ** secret_num) % mod_p


modulo_p = get_prime_num(1, 100)
primitive_root_g = get_primitive_root(modulo_p)
secret_num_a = get_secret_num(100)
secret_num_b = get_secret_num(100)
shared_num_a = get_shared_num(modulo_p, primitive_root_g, secret_num_a)
shared_num_b = get_shared_num(modulo_p, primitive_root_g, secret_num_b)
shared_key_a = get_shared_key(modulo_p, secret_num_a, shared_num_b)
shared_key_b = get_shared_key(modulo_p, secret_num_b, shared_num_a)
assert shared_key_a == shared_key_b

print(modulo_p)
print(primitive_root_g)
print(secret_num_a)
print(secret_num_b)
print(shared_num_a)
print(shared_num_b)
print(shared_key_a)
print(shared_key_b)
