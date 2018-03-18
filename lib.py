#!/usr/bin/python3

class Matrix:

	def __init__(self, *args):
		self.state = []
		self.size = len(args[0])
		
		if not all(len(a) == self.size for a in args):
			raise ValueError("Incorect number of columns, different than {0}!".format(self.size))
		[self.state.append(a) for a in args]
		
		if len(self.state) != self.size:
			raise ValueError("Incorrect number of rows, different than {0}!".format(self.size))

	def __str__(self):
		return "[{0}]".format(",\n".join(map(lambda x: str(x),self.state)))

	def __eq__(self,other):
		if not self.validate_matrix_size(other):
			return False
		
		if not all(self.state[i][j] == other.state[i][j] for i in range(self.size) for j in range(self.size)):
			return False

		return True

	def __add__(self,other):
		if self.is_number(other):
			return self.add_with_scalar(other)
		if not self.validate_matrix_size(other):
			raise ValueError("Matrixes have different sizes!")
		return self.add_with_matrix(other)

	def __radd__(self, other):
		return self.add_with_scalar(other)

	def add_with_matrix(self,matrix):
		return self.matrix_operation(lambda i,j: self.state[i][j] + matrix.state[i][j])
	
	def add_with_scalar(self,scalar):
		return self.matrix_operation(lambda i,j: self.state[i][j] + scalar)
	
	def __sub__(self,other):
		if self.is_number(other):
			return self.sub_with_scalar(other)
		if not self.validate_matrix_size(other):
			raise ValueError("Matrixes have different sizes!")
		return self.sub_with_matrix(other)
		
	def sub_with_matrix(self,matrix):
		return self.matrix_operation(lambda i,j: self.state[i][j] - matrix.state[i][j])
	
	def sub_with_scalar(self,scalar):
		return self.matrix_operation(lambda i,j: self.state[i][j] - scalar)

	def __rsub__(self, other):
		return self.matrix_operation(lambda i,j: other - self.state[i][j])

	def __mul__(self,other):
		if self.is_number(other):
			return self.mul_with_scalar(other)
		if not self.validate_matrix_size(other):
			raise ValueError("Matrixes have different sizes!")

		return self.mul_with_matrix(other)

	def mul_with_scalar(self,scalar):
		return self.matrix_operation(lambda i,j: self.state[i][j] * scalar)

	def mul_with_matrix(self,matrix):
		new_matrix_state = []
		for i in range(self.size):
			temp = []
			[temp.append(sum([self.state[i][k] * matrix.state[k][j] for k in range(self.size)])) for j in range(self.size)]
			new_matrix_state.append(temp)
		return Matrix(*new_matrix_state)

	def __rmul__(self,other):
		return self.mul_with_scalar(other)

	def matrix_operation(self,operation):
		new_matrix_state = []
		[new_matrix_state.append([operation(i,j) for j in range(self.size)]) for i in range(self.size)]
		return Matrix(*new_matrix_state)

	def is_number(self, number):
		return isinstance(number,(int,float))

	def validate_matrix_size(self,matrix):
		if not isinstance(matrix,Matrix) or self.size != matrix.size:
			return False
		return True
