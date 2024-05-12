class Calculator:
	def __init__(self):
		self.current = 0
		self.previous = 0
		self.operator = None

	def add(self, num):
		self.previous = self.current
		self.operator = 'add'
		self.current = num

	def subtract(self, num):
		self.previous = self.current
		self.operator = 'subtract'
		self.current = num

	def multiply(self, num):
		self.previous = self.current
		self.operator = 'multiply'
		self.current = num

	def divide(self, num):
		self.previous = self.current
		self.operator = 'divide'
		self.current = num

	def calculate(self):
		if self.operator == 'add':
			self.current = self.previous + self.current
		elif self.operator == 'subtract':
			self.current = self.previous - self.current
		elif self.operator == 'multiply':
			self.current = self.previous * self.current
		elif self.operator == 'divide':
			self.current = self.previous / self.current
		self.previous = 0
		self.operator = None

	def display(self):
		print(self.current)

calculator = Calculator()

while True:
	user_input = input('Enter a number or operation (+, -, *, /) or "q" to quit: ')
	if user_input == 'q':
		break
	elif user_input in ('+', '-', '*', '/'):
		calculator.add(float(user_input))
	elif user_input.isdigit():
		calculator.add(float(user_input))
	else:
		print('Invalid input')
	calculator.display()