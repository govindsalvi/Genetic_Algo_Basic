import numpy as np


class GA:
    def __init__(self, string):
        self.target = string
        self.target_size = len(string)
        self.population = []
        self.population_size = 100
        self.mutation_rate = 0.01

    def fitness(self, testString):
        score = 0
        for i in range(self.target_size):
            if self.target[i] == testString[i]:
                score += 1
        return score

    def initialize(self):
        for i in range(self.population_size):
            p = np.random.randint(low=97, high=122, size=self.target_size)
            s = ''
            for j in range(self.target_size):
                s += chr(p[j])
            self.population.append(s)

    def selection(self):
        self.population.sort(key=lambda x: self.fitness(x),reverse=True)
        new_population = self.population[:40]
        rest = np.random.choice(self.population[40:], 10)
        new_population.extend(rest)
        self.population = new_population

    def crossover(self):
        for i in range(50):
            x,y = np.random.choice(50,2,replace=True)
            x,y = self.population[x],self.population[y]
            child = ''
            for j in range(self.target_size):
                if 0.5 <= np.random.rand():
                    child += x[j]
                else:
                    child += y[j]
            self.population.append(child)

    def mutation(self):
        mutatedChild = []
        for i in range(50):
            child = ''
            for j in self.population[i]:
                if self.mutation_rate >= np.random.rand():
                    child += chr(np.random.randint(low=97,high=122))
                else:
                    child += j
            mutatedChild.append(child)
        self.population.extend(mutatedChild)

    def run(self):
        generation = 0
        self.initialize()
        while generation < 1000:
            self.selection()
            self.crossover()
            self.mutation()
            if self.fitness(self.population[0]) == self.target_size:
                break
            generation +=1
        print("After Generation Count", generation, "string is ", self.population[0])
        return 1


x = GA("helloworldxramlaljitelibhagyashreegovindsalvigopalsalvi").run()
print(x)
