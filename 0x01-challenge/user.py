#!/usr/bin/python3
""" 
User class module
"""

class User():
    """ Defines a class user
        Attr:
            email
        Methods:
            email getter
            email setter
    """

    def __init__(self):
        """ Initialize a User instance """
        self.__email = None
    
    @property
    def email(self):
        """ Define the email getter """
        return self.__email

    @email.setter
    def email(self, value):
        """ Define the email setter """
        if isinstance(value, str):
            self.__email = value
        else:
            raise TypeError("email must be a string")


if __name__ == "__main__":

    u = User()
    u.email = "john@snow.com"
    print(u.email)
