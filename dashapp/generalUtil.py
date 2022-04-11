def returnStatusValue(status):
	val = 0

	if status == "Green":
		val = 100
	elif status == "Yellow":
		val = 60
	else:
		val = 30
	return val
    
def monthDataToLists(someDict):

	list1 = list()
	list2 = list()
	list3 = list()
	list4 = list()
	for k,v in someDict.items():
    		list1.append(k)
    		list2.append(v[0])
    		list3.append(float(v[1])*100)
    		list4.append(v[2])

	return list1,list2,list3,list4

def rolesAndCounters(someDict):
	list1 = list()
	list2 = list()
	for k,v in someDict.items():
    		list1.append(k)
    		list2.append(""+str(v))

	return list1,list2