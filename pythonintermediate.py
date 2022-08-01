class ClubMembers:
    def __init__(self, name, birthday, age, Ffood, goal):
        self.name = name
        self.birthday = birthday
        self.age = age
        self.Ffood = Ffood
        self.goal = goal

    def display1(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Ffood: ", self.Ffood)
        print("Goal", self.goal)

class ClubOfficers(ClubMembers):
    def __init__(self, name, birthday, age, Ffood, goal, position):
        self.position = position
        ClubMembers.__init__(self, name, birthday, age, Ffood, goal)

    def display2(self):
        print("Name: ", self.name)
        print("Birthday: ", self.birthday)
        print("Age: ", self.age)
        print("Ffood: ", self.Ffood)
        print("Goal:", self.goal)
        print("Position: ", self.position)

m_1 = ClubMembers("Tom", "January 16", 14, "Ice cream", "To be happy")
o_1 = ClubOfficers("Vera", "June 22", 16, "Beef stroganoff", "to be the world's greatest chef", "Treasurer")

m_1.display1()


