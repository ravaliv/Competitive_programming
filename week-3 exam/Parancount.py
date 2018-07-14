class Parancount:
	def paranthesis(self, n):
		res = []
		self.printall(res, "", n, n)
		return res

	def printall(self, res, c, l, r):
		if l == 0 and r == 0:
			res.append(c)
		if l > 0:
			self.printall(res, c + "(", l - 1, r)
		if l < r:
			self.printall(res, c + ")", l, r - 1)

    


if __name__ == "__main__":
	n=int(input("enter a number: "))
	r=Parancount().paranthesis(n)
	print (r)
	print (len(r))
