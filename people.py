hiddenpeople = {'Paul': {'bald': False, 'beard': False, 'eyes': 'brown', 'gender': 'man', 'hair': 'white', 'hat': False,
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
                }

for person in hiddenpeople:
    # if not hiddenpeople[person]['beard']:
    print(person + ': ' + str(hiddenpeople[person]))
