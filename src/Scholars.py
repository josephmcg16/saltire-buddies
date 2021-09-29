"""
Class for a Buddy (Saltire Alumni)

Methods:
    print - prints and returns attributes of the class instance

Attributes:
    name - the Buddy's full name
    uni - selected university of the buddy
    degree - selected degree of the buddy
    interests - list of interests of the buddy
"""


class Buddy:
    def __init__(self, name, uni, degree, interests):
        # make all the attributes lower case
        self.name = name.lower()
        self.uni = uni.lower()
        self.degree = degree.lower()
        interests = [interest.lower() for interest in list(interests)]
        self.interests = interests

    def print(self):
        # print out all the class attributes
        print(vars(self))
        return vars(self)


"""
Class for a Student (Saltire Candidate)

Methods:
    print - prints and returns attributes of the class instance

Attributes:
    name - the Student's full name
    uni - selected university of the student
    degree - selected degree of the student
    interests - list of interests of the student
"""


class Student:
    def __init__(self, name, uni, degree, interests):
        # make all the attributes lower case
        self.name = name.lower()
        self.uni = uni.lower()
        self.degree = degree.lower()
        interests = [interest.lower() for interest in list(interests)]
        self.interests = interests

    def print(self):
        # print out all the class attributes
        print(vars(self))
        return vars(self)
