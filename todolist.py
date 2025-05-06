class Todo:
    DONE = 'X'
    NOT_DONE = ' '

    def __init__(self, title):
        self._title = title
        self.done = False

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return (self.title == other.title and 
                self.done == other.done)
    
    def __str__(self):
        return f'[{self.mark}] {self.title}'

    @property
    def mark(self):
        return Todo.DONE if self.done else Todo.NOT_DONE

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, done):
        self._done = done

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    def __len__(self):
        return len(self._todos)

    def __str__(self):
        output_lines = [f"---- {self.title} ----"]
        output_lines += [str(todo) for todo in self._todos]
        return '\n'.join(output_lines)

    @property
    def title(self):
        return self._title
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add 'Todo' objects")
        
        self._todos.append(todo)

    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return self._todos[:]
    
    def todo_at(self, idx):
        return self._todos[idx]

    def mark_done_at(self, idx):
        self.todo_at(idx).done = True
    
    def mark_undone_at(self, idx):
        self.todo_at(idx).done = False
    
    def  mark_all_done(self):    
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False
        
        self.each(mark_undone)

    def all_done(self):
        return all([todo.done for todo in self._todos])
    
    def remove_at(self, idx):
        del self._todos[idx]
    
    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        filtered_list = TodoList(self.title)
        for todo in filter(callback, self._todos):
            filtered_list.add(todo)
        
        return filtered_list

    def find_by_title(self, title):
        found = self.select(lambda todo: todo.title == title)
        return found.todo_at(0)

    def done_todos(self):
        return self.select(lambda todo: todo.done)
    
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        found = self.find_by_title(title)
        found.done = True