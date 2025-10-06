

# class person:


#     def __init__(self, name , age , email):
#         self._name = name
#         self._age = age
#         self._email = email

#     @property
#     def age(self):
#         return self._age


#     @property
#     def name(self):
#         return self._name


#     @property
#     def email(self):
#         return self._email
    

#     @email.setter
#     def email(self, new_email):
        
#         if "@" in new_email:
#             self._email = new_email
#         else:
#             raise ValueError("din mail måste innehålla '@' annars är den inte godkänd")

#     @name.setter
#     def name(self, new_name):
#         if new_name.strip().isalpha():
#             self._name = new_name
#         else:
#             raise ValueError("ditt namn får bara innehålla bokstäver")



#     @age.setter
#     def age(self, new_age):
#         if 0 < new_age < 125:
#             self._age = new_age
#         else:
#             raise ValueError("du är inte inom en rimlig ålder")


        
#     def __repr__(self):
#         return f"""hi my name is {self._name}
# I am {self._age} years old
# and my email adess is: {self._email} """

# person1 = person("zebbe", 135, "hejsan@svejsan")

# name = input("skriv in ditt namn: ")
# age = input("skriv in din ålder: ")
# email = input("skriv in din email: ")


# person1.age = int(age)
# person1.email = email
# person1.name = name
# print(person1)