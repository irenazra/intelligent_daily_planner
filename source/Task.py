class Task:
    """
    A simple class that defines a task 
    """
    def __init__(self,task_name, estimated_completion_time, desire_level, importance, can_divide):
        """
        ------------
         Parameters
        ------------
        task_name : str
                the description of the task
        estimated_completion_time : int
                the estimated completion time for the task in minutes
        desire_level : int 
                a number indicating how much the user is willing to perform this task (10, very eager)
        importance : int
                a number indicating how important this task is (10, very important)
        can_divide : boolean
                can this task be completed in multiple sittings? (True)
                does it need to be completed in one sitting? (False)
        """

        self.name = task_name
        self.ect = estimated_completion_time
        self.desire = desire_level
        self.priority = importance
        self.can_divide = can_divide


