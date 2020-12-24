import tkinter as tk

class Schedule_UI:
    def __init__(self,schedule_list,time_interval,start_time):
        self.window = tk.Tk()
        self.window.title("Best Schedules!")
        self.schedule_list = schedule_list
        self.time_interval = time_interval
        self.start_time = start_time
        

    def print_best_schedule(self,num):
        for i in range (0,num):
            self.show_schedule(self.schedule_list[i])
        
        

    def show_schedule(self, one_schedule):
        schedule_frame = tk.Frame(master = self.window,width = 200, height = 700)
        title_frame = tk.Frame(master = schedule_frame, width=100, height=100, bg="turquoise2")
        title_label = tk.Label(master= title_frame, text="Schedule", bg="turquoise2")
        title_label.pack()
        title_frame.pack(fill=tk.X)

        
        

        one_schedule[0].reverse()
        #cleaned_schedule = self.clean_fitness_info(schedule)
        item_counter = 0


        for i in range(0,len(one_schedule[0])):
            #print("PRINTING SCHEDULE")
            #print(one_schedule[0])

            #print("DO WE ENTER HERE?")
            #rand_color = (int)(random.uniform(0,3)) 
            task = one_schedule[0][i]
            
            #print("PRINTING TASK ")
            #print (task)
            description = " "
            if ( task == "break"):
                description = "break"
                name_frame_color = "pale green"
            else:
                description = task.name
                name_frame_color = "salmon"

            frame = tk.Frame(master=schedule_frame, width=100, height=100, bg="bisque")
            

            time_frame = tk.Frame(master = frame, width=50, height=100, bg="salmon")
            name_frame = tk.Frame(master = frame, width=50, height=100, bg= name_frame_color)

            time_label = tk.Label(master=time_frame, text=str(item_counter), bg="bisque")
            name_label = tk.Label(master=name_frame, text=description, bg=name_frame_color)

            time_label.pack()
            name_label.pack()

            #time_frame.grid(column=0, row=0)
            #name_frame.grid(column=1, row=0)

            time_frame.pack(side = tk.LEFT)
            name_frame.pack(side = tk.LEFT)

            time_label.pack()
            name_label.pack()
            frame.pack(fill=tk.X)

            item_counter = item_counter + 1
            schedule_frame.pack(side = tk.LEFT)
        

    def clean_fitness_info (self, reversed_schedule):
        cleaned = []

        for i in reversed_schedule:
            cleaned.append(i[0])

        return cleaned


    def loop (self,num_schedules):
        self.print_best_schedule(num_schedules)
        self.window.mainloop()


#if __name__ == "__main__":
#    UI = Schedule_UI()

    

    










