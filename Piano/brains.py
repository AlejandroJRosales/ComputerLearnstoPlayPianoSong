import random

iterations = 200
pop_size = 10000
tournament_size = 7
pop_keep = .6
prob_crossover = 0.9
prob_mutation = 0.15


def generate_population(genes_per_ch, interval_min, interval_max):
	individuals = []
	for i in range(0, pop_size):
		chromosomes = []
		for c in range(0, genes_per_ch):
			chromosomes.append(random.randint(interval_min, interval_max))
		individuals.append(chromosomes)
	return individuals
	
	
def calc_fitness(population, genes_per_ch, interval_min, interval_max, target):
	pop_fitness = []
	for individual in range(len(population)):
		if len(population[individual]) < genes_per_ch:
			missing_chr = genes_per_ch - len(population[individual])
			for i in range(0, missing_chr):
				individual_index = population[individual]
				individual_index.append(random.randint(interval_min, interval_max))
		fitness = 0
		for i in range(len(target)):
			place = population[individual]
			difference = abs(target[i] - place[i])
			fitness += difference
		pop_fitness.append(fitness)
	return pop_fitness
	
	
def select_fittest(population, fitness_scores, genes_per_ch, interval_min, interval_max):
	fitter_population = []
	for i in range(0, int(len(population) * pop_keep)):
		r = random.randint(0, len(fitness_scores) - 1)
		best = fitness_scores[r]
		best_index = population[r]
		for member in range(0, tournament_size):
			competitor_index = random.randint(0, len(fitness_scores) - 1)
			if fitness_scores[competitor_index] < best:
				best = fitness_scores[competitor_index]
				best_index = population[competitor_index]
		fitter_population.append(best_index)
	for a in range(len(population) - len(fitter_population)):
		chromosomes = []
		for c in range(0, genes_per_ch):
			chromosomes.append(random.randint(interval_min, interval_max))
		fitter_population.append(chromosomes)
	return fitter_population
	
	
def crossover(population, genes_per_ch):
	for individual in range(int((len(population) - 2))):
		if random.random() <= prob_crossover:
			ch1 = population.pop(individual)
			ch2 = population.pop(individual + 1)
			r = random.randint(0, genes_per_ch)
			population.insert(individual, ch1[:r] + ch2[r:])
			population.insert(individual + 1, ch2[:r] + ch1[r:])
	return population
	
	
def mutation(population, interval_min, interval_max):
	for individual in range(int((len(population) - 1))):
		if random.random() <= prob_mutation:
			ch = population.pop(individual)
			for i in range(0, 3):
				r = random.randint(0, 2)
				get_chr = ch.pop(random.randint(0, len(ch) - 1))
				mutate = 1
				if r == 0:
					if get_chr >= interval_min + mutate:
						ch.append(get_chr - mutate)
					else:
						break
				else:
					if get_chr <= interval_max - mutate:
						ch.append(get_chr + mutate)
					else:
						break
			population.append(ch)
		return population
		
		
def breed(population, genes_per_ch, interval_min, interval_max):
	return mutation(crossover(population, genes_per_ch), interval_min, interval_max)
	
	
def learn(target):
	genes_per_ch = len(target)
	interval_max = max(target)
	interval_min = min(target)
	
	play = []
	population = generate_population(genes_per_ch, interval_min, interval_max)
	play.append(population[random.randint(0, len(population))])
	for generation in range(0, iterations + 1):
		pop_fitness = calc_fitness(population, genes_per_ch, interval_min, interval_max, target)
		if generation % 15 == 0:
			best = min(pop_fitness)
			mode = max(set(pop_fitness), key=pop_fitness.count)
			worst = max(pop_fitness)
			display_best = pop_fitness[pop_fitness.index(best)]
			display_worst = pop_fitness[pop_fitness.index(worst)]
			print("[G %3d] score=(%4d, %4d, %4d): %r" %
			(generation, display_best, mode, display_worst, population[pop_fitness.index(best)]))
			play.append(population[pop_fitness.index(best)])
			if min(pop_fitness) == 0:
				return play, min(pop_fitness)
		population = breed(select_fittest(population, pop_fitness, genes_per_ch, interval_min, interval_max), genes_per_ch, interval_min, interval_max)
	return play, min(pop_fitness)

