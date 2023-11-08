# class ABC:
#     def __int__(self):
#         self.public_attribute = None # public attribute
#
#     def public_function(self):
#         pass

# Private Attribute (2 __)
# class ABC:
#     def __init__(self):
#         self.__private_attribute = None  # private attribute
#
#     def __private_function(self):
#         pass
#
#
# obj1 = ABC()
# print(obj1.private_attribute)  # Through error

# Protected Attribute (1 _ )
class ABC:
    def __int__(self):
        self._protected_attribute = None # protected attribute

    def _protected_function(self):
        pass


