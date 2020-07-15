"""
program: invoice_class.py
Author: Ondrea Li
Last date modfied: 06/30/20

The purpose of this program is print student information in a string and conduct issuperset for characters
"""


class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname) and name_characters.issuperset(
                major)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    @property
    def last_name(self):
        '''
        :return: the last name of the customer
        '''
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        '''
        :return: returns last name
        :keyError: raise AttributeError if its not a str
        '''
        if isinstance(value, str):
            self._last_name = value
        else:
            raise ValueError

    @property
    def first_name(self):
        '''
        :return: the last name of the customer
        '''
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        '''
        :return:returns first name
        :keyError: raise AttributeError if its not a str
        '''
        if isinstance(value, str):
            self._first_name = value
        else:
            raise ValueError

    @property
    def major(self):
        '''
        :return: returns the major
        '''
        return self._major

    @major.setter
    def major(self, value):
        '''
        :param value: represents the major
        :keyError: raises AttributeError
        '''
        if isinstance(value, str):
            self._major = value
        else:
            raise ValueError

    @property
    def gpa(self):
        '''
        :return: returns the gpa
        '''
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        '''
        :param value: represents the gpa
        :keyError: raises AttributeError
        '''
        if isinstance(value, float):
            if value <= 4.0 and value >= 0.0:
                self._gpa = value
            else:
                raise ValueError
        else:
            raise ValueError

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + "with gpa: " + str(self.gpa)

    def __repr__(self):
        return self.__str__()

    def display(self):
        return self.last_name + ',' + self.first_name + " has major:" + self.major + " with gpa:" + str(self.gpa)


if __name__ == '__main__':
    s = Student('Mouse', 'Mickey', 'Zoology', 4.0)
    print(s.display())
