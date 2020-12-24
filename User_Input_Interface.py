import tkinter as tk
from tkinter import ttk
import Task
class User_Input_Interface:
    def __init__(self):
        self.window = tk.Tk()

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

    #TODO Handle the cases where the user input does not make sense, have default values etc.
    def add_task(self):
        task_description = self.name_entry_widget.get()
        est_comp_time = self.time_combobox.get() 
        desire_level = self.desire_combobox.get() 
        importance = self.importance_combobox.get() 
        dividable = self.check_value.get()

        task = Task.Task(task_description, est_comp_time, desire_level, importance, dividable)
        print(task)
        print(task.can_divide)
        print(task.name)
        print(task.ect)
        print(task.desire)
        print(task.priority)









    def loop(self):
        self.enter_task_UI_frame()
        self.window.mainloop()

if __name__ == "__main__":
    test = User_Input_Interface()
    test.loop()





