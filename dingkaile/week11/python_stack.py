
class stack():

	def __init__(self):
		self.contain=[]

	def push(self,value):
		self.contain.append(value)

	def pop(self):
		return self.contain.pop(self.contain[-1])