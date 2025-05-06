class Todo:
    DONE = 'X'
    NOT_DONE = ' '

    def __init__(self, title):
        self._title = title
        self.done = False
    
    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, done):
        self._done = done

    @property
    def mark(self):
        return Todo.DONE if self.done else Todo.NOT_DONE
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented

        return (self.title == other.title and 
                self.done == other.done)
    
    def __str__(self):
        return f'[{self.mark}] {self.title}'