# this is the mainfile, where the main simulation is run
import config
import popclass
import virfunctions
import matplotlib.pyplot as plt

# initialize dic and population
dic = config.Config()
pop = popclass.Population(dic)


plotsusceptible = [pop.susceptible]
plotincubating = [sum([x[0] for x in pop.incubating])]
plotinfected = [sum(pop.infected)]
plothealed = [pop.healed]
plotdied = [pop.died]
endtrigger = False
overrundays = 30

for day in range(dic.runtime):
    if dic.loud:
        print('############################# day', day, '###############################')
    # find out how many more people become infected:
    virfunctions.calcnewincubating(day, pop, dic)
    virfunctions.calcnewinfected(day, pop, dic)
    virfunctions.processinfected(day, pop, dic)

    plotsusceptible.append(pop.susceptible)
    plotincubating.append(sum([x[0] for x in pop.incubating]))
    plotinfected.append(sum(pop.infected))
    plothealed.append(pop.healed)
    plotdied.append(pop.died)

    if endtrigger:
        overrundays -= 1
        if overrundays < 1:
            break
    elif pop.susceptible < 20:
        endtrigger = True


plt.plot(plotsusceptible, c='red')
plt.plot(plotincubating, c='blue')
plt.plot(plothealed, c='green')
plt.plot(plotinfected, c='yellow')


plt.show()

