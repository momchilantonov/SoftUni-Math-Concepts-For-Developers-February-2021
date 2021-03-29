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


def get_mean_times(sizes, num_start=0, num_stop=100, trails=10):
    py_mean_times = []
    np_mean_times = []
    for size in sizes:
        np_array = np.random.uniform(num_start, num_stop, size=size)
        py_list = list(np_array)
        py_current_times = []
        for trail in range(trails):
            py_current_times.append(sum_array_with_py(py_list))
        py_mean_times.append(np.mean(py_current_times))
        np_current_times = []
        for trail in range(trails):
            np_current_times.append(sum_array_with_np(np_array))
        np_mean_times.append(np.mean(np_current_times))
    return py_mean_times, np_mean_times


def get_speedup_factor(py_times, np_times):
    speedup = []
    for idx in range(len(np_times)):
        if not py_times[idx] == 0:
            speedup.append(np_times[idx] / py_times[idx])
        else:
            speedup.append(0)
    return speedup


def plot_times(sizes, py_times, np_times):
    plt.plot(py_times, color="red")
    plt.plot(np_times, color="blue")
    plt.xlim(0, len(sizes))
    plt.ylim(-0.05, max(py_times) * 1.5)
    plt.xticks([0, 2, 4, 6, 8, 10], ["10²", "10³", "10⁴", "10⁵", "10⁶", "10⁷"], rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel("array/list size", loc="center", fontsize="x-large")
    plt.ylabel("time[s]", loc="center", fontsize="x-large")
    plt.legend(["PythonSum(list)", "NumPySum(array)"], fontsize="large", loc='upper left')
    plt.title("Performance Test", fontsize="xx-large")
    plt.grid()
    plt.show()


def plot_speedup_factor(sizes, speedup):
    plt.plot(speedup, color="magenta")
    plt.xlim(0, len(sizes))
    plt.ylim(0, max(speedup) * 1.1)
    plt.xticks([0, 2, 4, 6, 8, 10], ["10²", "10³", "10⁴", "10⁵", "10⁶", "10⁷"], rotation=45)
    plt.yticks(rotation=45)
    plt.xlabel("array/list size", loc="center", fontsize="x-large")
    plt.ylabel("speedup factor", loc="center", fontsize="x-large")
    plt.legend(["NPTimes(array)/PYTimes(list)"], fontsize="large", loc='lower right')
    plt.title("SpeedUp Factor", fontsize="xx-large")
    plt.grid()
    plt.show()


array_sizes = np.arange(10 ** 2, 10 ** 7, 10 ** 6)
py_times_list, np_times_array = get_mean_times(array_sizes)
speedup_factor = get_speedup_factor(py_times_list, np_times_array)
plot_times(array_sizes, py_times_list, np_times_array)
plot_speedup_factor(array_sizes, speedup_factor)
