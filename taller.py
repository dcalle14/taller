class Todo:
    def __init__(self, code_id, title, description):
        self.code_id = code_id
        self.title = title
        self.description = description
        self.completed = False
        self.tags = []

    def mark_completed(self):
        self.completed = True

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def __str__(self):
        return f"{self.code_id} - {self.title}"

class TodoBook:
    def __init__(self):
        self.todos = {}

    def add_todo(self, title, description):
        new_id = len(self.todos) + 1
        new_todo = Todo(new_id, title, description)
        self.todos[new_id] = new_todo
        return new_id

    def pending_todos(self):
        return [todo for todo in self.todos.values() if not todo.completed]

    def completed_todos(self):
        return [todo for todo in self.todos.values() if todo.completed]

    def tags_todo_count(self):
        tag_counts = {}
        for todo in self.todos.values():
            for tag in todo.tags:
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        return tag_counts