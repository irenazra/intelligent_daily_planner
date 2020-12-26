import tkinter as tk
from tkinter import ttk
import tkinter.font
import Task
import scheduler
import Schedule_UI
import random

class User_Input_Interface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("The Intelligent Scheduler!")
        self.tasks = set()
        self.font = tk.font.Font(family="Lucida Grande", size=20)
        self.color_set = self.define_task_colors()
        self.window['bg'] = "bisque"
    

    def enter_task_UI_frame(self):

        enter_task_frame = tk.Frame(master = self.window, width=600, height=100, bg="bisque")
        enter_task_label =  tk.Label(master= enter_task_frame, text="Enter a task!", bg="bisque", font = self.font)
        enter_task_label.pack()

        name_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="bisque")
        name_label = tk.Label(master= name_frame, text="Description", bg="salmon")
        name_entry_widget = tk.Entry(master = name_frame)
        self.name_entry_widget = name_entry_widget
        name_label.pack()
        name_entry_widget.pack()
        name_frame.pack(side = tk.LEFT)

        time_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="bisque")
        time_label = tk.Label(master= time_frame, text="Time Required", bg="salmon")
        time_values = [20,40,60,80,100,120,140,160,180,200,220,240,260,280,300]
        time_combobox = ttk.Combobox(master = time_frame, values = time_values,width=4)
        self.time_combobox = time_combobox
        time_label.pack()
        time_combobox.pack()
        time_frame.pack(side = tk.LEFT)

        desire_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="bisque")
        desire_label = tk.Label(master= desire_frame, text="Enjoyment Rate", bg="salmon")
        desire_values = [1,2,3,4,5,6,7,8,9,10]
        desire_combobox = ttk.Combobox(master = desire_frame, values = desire_values,width=4)
        self.desire_combobox = desire_combobox
        desire_label.pack()
        desire_combobox.pack()
        desire_frame.pack(side = tk.LEFT,padx=10)

        importance_frame = tk.Frame(master = enter_task_frame, width=100, height=100, bg="bisque")
        importance_label = tk.Label(master= importance_frame, text="Importance/Urgence", bg="salmon")
        importance_combobox = ttk.Combobox(master = importance_frame, values = desire_values,width=4)
        self.importance_combobox = importance_combobox
        importance_label.pack()
        importance_combobox.pack()
        importance_frame.pack(side = tk.LEFT,padx=10)

        self.check_value = tk.BooleanVar()
        dividable_checkbutton = tk.Checkbutton(master = enter_task_frame, text = "Needs to be completed in one sitting",bg="salmon",var=self.check_value,onvalue= False, 
                            offvalue=True)
        dividable_checkbutton.pack(side = tk.LEFT)
        self.dividable_checkbutton = dividable_checkbutton

        add_button = tk.Button(master = enter_task_frame, command = self.add_task, text = "Add Task",bg="bisque")
        add_button.pack()

        enter_task_frame.pack()

    def show_entered_tasks(self):
        tasks_frame= tk.Frame(master = self.window, width=630, height=25,bg="bisque")
        tasks_frame.pack()
        self.tasks_frame = tasks_frame

    def add_scheduler_options(self):
        options_frame= tk.Frame(master = self.window, width=500, height=100,bg="bisque")
        options_frame.pack()
        self.options_frame = options_frame

        options_label = tk.Label(master= options_frame, text="Scheduler Options",font = self.font,bg="bisque")
        options_label.pack()



        time_interval_frame = tk.Frame(master = options_frame, width=100, height=100, bg="bisque")
        time_interval_label = tk.Label(master= time_interval_frame, text="Time Interval", bg="salmon")
        time_interval_values = [20,40,60,80,100,120]
        time_interval_combobox = ttk.Combobox(master = time_interval_frame, values = time_interval_values, width=4)
        self.time_interval_combobox = time_interval_combobox
        time_interval_label.pack()
        time_interval_combobox.pack()
        time_interval_frame.pack(side = tk.LEFT)



        wbr_frame = tk.Frame(master = options_frame, width=100, height=100, bg="bisque")
        wbr_label = tk.Label(master= wbr_frame, text="Work ratio of schedule", bg="salmon")
        wbr_values = [1,0.9,0.8,0.7,0.6,0.5,0.4]
        wbr_combobox = ttk.Combobox(master = wbr_frame, values = wbr_values,width=4)
        self.wbr_combobox = wbr_combobox
        wbr_label.pack()
        wbr_combobox.pack()
        wbr_frame.pack(side = tk.LEFT,padx=10)

        start_frame = tk.Frame(master = options_frame, width=100, height=100, bg="bisque")
        start_label = tk.Label(master= start_frame, text="Start time", bg="salmon")
        min_values = [0,10,20,30,40,50]
        hour_values = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
        start_min_combobox = ttk.Combobox(master = start_frame, values = min_values,width=2)
        start_hour_combobox = ttk.Combobox(master = start_frame, values = hour_values,width=2)
        self.start_min_combobox = start_min_combobox 
        self.start_hour_combobox = start_hour_combobox 
        start_label.pack()
        start_hour_combobox.pack(side =tk.LEFT)
        start_min_combobox.pack(side =tk.LEFT)
        start_frame.pack(side = tk.LEFT)


        end_frame = tk.Frame(master = options_frame, width=100, height=100, bg="bisque")
        end_label = tk.Label(master= end_frame, text="End time", bg="salmon")
        end_min_combobox = ttk.Combobox(master = end_frame, values = min_values,width=2)
        end_hour_combobox = ttk.Combobox(master = end_frame, values = hour_values,width=2)
        self.end_min_combobox =end_min_combobox 
        self.end_hour_combobox = end_hour_combobox 
        end_label.pack()
        end_hour_combobox.pack(side =tk.LEFT)
        end_min_combobox.pack(side =tk.LEFT)
        end_frame.pack(side = tk.LEFT)





        create_schedule_button = tk.Button(master = options_frame, command = self.create_scheduler, text = "Create Schedule!",bg="pale green")
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
        print("TIME RANGE IS:   ")
        print(time_range)


        cross_over_prob = 0.8
        mutation_prob = 0.7
        pop_size = 200
        generations = 10
        

        #create a scheduler 
        my_scheduler =scheduler.Scheduler(wbr,self.tasks,time_interval,time_range,cross_over_prob,mutation_prob,pop_size,generations)
        schedules = my_scheduler.create_schedule()
        UI = Schedule_UI.Schedule_UI(schedules,time_interval,start_hour,start_min)
        UI.loop(5)

       

    def give_minute_difference(self,hour1,min1,hour2,min2):

        hour_diff = hour2 - hour1
        min_diff = min2 - min1

        time_range = (hour_diff * 60 ) + min_diff

        if (time_range < 0):
            until_midnight = self.give_minute_difference(hour1,min1,24,0)
            after_midnight = self.give_minute_difference(0,0,hour2,min2)
            return until_midnight + after_midnight


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

        random_color = random.choice(list(self.color_set))

        task_label = tk.Label(master= self.tasks_frame, text=task.name,bg=random_color,justify=tk.LEFT)
        task_label.grid()
        

    def define_task_colors(self):
        color_set = set()
        color_set.add("pink")
        color_set.add("gold")
        color_set.add("khaki")
        color_set.add("lavender")
        color_set.add("orange")
        color_set.add("peach puff")
        color_set.add("green yellow")
        color_set.add("yellow")
        color_set.add("violet red")
        color_set.add("RoyalBlue1")
        color_set.add("SkyBlue1")
        color_set.add("green2")
        color_set.add("purple1")
        color_set.add("deep sky blue")
        color_set.add("red")
        color_set.add("gray73")
        color_set.add("sandybrown")
        color_set.add("aquamarine")
        return color_set







    




    def loop(self):
        self.enter_task_UI_frame()
        self.show_entered_tasks()
        self.add_scheduler_options()
        self.window.mainloop()

if __name__ == "__main__":
    test = User_Input_Interface()
    test.loop()





