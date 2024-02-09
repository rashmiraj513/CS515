import heapq

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task, priority):
        heapq.heappush(self.tasks, (priority, task))

    def execute_tasks(self):
        while self.tasks:
            priority, task = heapq.heappop(self.tasks)
            print(f"Executing task: {task}, {priority}")
            
# Test the TaskScheduler
if __name__ == "__main__":
    scheduler = TaskScheduler()
    n = int(input("Enter the number of tasks: "))
    for _ in range(n):
        task = input("Enter the task name: ")
        priority = int(input("Enter the task priority: "))
        # Add tasks with priorities
        scheduler.add_task(task, priority)
        print("\n")

    # Execute tasks based on their priorities
    scheduler.execute_tasks()