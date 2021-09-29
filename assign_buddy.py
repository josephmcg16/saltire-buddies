"""
Simple Script to Assign a Saltire Candidate to an Alumni Based on Interests

Data gathered from Google Forms:
- Saltire Candidate Form
- Saltire Alumni (Buddy) Form

Based on the Form inputs, a Candidate is assigned to an Alumni.

Simple Example Below, works out compatibility based on the uni the couple go to.
Can easily extend this code.
"""

from src.Scholars import Student, Buddy
from data import scottish_unis as unis


# simple example of the usage of the Student and Buddy classes
def example():
    # variables for charlie Student class instance
    # (yes this example is an Always Sunny reference...)
    name = "Charlie Day"
    uni = "University of Strathclyde"
    degree = "law"
    interests = "bird law", "milk-steak", "money"
    # create the Charlie Student object
    charlie = Student(name, uni, degree, interests)

    # variables for dennis Buddy class instance
    name = "Dennis Reynolds"
    uni = "university of aberdeen"
    degree = "D.E.N.N.I.S system"
    interests = "tools", "separating entirely", "makeup", "money"
    # create the dennis Buddy object
    dennis = Buddy(name, uni, degree, interests)

    # and return a dictionary of the charlie and dennis objects
    return {"Student": charlie, "Buddy": dennis}


# calculate compatibility score based on academic attributes (uni, degree, location of unis)
def assign_academia(student, buddy):
    if student.uni not in unis.names or buddy.uni not in unis.names:
        raise ValueError('Invalid input, university does not exist.')
    elif student.uni == buddy.uni:
        # same university
        score = 10
    else:
        score = unis.distance(student.uni, buddy.uni)
    return score


if __name__ == '__main__':
    mydict = example()  # return dictionary containing the Student and Buddy class instances
    compatibility = assign_academia(mydict['Student'], mydict['Buddy'])
    print(f'Compatibility: {compatibility}')
