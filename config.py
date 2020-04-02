# this is the initial config class where all simluation parameters are kept


class Config:
    def __init__(self):

        # general simulation parameters
        self.runtime = 200
        self.loud = 1

        # population parameters
        self.population = 500000
        self.agespread = [0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05]
        self.contactsperday = 70

        # virus parameters
        self.infectprobability = 0.05
        self.contagiousstart = [0, 0, 0.1, 0.3, 0.4, 0.1, 0.07, 0.03]
        self.sickstart = [0, 0, 0, 0, 0.5, 0.5, 0, 0, 0]
        self.illnessduration = 20
        self.mortalityrate = 0.03

        # initialization parameters
        self.startinfected = 50
