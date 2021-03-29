from time import time
import numpy as np
import matplotlib.pyplot as plt
from functools import wraps


def performance_test(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        start_time = time()
        function(*args, **kwargs)
        end_time = time()
        time_result = end_time-start_time
        return time_result

    return wrapper


@performance_test
def sum_array_with_py(array):
    return sum(array)


@performance_test
def sum_array_with_np(array):
    return np.sum(array)


def get_mean_times_with_list(exec_time_func, sizes, num_start=0, num_stop=100, trails=10):
    mean_times = []
    for size in sizes:
        array = list(np.random.uniform(num_start, num_stop, size=size))
        current_times = []
        for trail in range(trails):
            current_times.append(exec_time_func(array))
        mean_times.append(np.mean(current_times))
    return mean_times


def get_mean_times_with_array(exec_time_func, sizes, num_start=0, num_stop=100, trails=10):
    mean_times = []
    for size in sizes:
        array = np.random.uniform(num_start, num_stop, size=size)
        current_times = []
        for trail in range(trails):
            current_times.append(exec_time_func(array))
        mean_times.append(np.mean(current_times))
    return mean_times


def get_speedup_factors(py_times_list, np_times_list, py_times_array, np_times_array):
    speedup_list_list = []
    speedup_list_array = []
    speedup_array_list = []
    speedup_array_array = []
    for idx in range(len(np_times_list)):
        if not py_times_list[idx] == 0:
            speedup_list_list.append(np_times_list[idx] / py_times_list[idx])
        else:
            speedup_list_list.append(0)
        if not py_times_list[idx] == 0:
            speedup_list_array.append(np_times_array[idx] / py_times_list[idx])
        else:
            speedup_list_array.append(0)
        if not py_times_array[idx] == 0:
            speedup_array_list.append(np_times_list[idx] / py_times_array[idx])
        else:
            speedup_array_list.append(0)
        if not py_times_array[idx] == 0:
            speedup_array_array.append(np_times_array[idx] / py_times_array[idx])
        else:
            speedup_array_array.append(0)
    return speedup_list_list, speedup_list_array, speedup_array_list, speedup_array_array


def plot_times(sizes, py_times_list, np_times_list, py_times_array, np_times_array):
    plt.plot(py_times_list, color="red")
    plt.plot(np_times_list, color="blue")
    plt.plot(py_times_array, color="orange")
    plt.plot(np_times_array, color="green")
    plt.xlim(0, len(sizes))
    plt.ylim(0, max(py_times_array) * 1.05)
    plt.xticks([0, 2, 4, 6, 8, 10], ["10²", "10³", "10⁴", "10⁵", "10⁶", "10⁷"], rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel("array/list size", loc="center", fontsize="x-large")
    plt.ylabel("time[s]", loc="center", fontsize="x-large")
    plt.legend(["PythonSum(list)", "NumPySum(list)", "PythonSum(array)", "NumPySum(array)"], fontsize="large",
               loc='upper left')
    plt.title("Performance Test", fontsize="xx-large")
    plt.grid()
    plt.show()


def plot_speedup_factors(sizes, speedup_list_list, speedup_list_array, speedup_array_list, speedup_array_array):
    plt.plot(speedup_list_list, color="red")
    plt.plot(speedup_list_array, color="blue")
    plt.plot(speedup_array_list, color="orange")
    plt.plot(speedup_array_array, color="green")
    plt.xlim(0, len(sizes))
    plt.ylim(0, max(speedup_list_list) * 1.05)
    plt.xticks([0, 2, 4, 6, 8, 10], ["10²", "10³", "10⁴", "10⁵", "10⁶", "10⁷"], rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel("array/list size", loc="center", fontsize="x-large")
    plt.ylabel("speedup factor", loc="center", fontsize="x-large")
    plt.legend(["PY list / NP list", "PY list / NP array", "PY array / NP list", "PY array / NP array"],
               fontsize="large", loc='upper left')
    plt.title("SpeedUp Factors", fontsize="xx-large")
    plt.grid()
    plt.show()


array_sizes = np.arange(10 ** 2, 10 ** 7, 10 ** 6)
np_times_list = get_mean_times_with_list(sum_array_with_np, array_sizes)
py_times_list = get_mean_times_with_list(sum_array_with_py, array_sizes)
np_times_array = get_mean_times_with_array(sum_array_with_np, array_sizes)
py_times_array = get_mean_times_with_array(sum_array_with_py, array_sizes)
spf_list_list, spf_list_array, spf_array_list, spf_array_array \
    = get_speedup_factors(py_times_list, np_times_list, py_times_array, np_times_array)
plot_times(array_sizes, py_times_list, np_times_list, py_times_array, np_times_array)
plot_speedup_factors(array_sizes, spf_list_list, spf_list_array, spf_array_list, spf_array_array)
