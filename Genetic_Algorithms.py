import random
from collections import defaultdict

class Genetic_Algorithms: 
    def __init__ (self,interval,cross_over_prob, mutation_prob,wbr) :
        self.interval = interval 
        self.cross_over_prob = cross_over_prob
        self.mutation_prob = mutation_prob
        self.wbr = wbr
       

    #Define fitness function
    def fitness(self,schedule,work_break_ratio):
        #print("calculating fitness")
        score = 0
        
        #balanced with breaks in between
        break_amount = 0
        work_amount = 0 
        
        #punish long stretches of breaks
        break_stretch = 0
        break_stretch_punishment = 10
        in_break = False

        score = score + self.detect_repetitive_tasks(schedule)

        score = score + self.consider_desire_level(schedule)

        if (schedule[0] == "break" or schedule[len(schedule)-1] == "break"):
            score = score - 30
        

        #print ("evaluating breaks")
        for item in schedule:
            if (item == "break"):
                break_amount = break_amount + 1
                
                in_break = True
                break_stretch = break_stretch + 1
                
            else :
                in_break = False
                score = score - (break_stretch * break_stretch_punishment)
                break_stretch = 0
                work_amount = work_amount + 1
        

        #print ("evaluating work and break ratio")
        abs_difference = abs(work_break_ratio - (work_amount - break_amount))
        score = score - (abs_difference * 7)
        
        
        #print("evaluating task priorities")
        #prioritizes more important tasks
        for item in schedule:
            if not (item == "break"):
                score += item.priority 

        return score

    def detect_repetitive_tasks(self,schedule):
        score_update = 0
        for item in schedule:
            if (item == "break"):
                continue
            repeat_time = schedule.count(item)
            max_accepted_num_repeats = (int) (item.ect / self.interval)
            if (repeat_time > max_accepted_num_repeats):
                score_update = score_update - (10 * (repeat_time - max_accepted_num_repeats))

        return score_update

    def consider_desire_level(self,schedule):
        score_update = 0
        distance_from_last_break = 0
        for item in schedule:
            if (item == "break"):
                distance_from_last_break = 0
                continue
            desire_score = distance_from_last_break * item.desire
            desire_score_scale = desire_score / len(schedule)
            score_update = score_update + desire_score


        return score_update


    
    #Randomly generate initial population
    def initialize(self, population_size,tasks,work_break_ratio, total_items):
        #print( "in initialize")
        self.tasks = tasks
        pop = []
        counter = 0
        while (counter < population_size):
            ind = self.make_individual(tasks, work_break_ratio, total_items)
            ind_fitness = self.fitness(ind,work_break_ratio)
            pop.append((ind,ind_fitness))
            #print("finished making one individual")
            counter = counter + 1
            
        return pop


    def make_individual(self,tasks,work_break_ratio,total_items):
        #print("making individual")
        counter = 0
        chromosome = []
        while (counter < total_items):
            #creates a random number between 0 and 1
            rand = random.uniform(0,1)
            if (rand < work_break_ratio):
                chromosome.append(random.choice(list(tasks)))
            else:
                chromosome.append("break")
            
            counter = counter + 1
                
        return chromosome
                
        
            
    def mate_and_mutate(self,parent_one, parent_two,cross_over_prob, mutation_prob,total_items):
        cross_num = (random.uniform(0,1)) 
        mutation_num = (random.uniform(0,1)) 
        children = [parent_one, parent_two]
        
        if (cross_num <= cross_over_prob):
            children = self.cross_over(parent_one,parent_two,total_items)
            
        if (mutation_num <= mutation_prob):
            children = self.mutate(children,total_items)
            
        return children
        
        
        
    def cross_over (self,first_parent,second_parent,total_items):
        cross_point = (int)(random.uniform(0,total_items)) 
        print("CROSS POINT")
        print(cross_point)
        first_child = []
        second_child = []
        
        first_child.extend(first_parent[:cross_point])
        second_child.extend(second_parent[:cross_point])
        first_child.extend(second_parent[cross_point:])
        second_child.extend(first_parent[cross_point:])
        
        return [first_child,second_child]
        
    #Don't know how this should be yet
    def mutate (self,offspring_list,total_items):
        num_mutations = (int)(random.uniform(0,4)) 
        for i in range(0,num_mutations):
            for o in offspring_list:
                self.insert_random_task(o,total_items)

        return offspring_list

    def insert_random_task(self,schedule,total_items):
        work_or_break = (random.uniform(0,1)) 
        if (self.wbr < work_or_break):
            random_task = "break"
        else:
            random_task = random.choice(list(self.tasks))

        random_place = (int)(random.uniform(1,total_items - 1)) 
        schedule[random_place] = random_task
        
    def fitness_greater(self,first,second):
        first_fitness = first[1]
        second_fitness = second[1]
        return (first_fitness > second_fitness)

        
    def rank_parents(self, population) :
        while (True):
            swapped = False
            for i in range(0, len(population) - 1):
                if self.fitness_greater(population[i+1], population [i]) :
                    swapped = True
                    temp = population[i]
                    population[i] = population[i+1]
                    population[i+1] = temp
            if (swapped == False):
                break


    def next_generation (self,population, population_size,total_items):
        self.rank_parents(population)
        new_generation = []
   
        for i in range(0, len(population) - 1):
            #print('PRITNING PARENT')
            #print(population[i])
            two_children = self.mate_and_mutate(population[i][0], population[i+1][0],self.cross_over_prob, self.mutation_prob,total_items)

            new_generation.append(two_children[0])
            #print('PRINTING CHILDREN')
            #print(two_children[0])
            if (len(new_generation) == population_size):
                break
            new_generation.append(two_children[1])
            if (len(new_generation) == population_size ):
                break
        
        return new_generation 


    def assess_fitness_of_generation (self, new_generation, work_break_ratio):
        pop = []

        for ind in new_generation:
            ind_fitness = self.fitness(ind,work_break_ratio)
            pop.append((ind,ind_fitness))
            
        return pop

          
        




       