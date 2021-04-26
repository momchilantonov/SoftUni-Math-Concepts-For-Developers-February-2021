import matplotlib.pyplot as plt
import numpy as np


def calculating_matching_probability(people):
    return 1-np.exp(-people ** 2 / 730)


def get_people_count():
    return 1 / 2+np.sqrt(1 / 4+2 * np.log(2) * 365)


def plot_birthday_paradox(*args):
    plt.plot(args[0], label="Probability of a matching pair", color="blue")
    plt.scatter(args[1], args[2], label=f"Probability > 50%", color="red")
    plt.vlines(args[1], ymin=0, ymax=args[2], color="green", linestyle="--")
    plt.hlines(args[2], xmin=0, xmax=args[1], color="green", linestyle="--")
    plt.xlim(0, 100)
    plt.ylim(0, 1.1)
    plt.xticks(np.arange(0, 101, 5))
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.xlabel("Number of people", fontsize="large")
    plt.ylabel("Probability", fontsize="large")
    plt.title("Birthday Paradox", fontsize="large")
    plt.legend(loc="center right")
    plt.grid(linestyle="--")
    plt.show()


days_range = np.arange(366)
matching_probabilities = [calculating_matching_probability(people) for people in days_range]
people_count = int(np.ceil(get_people_count()))
probability_at_people_count = matching_probabilities[people_count]
plot_birthday_paradox(matching_probabilities, people_count, probability_at_people_count)
# print(f"People count at probability more than 50% - {people_count}")
# print(f"Exactly probability at {people_count} people - {probability_at_people_count}")
