import tkinter as tk

class Schedule_UI:
    def __init__(self,schedule_list):
        self.window = tk.Tk()
        self.schedule_list = schedule_list

    def print_best_schedule(self):
        show_schedule(self.schedule_list[0])

    def show_schedule(self, one_schedule):

        self.schedule_list.reverse()
        cleaned_schedule = self.clean_fitness_info(one_schedule)


        for i in range(0,len(cleaned_schedule)):
            #rand_color = (int)(random.uniform(0,3)) 
            task = cleaned_schedule[i]
            print("PRINTING TASK ")
            print (task)
            description = " "
            if ( task == "break"):
                description = "break"
            else:
                description = task.name

            frame = tk.Frame(master=self.window, width=100, height=100, bg="red")
            label = tk.Label(master=frame, text=description)
            label.pack()
            frame.pack()



    def clean_fitness_info (self, reversed_schedule):
        cleaned = []

        for i in reversed_schedule:
            cleaned.append(i[0])

        return cleaned


    def loop (self):
        self.print_best_schedule
   
        self.window.mainloop()


#if __name__ == "__main__":
#    UI = Schedule_UI()

    

    










