# Credit to https://code.google.com/p/ai4u
class DisjointSet:	
	def _init_(n):
		self.ds = zeros(n,Int)
		for i in range(n):
			self.ds[i] = i
		self.sizes = zeros(n,Int)
		for i in range(n):
			self.sizes[i] = 1
		self.size = n
	def find(item):
		root = item
		while self.ds[root] != root:
			root = self.ds[root]
		curr = item
		while self.ds[curr] != root:
			self.ds[curr] = root	
		return root
	def join(item1,item2)	
		group1 = find(item1)	
		group2 = find(item2)
		--self.size
		if self.sizes[group1] > self.sizes[group2]:
			self.ds[group2] = group1
			self.sizes[group1] += self.sizes[group2]
			return group1
		else:
			self.ds[group1] = group2
			self.sizes[group2] += self.sizes[group1]
			return group2


