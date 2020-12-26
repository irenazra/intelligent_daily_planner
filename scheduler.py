import Genetic_Algorithms
import Task
import Schedule_UI

class Scheduler:
    def __init__(self,wbr,tasks,time_interval,time_range,cross_over_prob,mutation_prob,pop_size,generations):
        self.work_break_ratio = wbr
        self.tasks = tasks
        self.time_interval = time_interval
        self.total_items = int(time_range / time_interval)
        self.cross_over_prob = cross_over_prob
        self.mutation_prob = mutation_prob
        self.genetic_algorithms = Genetic_Algorithms.Genetic_Algorithms(self.time_interval,self.cross_over_prob,self.mutation_prob,self.work_break_ratio)
        self.population_size = pop_size
        self.num_generations = generations
    

    def create_schedule (self):
   
        initial_population = self.genetic_algorithms.initialize(self.population_size,self.tasks,self.work_break_ratio, self.total_items)

        current_population = initial_population
        counter = self.num_generations
        while (counter > 0):

            next_gen = self.genetic_algorithms.next_generation (current_population, self.population_size,self.total_items)
            next_gen_assessed = self.genetic_algorithms.assess_fitness_of_generation (next_gen, self.work_break_ratio)
            current_population = next_gen_assessed
            counter = counter - 1

        return current_population


def test():
    print("running main")
    tasks = set()
    #(task_name, estimated_completion_time, desire_level, importance)
    task1 = Task.Task("Do CS homework", 60, 3, 10, True)
    task2 = Task.Task("Exercise", 40, 8, 1, True)
    task3 = Task.Task("Meditate", 20, 2, 9, True)
    task4 = Task.Task("Finish job applications", 60, 9, 3, True)
    task5 = Task.Task("Clean the house", 60, 3, 8, True)
    task6 = Task.Task("Cook", 40, 8, 1, True)
    task7 = Task.Task("Run", 60, 2, 10, False)
    task8 = Task.Task("Feed the cat", 20, 6, 7, True)
    tasks.add(task1)
    tasks.add(task2)
    tasks.add(task3)
    tasks.add(task4)
    tasks.add(task5)
    tasks.add(task6)
    tasks.add(task7)
    tasks.add(task8)
    #wbr,tasks,time_interval,time_range,cross_over_prob,mutation_prob,pop_size,generations
    wbr = 0.7
    start_hour = 8 
    start_min = 20 
    time_interval = 20 #mins
    time_range = 400 #mins
    cross_over_prob = 0.8
    mutation_prob = 0.7
    pop_size = 100
    generations = 10
    my_schedule = Scheduler(wbr,tasks,time_interval,time_range,cross_over_prob,mutation_prob,pop_size,generations)
    schedule = my_schedule.create_schedule()
    UI = Schedule_UI.Schedule_UI(schedule,time_interval,start_hour,start_min)
    UI.loop(5)


if __name__ == "__main__":
    test()