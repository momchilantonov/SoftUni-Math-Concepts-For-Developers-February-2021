import matplotlib.pyplot as plt
from secrets import randbits
from sympy import Mul, factorint
import timeit


def get_bits(start_bit, end_bit, step=8):
    return [bit for bit in range(start_bit, end_bit, step)]


def get_times(bits):
    fact_times = []
    mul_times = []
    for bit in bits:
        fact_param = randbits(bit)
        mul_param = [k ** v for k, v in factorint(fact_param).items()]
        fact_time = timeit.timeit(lambda: factorint(fact_param), "from sympy import factorint", number=1000)
        mul_time = timeit.timeit(lambda: Mul(*mul_param), "from sympy import Mul", number=1000)
        fact_times.append(fact_time)
        mul_times.append(mul_time)
    return fact_times, mul_times


def plot_result(bits, fact, mul):
    plt.plot(bits, fact)
    plt.plot(bits, mul)
    plt.legend(["Factorization", "Multiplication"])
    plt.xlabel("Bits")
    plt.ylabel("Time[s]")
    plt.grid()
    plt.show()


bits_list = get_bits(8, 64)
factorizations, multiplications = get_times(bits_list)
plot_result(bits_list, factorizations, multiplications)
print(factorizations)
print(multiplications)
