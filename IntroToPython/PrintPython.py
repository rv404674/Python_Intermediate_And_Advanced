# class Person():
# 	def __init__(self, name, age):
# 		self.name, self.age = name,age

# rahul = Person('Rahul Verma', 22)
# print(repr(rahul))
# print(rahul)

#<__main__.Person object at 0x100e31dd0>
#module, class, address of object in memory.

class User:
	def __init__(self, login, pwd):
		self.login, self.pwd = login, pwd

	def __str__(self):
		return self.login

	def __repr__(self):
		return f"User {self.login} Pwd {self.pwd}"

user = User('Rahul','123we')
print(user)
#print(user) will call str(user) which will eventually call user.__str__()

print([user])
#list and tuples implements their __str__() method so that all of their elements are first converted to 
# __repr__

