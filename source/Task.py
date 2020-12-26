#The task class
class Task:
    def __init__(self,task_name, estimated_completion_time, desire_level, importance, can_divide):
        self.name = task_name
        self.ect = estimated_completion_time
        self.desire = desire_level
        self.priority = importance
        self.can_divide = can_divide



        #you can add urgence!