class Group:
    group_id = 0

    @classmethod
    def autoincrement(cls):
        cls.group_id += 1
        return cls.group_id

    def __init__(self, name):
        self.__id = Group.autoincrement()
        self.name = name

    def get_id(self):
        return self.__id

    def __repr__(self):
        return f"{self.name}"


Group_11M = Group("11М")
Group_22B = Group("22Б")
Group_33R = Group("33Р")
