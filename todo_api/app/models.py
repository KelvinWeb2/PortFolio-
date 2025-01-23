# models.py - Defines the structure of Todo items

# Temporary in-memory storage for Todos (simulating a database)
todos = []

# Todo data structure
class Todo:
    def __init__(self, title, description):
        self.id = len(todos) + 1  # Simple unique ID generation
        self.title = title
        self.description = description
        self.completed = False

    def to_dict(self):
        """ Convert Todo object to dictionary """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "completed": self.completed
        }
