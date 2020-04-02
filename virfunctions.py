# this stores all functions related to the virus and how it spreads
import math

def calcnewincubating(day, population, dic):
    allinfected = sum(population.infected)
    fractionsusceptible = max(population.susceptible / population.population, 0)
    if dic.loud:
        print('fractionsusceptible', fractionsusceptible)
    contacts = round(allinfected * fractionsusceptible * dic.contactsperday)
    print('contacts', contacts)
    newincubating = round(contacts * dic.infectprobability)
    print('newincubating')
    population.susceptible -= newincubating
    population.incubating.append([int(newincubating), int(newincubating)])


def calcnewinfected(day, population, dic):
    print('old incubating')
    print(population.incubating)
    newsick = 0
    for i, fraction in enumerate(dic.sickstart):
        if i > len(population.incubating):
            break
        thisdaysick = min(math.ceil(fraction * population.incubating[-i][1]), population.incubating[-i][0])
        newsick += thisdaysick
        population.incubating[-i][0] -= thisdaysick

    population.infected.append(newsick)
    print('new incubating')
    print(population.incubating)


def processinfected(day, population, dic):
    if len(population.infected) < dic.illnessduration:
        return
    infected = population.infected[-dic.illnessduration]
    population.infected[-dic.illnessduration] = 0
    died = int(infected * dic.mortalityrate)
    healed = infected - died

    population.healed += healed
    population.died += died
