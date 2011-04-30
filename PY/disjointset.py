# Credit to https://code.google.com/p/ai4u
class DisjointSet:	
	def _init_(self, n):
		self.ds = []
		for i in range(n):
			self.ds.append(i)
		self.sizes = []
		for i in range(n):
			self.sizes.append(1)
		self.size = n

	def find(self, item):
		root = item
		while self.ds[root] != root:
			root = self.ds[root]
		curr = item
		while self.ds[curr] != root:
			self.ds[curr] = root	
		return root

	def join(self, item1, item2)	
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


