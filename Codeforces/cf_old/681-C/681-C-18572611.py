from heapq import heappush,heappop
n = int(raw_input())
h = []
#h will be used a binary heap
p = []
for i in range(0,n):
	x = raw_input().split()
	if(x[0] == "insert" or x[0] == "getMin") :
		data = int(x[1])
	if(x[0] == "insert"):
		heappush(h,(data))
		p.append( "insert %d" %(data))
	if(x[0] == "removeMin"):
		if(h):
			p.append("removeMin")
			heappop(h)
		else :
			p.append("insert 0")
			p.append("removeMin")
	if(x[0] == "getMin") :
		if(h) :
			while (h and h[0] < data):
				p.append( "removeMin")
				heappop(h)
			if (not(h) or (h[0] > (data))) :
				heappush(h,(data))
				p.append( "insert %d" %(data))
			p.append( "getMin %d" %(data))
		else :
			heappush(h,data)
			p.append("insert %d" %((data)))
			p.append("getMin %d" %((data)))

print len(p)
print '\n'.join(p)