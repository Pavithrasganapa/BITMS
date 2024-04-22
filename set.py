states={'goa','karnataka','mp','ap'}
print(states)
print(type(states))
print('looping through set elements')
for i in states:
    print(i)
print()
state={}#empty set is caalled dictionary
print(type(state))
print()
states=set(['goa','karnataka','mp','ap'])
print('original',states)
states.update(['up','uk','delhi'])
'''for i in states:
    print(" ",states)'''
print("updated",states)
states.remove('up')
states.pop()#it will del from randomly
states.discard('delhi')
states.clear()#it will del from randomly
print(states)
print()
day1={'mon','tue','wed','thru'}
day2={'san','mon'}
print(day1|day2)
print()
day1={'mon','tue','wed','thru'}
day2={'san','mon'}
print(day1.union(day2))#print union no print common value one time and print all element
print()
set1={1,2,4}
set2={3,4,5}
set3={4,8,9}
common=set1.union(set2,set3)
print(common)
print()
day1={'mon','tue','wed','thru'}
day2={'san','mon'}
print(day1&day2)
day1={'mon','tue','wed','thru'}
day2={'san','mon'}
print(day1.intersection(day2))
print()
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a^b#symmetric operator common data are eliminted
print(c)
print()
day1={'mon','tue','wed','thru'}
day2={'san','mon','tue'}
print(day1-day2)
print(day2.difference(day1))
print()
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a.symmetric_difference(b)
print(c)
print()
day1={'mon','tue','wed','thru'}
day2={'san','mon','tue'}
day3={'mon','tue','fri'}
print(day1>day2)#day1 is a superset of day2 then it will print true
print(day1<day2)#day1 is not the subset of set2
print(day2==day3)#print false day2 and day3 are not equivalent