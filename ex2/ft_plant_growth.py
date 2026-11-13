class plants:
    def __init__(self, name, Height, Age):
        self.name = name
        self.Height = Height
        self.Age = Age

    def grow(self) -> none:
        self.Height += 1
        self.Age += 1