from collections import deque

"""
Create Task list with deque using append and
"""


class Todolist:
    def __init__(self, tasklist: list):
        self.tasks = deque(tasklist)

    def adding(self, tasks_list, priority=False):
        if priority == True:
            self.tasks.extendleft(tasks_list)
        else:
            self.tasks.extend(tasks_list)

    def printing(self):
        print(f"The tasks are {', '.join(self.tasks)}")

    def completing(self, task):
        for tasks in task:
            self.tasks.remove(tasks)
        print(f"Finished task: {', '.join(task)}")


def main():
    # add code here
    tasks_list = Todolist(["HW", "Bunny Stream"])
    tasks_list.adding(["Themo FE"])
    tasks_list.adding(["Hackerrank"], priority=True)
    tasks_list.printing()
    tasks_list.completing(["Bunny Stream", "Hackerrank"])
    tasks_list.printing()
    return


if __name__ == "__main__":
    main()
