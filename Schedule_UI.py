import tkinter as tk
import pandas as pd

class Schedule_UI:
    def __init__(self,schedule_list,time_interval,start_hour,start_min):
        self.window = tk.Tk()
        self.window.title("Best Schedules!")
        self.schedule_list = schedule_list
        self.time_interval = time_interval
        self.start_hour = start_hour
        self.start_min = start_min



    def print_best_schedule(self,num):
        for i in range (0,num):
            self.show_schedule(self.schedule_list[i],i)


    def show_schedule(self, one_schedule,index):
        schedule_frame = tk.Frame(master = self.window,width = 200, height = 700)
        title_frame = tk.Frame(master = schedule_frame, width=100, height=100, bg="turquoise2")
        title_label = tk.Label(master= title_frame, text="Schedule", bg="turquoise2")
        title_label.pack()
        title_frame.pack(fill=tk.X)


        hour_min_pair = (self.start_hour,self.start_min)


        for i in range(0,len(one_schedule[0])):

            start_time_string = self.get_time_string(hour_min_pair[0],hour_min_pair[1])
            hour_min_pair = self.add_interval_to_time(hour_min_pair[0],hour_min_pair[1])

            task = one_schedule[0][i]

            if ( task == "break"):
                description = "break"
                name_frame_color = "pale green"
            else:
                description = task.name
                name_frame_color = "salmon"

            

            frame = tk.Frame(master=schedule_frame, width=100, height=100, bg="bisque")
            

            time_frame = tk.Frame(master = frame, width=50, height=100, bg="salmon")
            name_frame = tk.Frame(master = frame, width=50, height=100, bg= name_frame_color)

            time_label = tk.Label(master=time_frame, text=start_time_string, bg="bisque")
            name_label = tk.Label(master=name_frame, text=description, bg=name_frame_color)

            time_label.pack()
            name_label.pack()


            time_frame.pack(side = tk.LEFT)
            name_frame.pack(side = tk.LEFT)

            time_label.pack()
            name_label.pack()
            frame.pack(fill=tk.X)

            
            schedule_frame.pack(side = tk.LEFT)

        save_button = tk.Button( master = schedule_frame, text ="Save Schedule",command = lambda: self.save_schedule(index))
        save_button.pack()

    def save_schedule(self,index):
        chosen_schedule = self.schedule_list[index][0]

        for i,e in enumerate(chosen_schedule):
            if (not isinstance(e, str)):
                chosen_schedule[i] = e.name
        
        time_list = []
        hour_min_pair = (self.start_hour,self.start_min)


        for i in range(0,len(chosen_schedule)):
            start_time_string = self.get_time_string(hour_min_pair[0],hour_min_pair[1])
            hour_min_pair = self.add_interval_to_time(hour_min_pair[0],hour_min_pair[1])
            time_list.append(start_time_string)

        d = {'Time': time_list,'Task': chosen_schedule}

        df = pd.DataFrame(d)
        print(df)
        df.to_csv('schedule.csv',index=False)

    def get_time_string(self, hour,min):
        return str(hour) + ":" + str(min)

    def add_interval_to_time(self,hour,min):
        new_min = min + self.time_interval

        if (new_min > 60):
            added_hours = new_min // 60
            new_min = new_min - (added_hours * 60)
            total_hours = hour + added_hours
            return (total_hours,new_min)

        else:
            return (hour,new_min)

        








    def loop (self,num_schedules):
        self.print_best_schedule(num_schedules)
        self.window.mainloop()

    

    










