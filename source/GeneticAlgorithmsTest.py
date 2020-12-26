import Task
import unittest
import Genetic_Algorithms


class GeneticAlgorithmsTest(unittest.TestCase):
    """
    A unittest class that can be used to test and debug the functions in Genetic_Algorithms.py file

    """

    work_break_ratio = 0.8
    total_items = 4
    tasks = set()
    task1 = Task.Task("1", 20, 10, 10)
    task2 = Task.Task("2", 20, 8, 1)
    task3 = Task.Task("3", 20, 2, 9)
    task4 = Task.Task("4", 20, 6, 3)
    tasks.add(task1)
    tasks.add(task2)
    tasks.add(task3)
    tasks.add(task4)

    def test_make_individual(self): 
        scheduler = Genetic_Algorithms.Genetic_Algorithms()
        draft_schedule = scheduler.make_individual(GeneticAlgorithmsTest.tasks,0.8,4)
        self.assertEqual(len(draft_schedule), 4)
        #print(draft_schedule)

    def test_initialize(self):
        scheduler = Genetic_Algorithms.Genetic_Algorithms()
        population_list = scheduler.initialize(2,GeneticAlgorithmsTest.tasks,0.8, 4)
        #print ("population list is:")
        #print(population_list)

    def test_rank_parents(self):
        scheduler = Genetic_Algorithms.Genetic_Algorithms()
        population_list = scheduler.initialize(2,GeneticAlgorithmsTest.tasks,0.8, 4)
        #print ("population list is:")
        #print(population_list)
        scheduler.rank_parents(population_list)
        #print ("sorted population list is:")
        #print(population_list)

        population_list = scheduler.initialize(10,GeneticAlgorithmsTest.tasks,0.8, 4)
        #print ("population list is:")
        #print(population_list)
        scheduler.rank_parents(population_list)
        #print ("sorted population list is:")
        #print(population_list)

    def test_next_generation(self):
        scheduler = Genetic_Algorithms.Genetic_Algorithms()
        population_list = scheduler.initialize(2,GeneticAlgorithmsTest.tasks,0.8, 4)
        next_gen = scheduler.next_generation(population_list,2,4)

        print("population list")
        print(population_list)
        for i in population_list:
            print("individual ")
            for j in i[0]:
                if j == "break":
                    print("break")
                else:
                    print(j.name)

        for k in next_gen:
            print("individual ")
            for l in k:
                if l == "break":
                    print("break")
                else:
                    print(l.name)



if __name__ == '__main__':
    unittest.main()

