import numpy as np
class Randomizer:
	def __init__(self, maxval=24, split=3):
		print("MAX VALUE: "+str(maxval) )
		self.maxval = maxval
		self.trial = split
		self.stack = range(1,self.maxval+1)
		self.placement = []
		self.minlimit = int(round((self.maxval/self.trial/(self.trial+1))))
		self.maxlimit = int(round((self.stack.__len__()/self.trial)))
		self.get()
	def get(self):
		self.stack = range(1,self.maxval+1)
		self.placement = []
		for x in range(1, self.trial):	
			if (x<self.trial):
				self.maxlimit = int(round((self.maxval/(self.trial))))+3
				self.minlimit = self.maxval/(self.trial)-3
				howmany = np.random.randint(self.minlimit,self.maxlimit)		
				t = list(np.random.choice(self.stack,howmany,replace=False))			
				self.placement.append(np.sort(t))
				self.stack = list(set(self.stack) - set(t))
		self.placement.append(self.stack)
		for q in self.placement:
			print "total:" + str(q.__len__()) +" ==> "+ str(q)
		return self.placement

r = Randomizer()
