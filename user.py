class User:
    def __init__(
                self, 
                name : str = "temp", 
                age : int = 18 
        ) -> None:
        self.username = name
        self.age = age

    def __repr__(self) -> str:
        return self.username + "//" + str(self.age)