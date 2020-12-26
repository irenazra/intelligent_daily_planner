import tkinter as tk
from tkinter import ttk
import Task
import scheduler
import Schedule_UI

class User_Input_Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.tasks = set()

    def enter_task_UI_frame(self):
        enter_task_frame = tk.Frame(master = self.window, width=600, height=100, bg="turquoise2")
        enter_task_label =  tk.Label(master= enter_task_frame, text="Enter a task!", bg="turquoise2")
        enter_task_label.pack()

        name_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="turquoise2")
        name_label = tk.Label(master= name_frame, text="Description of the task", bg="turquoise2")
        name_entry_widget = tk.Entry(master = name_frame)
        self.name_entry_widget = name_entry_widget
        name_label.pack()
        name_entry_widget.pack()
        name_frame.pack(side = tk.LEFT)

        time_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="turquoise2")
        time_label = tk.Label(master= time_frame, text="How much time will this task take?", bg="turquoise2")
        time_values = [20,40,60,80,100,120,140,160,180,200,220,240,260,280,300]
        time_combobox = ttk.Combobox(master = time_frame, values = time_values)
        self.time_combobox = time_combobox
        time_label.pack()
        time_combobox.pack()
        time_frame.pack(side = tk.LEFT)

        desire_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="turquoise2")
        desire_label = tk.Label(master= desire_frame, text="How much do you enjoy this task?", bg="turquoise2")
        desire_values = [1,2,3,4,5,6,7,8,9,10]
        desire_combobox = ttk.Combobox(master = desire_frame, values = desire_values)
        self.desire_combobox = desire_combobox
        desire_label.pack()
        desire_combobox.pack()
        desire_frame.pack(side = tk.LEFT)

        importance_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="turquoise2")
        importance_label = tk.Label(master= importance_frame, text="How important/urgent is this task?", bg="turquoise2")
        importance_combobox = ttk.Combobox(master = importance_frame, values = desire_values)
        self.importance_combobox = importance_combobox
        importance_label.pack()
        importance_combobox.pack()
        importance_frame.pack(side = tk.LEFT)

        self.check_value = tk.BooleanVar()
        dividable_checkbutton = tk.Checkbutton(master = enter_task_frame, text = "This task needs to be completed in one sitting",bg="turquoise2",var=self.check_value,onvalue= False, 
                            offvalue=True)
        dividable_checkbutton.pack(side = tk.LEFT)
        self.dividable_checkbutton = dividable_checkbutton

        add_button = tk.Button(master = enter_task_frame, command = self.add_task, text = "Add Task")
        add_button.pack(side = tk.LEFT)

        enter_task_frame.pack()

    def show_entered_tasks(self):
        tasks_frame= tk.Frame(master = self.window, width=630, height=100)


        tasks_frame.pack(side = tk.LEFT)
        self.tasks_frame = tasks_frame

    def add_scheduler_options(self):
        options_frame= tk.Frame(master = self.window, width=630, height=100)
        options_frame.pack()
        self.options_frame = options_frame

        options_label = tk.Label(master= options_frame, text="Scheduler Options")
        options_label.pack()



        time_interval_frame = tk.Frame(master = options_frame, width=100, height=100, bg="turquoise2")
        time_interval_label = tk.Label(master= time_interval_frame, text="Time interval in the schedule", bg="turquoise2")
        time_interval_values = [20,40,60,80,100,120]
        time_interval_combobox = ttk.Combobox(master = time_interval_frame, values = time_interval_values)
        self.time_interval_combobox = time_interval_combobox
        time_interval_label.pack()
        time_interval_combobox.pack()
        time_interval_frame.pack(side = tk.LEFT)



        wbr_frame = tk.Frame(master = options_frame, width=100, height=100, bg="turquoise2")
        wbr_label = tk.Label(master= wbr_frame, text="What portion of the schedule should be work?", bg="turquoise2")
        wbr_values = [1,0.9,0.8,0.7,0.6,0.5,0.4]
        wbr_combobox = ttk.Combobox(master = wbr_frame, values = wbr_values)
        self.wbr_combobox = wbr_combobox
        wbr_label.pack()
        wbr_combobox.pack()
        wbr_frame.pack(side = tk.LEFT)

        start_frame = tk.Frame(master = options_frame, width=100, height=100, bg="turquoise2")
        start_label = tk.Label(master= start_frame, text="Start time", bg="turquoise2")
        min_values = [0,10,20,30,40,50]
        hour_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        start_min_combobox = ttk.Combobox(master = start_frame, values = min_values)
        start_hour_combobox = ttk.Combobox(master = start_frame, values = hour_values)
        self.start_min_combobox = start_min_combobox 
        self.start_hour_combobox = start_hour_combobox 
        start_label.pack()
        start_hour_combobox.pack(side =tk.LEFT)
        start_min_combobox.pack(side =tk.LEFT)
        start_frame.pack(side = tk.LEFT)


        end_frame = tk.Frame(master = options_frame, width=100, height=100, bg="turquoise2")
        end_label = tk.Label(master= end_frame, text="End time", bg="turquoise2")
        end_min_combobox = ttk.Combobox(master = end_frame, values = min_values)
        end_hour_combobox = ttk.Combobox(master = end_frame, values = hour_values)
        self.end_min_combobox =end_min_combobox 
        self.end_hour_combobox = end_hour_combobox 
        end_label.pack()
        end_hour_combobox.pack(side =tk.LEFT)
        end_min_combobox.pack(side =tk.LEFT)
        end_frame.pack(side = tk.LEFT)





        create_schedule_button = tk.Button(master = self.window, command = self.create_scheduler, text = "Create Schedule!")
        create_schedule_button.pack()

    def create_scheduler(self):
        # get information from the scheduler option widgets
        time_interval = (int) (self.time_interval_combobox.get())
        wbr = (float) (self.wbr_combobox.get())
        start_hour = (int)(self.start_hour_combobox.get())
        start_min = (int)(self.start_min_combobox.get())
        end_hour =(int)(self.end_hour_combobox.get())
        end_min =(int) (self.end_min_combobox.get())

        time_range = self.give_minute_difference(start_hour,start_min,end_hour,end_min)


        cross_over_prob = 0.8
        mutation_prob = 0.7
        pop_size = 100
        generations = 10
        

        #create a scheduler 
        my_scheduler =scheduler.Scheduler(wbr,self.tasks,time_interval,time_range,cross_over_prob,mutation_prob,pop_size,generations)
        schedules = my_scheduler.create_schedule()
        UI = Schedule_UI.Schedule_UI(schedules,time_interval,start_hour)
        UI.loop(10)

       

    def give_minute_difference(self,hour1,min1,hour2,min2):
        #print(hour1)
        #print(min1)
        #print(hour2)
        #print(min2)
        hour_diff = hour2 - hour1
        #print(hour_diff)
        min_diff = min2 - min1
        #print(min_diff)

        return (hour_diff * 60 ) + min_diff







    #TODO Handle the cases where the user input does not make sense, have default values etc.
    def add_task(self):
        task_description = self.name_entry_widget.get()
        est_comp_time = (int) (self.time_combobox.get())
        desire_level = (int)(self.desire_combobox.get())
        importance =(int) (self.importance_combobox.get())
        dividable = self.check_value.get()


        task = Task.Task(task_description, est_comp_time, desire_level, importance, dividable)
        self.tasks.add(task)

        task_frame= tk.Frame(master = self.tasks_frame, width=300, height=1, bg="pink")
        task_label = tk.Label(master= task_frame, text=task.name,bg="pink",justify=tk.LEFT)
        task_label.grid()
        task_frame.pack()






    




    def loop(self):
        self.add_scheduler_options()
        self.enter_task_UI_frame()
        self.show_entered_tasks()
        self.window.mainloop()

if __name__ == "__main__":
    test = User_Input_Interface()
    test.loop()





