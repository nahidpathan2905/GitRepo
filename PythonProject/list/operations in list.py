ls=[5,2,4,3,2,2,11.8]
print(len(ls))   #size
print(ls[3])   #specific data
newLs=sorted(ls)  #sort list without changing original list
print(newLs)
print(ls)

#del ls  #delete list
#print(ls) #error
print(ls.index(3))   #first occurrence at that index(to search)
print(ls.count(2))   #total occ.
nl=sorted(ls)
print(nl)
ls.sort()    #ascending
print(ls)
ls.reverse()   #descending
print(ls)
ls1=ls.copy()   #copy list
print(ls1)
ls.remove(2)   #remove any obj
print(ls)
ls.pop(2)   #remove element by index
print(ls)
ls.pop()   #last index removed
print(ls)
ls.extend([9,7])   #add multiple element
print(ls)
ls.append(6)   #add element
print(ls)
ls.insert(0,1)  #add element to sp index0/41L-|+
print(ls)

