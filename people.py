class HiddenPeople():
    """Class for holding information on people"""

    def __init__(self):
        self.people = {
                'Paul': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'man', 'hair': 'white', 'hat': False,
                         'glasses': True, 'moustache': False},
                'Richard': {'bald': True, 'beard': True, 'eyes': 'brown', 'gender': 'man', 'hair': 'brown',
                            'hat': False, 'glasses': False, 'moustache': True},
                'George': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'white',
                           'hat': True, 'glasses': False, 'moustache': False},
                'Frans': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'red', 'hat': False,
                          'glasses': False, 'moustache': False},
                'Bernard': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'brown',
                            'hat': True, 'glasses': True, 'moustache': False},
                'Anne': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'girl', 'hair': 'black',
                         'hat': False, 'glasses': False, 'moustache': False},
                'Joe': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'blonde', 'hat': False,
                        'glasses': True, 'moustache': False},
                'Peter': {'bald': False, 'beard': False, 'eyes': 'blue', 'gender': 'boy', 'hair': 'white', 'hat': False,
                          'glasses': False, 'moustache': False},
                'Tom': {'bald': True, 'beard': False, 'eyes': 'blue', 'gender': 'boy', 'hair': 'black', 'hat': False,
                        'glasses': True, 'moustache': False},
                'Susan': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'girl', 'hair': 'blonde',
                          'hat': False, 'glasses': False, 'moustache': False},
                'Sam': {'bald': True, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'white', 'hat': False,
                        'glasses': True, 'moustache': False},
                'Maria': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'girl', 'hair': 'brown',
                          'hat': True, 'glasses': False, 'moustache': False},
                'Robert': {'bald': False, 'beard': False, 'eyes': 'blue', 'gender': 'boy', 'hair': 'brown',
                           'hat': False, 'glasses': False, 'moustache': False},
                'Alex': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'black', 'hat': False,
                         'glasses': False, 'moustache': True},
                'Charles': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'blonde',
                            'hat': False, 'glasses': False, 'moustache': True},
                'Philip': {'bald': False, 'beard': True, 'eyes': 'brown', 'gender': 'boy', 'hair': 'black',
                           'hat': False, 'glasses': False, 'moustache': False},
                'David': {'bald': False, 'beard': True, 'eyes': 'brown', 'gender': 'boy', 'hair': 'blonde',
                          'hat': False, 'glasses': False, 'moustache': False},
                'Eric': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'blonde',
                         'hat': True, 'glasses': False, 'moustache': False},
                'Bill': {'bald': True, 'beard': True, 'eyes': 'brown', 'gender': 'boy', 'hair': 'red',
                         'hat': False, 'glasses': False, 'moustache': False},
                'Alfred': {'bald': False, 'beard': False, 'eyes': 'blue', 'gender': 'boy', 'hair': 'red', 'hat': False,
                           'glasses': False, 'moustache': True},
                'Anita': {'bald': False, 'beard': False, 'eyes': 'blue', 'gender': 'girl', 'hair': 'white',
                          'hat': False, 'glasses': False, 'moustache': False},
                'Max': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'black', 'hat': False,
                        'glasses': False, 'moustache': True},
                'Herman': {'bald': True, 'beard': False, 'eyes': 'brown', 'gender': 'boy', 'hair': 'red', 'hat': False,
                           'glasses': False, 'moustache': False},
                'Claire': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'girl', 'hair': 'red', 'hat': True,
                           'glasses': True, 'moustache': False}}

    def removeperson(self, person):
        """Remove a person from listing of people to choose"""
        del self.people[person]

    def printpeople(self):
        for person in self.people:
            print(person + ": " + str(self.people[person]))
