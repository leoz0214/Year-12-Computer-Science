from math import e
from matplotlib import pyplot as plt


def predator_prey(
    prey: int, predators: int, A: float, B: float, C: float, D: float,
    max_generation: int | None = float("inf"), output: bool = True,
    graph: bool = False) -> None:
    """
    Outputs the number of prey and predators in each generation until one them
    drops below 2.
    """
    generation = 0
    counts = {
        "prey": [prey],
        "predators": [predators]
    }
    while prey >= 2 and predators >= 2 and generation < max_generation:
        prey_growth_rate = e ** (A - C * predators)
        prey *= prey_growth_rate

        predator_growth_rate = e ** (D * C * prey - B)
        predators *= predator_growth_rate

        counts["prey"].append(prey)
        counts["predators"].append(predators)

        generation += 1
        if output:
            print(
                "Generation {}: {} prey, {} predators".format(
                    generation, round(prey), round(predators)))
    if graph:
        plt.scatter(counts["predators"], counts["prey"])
        plt.show()


def test():
    predator_prey(30, 5, 0.8, 0.5, 0.1, 0.3, 10)
    predator_prey(30, 5, 0.8, 0.5, 0.1, 0.3, 100000, False, True)
    predator_prey(100000, 1000, 0.8, 0.5, 0.1, 0.3, 100000, False, True)


test()