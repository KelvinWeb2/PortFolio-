class Todo:
    def __init__(self, title, description):
        self.id = None  # ID will be assigned dynamically
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }

# Initialize an in-memory list of todos
todos = [
    Todo("Buy groceries", "Milk, eggs, bread"),
    Todo("Learn Flask", "Complete Flask Todo API project")
]

# Assign IDs to todos
for idx, todo in enumerate(todos, start=1):
    todo.id = idx
