class Task:

    def __init__(self, task_name, task_description, task_date, subtasks=None):
        self.task_name = task_name
        self.task_description = task_description
        self.task_date = task_date
        self.subtasks = subtasks if subtasks is not None else []


    def info(self):
        print(f"Task Name: {self.task_name}\nTask Description: {self.task_description}\nTask Date: {self.task_date}")
        if self.subtasks:
            print("--- Subtasks ---")
            for subtask in self.subtasks:
                print(subtask)



task1 = Task(
    "Python basics",
    "In this task, I will mostly revising basic concepts of python",
    "13-08-2025")

task2 = Task(
    "Python basics",
    "In this task, I will mostly revise basic concepts of Python",
    "13-08-2025",
    ["Variables and Data Types", "Loops", "Functions", "File Handling"]
)

task2.info()