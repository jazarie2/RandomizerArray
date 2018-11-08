# RandomizerArray
a simple python snip to get a sequential number (i.e. 0~100) and split it unevenly to n split

Python snipets to get a list of randomize number that will deviate +3 and -3 from min of the total value split +3(Total/Split)-3
usage

#require numpy

from RandomizerArray import Randomizer as RA
q = RA(maxval=40, split=4)
q.placement #(To get result)

example of result:
[
	[21, 13, 5, 36, 30, 32, 6, 7, 40], 
	[10, 29, 1, 20, 3, 15, 34, 35, 17, 9, 26], 
	[4, 39, 38, 22, 27, 11, 33], 
	[2, 37, 8, 12, 14, 16, 18, 19, 23, 24, 25, 28, 31]
]

