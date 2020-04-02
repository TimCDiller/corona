# this is the file to store the different classes used for this simulation


class Population:
    def __init__(self, dic):
        self.population = dic.population
        self.susceptible = self.population
        self.incubating = [[0, 0]]
        self.infected = [dic.startinfected]
        self.healed = 0
        self.died = 0
