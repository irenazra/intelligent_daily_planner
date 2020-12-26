import tkinter as tk
import pandas as pd

class Schedule_UI:
    """
    Creates the UI representation of one schedule
    ---------
     Methods
    ---------

    loop (num_schedules):
            Creates and displays the UI representation of the best num_schedules schedules
        
    """

    def __init__(self,schedule_list,time_interval,start_hour,start_min):
        """

        ------------
         Parameters
        ------------

        window : 
            the pop up window that contains the schedules
        schedule_list : list
            contains all the schedules in order of fitness
        time_interval : int
            the intervals in the schedule that define a period over which a specific task is to be performed
        start_hour: int
            the hour value of the starting time
        start_min: int
            the minutes value of the starting time

        """


        self.window = tk.Tk()
        self.window.title("Best Schedules!")

        self.schedule_list = schedule_list
        self.time_interval = time_interval
        self.start_hour = start_hour
        self.start_min = start_min


    #Displays num best schedules
    def print_best_schedule(self,num):

        for i in range (0,num):
            self.show_schedule(self.schedule_list[i],i)

    #displays one schedule 
    def show_schedule(self, one_schedule,index):

        #Creates the main frame of the schedule and the its label
        schedule_frame = tk.Frame(master = self.window,width = 200, height = 700)
        title_frame = tk.Frame(master = schedule_frame, width=100, height=100, bg="turquoise2")
        title_label = tk.Label(master= title_frame, text="Schedule", bg="turquoise2")
        title_label.pack()
        title_frame.pack(fill=tk.X)


        #keeps track of the start time of intervals
        hour_min_pair = (self.start_hour,self.start_min)

        for i in range(0,len(one_schedule[0])):
            
            #save the starting time as a string
            start_time_string = self.get_time_string(hour_min_pair[0],hour_min_pair[1])

            #update to the starting time of the next interval
            hour_min_pair = self.add_interval_to_time(hour_min_pair[0],hour_min_pair[1])

            #get task from the (task, fitness) pair
            task = one_schedule[0][i]

            #Determine the description of this interval
            if ( task == "break"):
                description = "break"
                name_frame_color = "pale green"
            else:
                description = task.name
                name_frame_color = "salmon"

            #create the frame of this interval
            frame = tk.Frame(master=schedule_frame, width=100, height=100, bg="bisque")
            
            #create time and name frames
            time_frame = tk.Frame(master = frame, width=50, height=100, bg="salmon")
            name_frame = tk.Frame(master = frame, width=50, height=100, bg= name_frame_color)

            #add labels indicating the starting time of the interval and the description of the interval
            time_label = tk.Label(master=time_frame, text=start_time_string, bg="bisque")
            name_label = tk.Label(master=name_frame, text=description, bg=name_frame_color)

            #Pack all the widgets
            time_label.pack()
            name_label.pack()


            time_frame.pack(side = tk.LEFT)
            name_frame.pack(side = tk.LEFT)

            time_label.pack()
            name_label.pack()
            frame.pack(fill=tk.X)

            schedule_frame.pack(side = tk.LEFT)

        #Create a save button for each schedule
        save_button = tk.Button( master = schedule_frame, text ="Save Schedule",command = lambda: self.save_schedule(index))
        save_button.pack()

    #Creates a dataframe from the chosen schedule, and saves this schedule in the root directory
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
        df.to_csv('schedule.csv',index=False)

    #prints time
    def get_time_string(self, hour,min):
        min_string = str(min)
        if (len(min_string) == 1):
            min_string = "0" + min_string
        return str(hour) + ":" + min_string

    #adds schedule's interval to a specific time
    def add_interval_to_time(self,hour,min):
        new_min = min + self.time_interval

        if (new_min > 60):
            added_hours = new_min // 60
            new_min = new_min - (added_hours * 60)
            total_hours = (hour + added_hours) % 24
            return (total_hours,new_min)

        else:
            return (hour,new_min)

    
    def loop (self,num_schedules):
        
        """
        Creates the UI elements to display the best num_schedules schedules
        Starts the mainloop of the window

        ------------
        Parameters
        ------------

        num_schedules : int
                The number of schedules to print

        """

        self.print_best_schedule(num_schedules)
        self.window.mainloop()

    

    










