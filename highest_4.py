#Kush Agrawal
# >>> highest_4([1,2,3,4])
#[1, 2, 3, 4]
#>>> highest_4([1,2,3,4,5,1,2])
#[2, 4, 3, 5]

import heapq
def highest_4(iterable):
	if (len(iterable)<=4):
		return iterable[:4]
                
	else:
		h = iterable[:4]
		for element in iterable[4:]:
			if (h[0]<element):
				heapq.heappop(h)
				heapq.heappush(h, element)
		return h

