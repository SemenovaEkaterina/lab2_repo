import matplotlib.pyplot as plt
import numpy as np
import sys

from getFriendsBDateMod import getFriendsBdate
from getUserIdMod import getUserId

x = input()
	
getId = getUserId()
ID = getId.response_handler(x)

getBDate = getFriendsBdate()
bDateList = getBDate.response_handler(ID)
print(bDateList)

List = {}
for x in bDateList:
	if x not in List:
		List[x] = 1
	else:
		List[x] += 1

List2 = List.copy()

print()
while(len(List2) != 0):
	min = 100
	for x in List2.keys():
		if x < min:
			min = x
	print(min, end="")
	for i in range(List2[min]):
		print("#", end="")
	print()
	List2.pop(min)	

x= []
y = []
for i in List.keys():
	x.append(i - 0.5)
	y.append(List[i])
width = 1;


locs = x
width = 1
plt.bar(locs, y, width=width)
plt.show()

