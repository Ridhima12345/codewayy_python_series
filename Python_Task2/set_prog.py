#Initializing a set

marks = {45,56,12,85,99}
print("Marks :-",marks,end = " ")

#add() adds elements to the set

marks.add(87)
print("\nUpdated marks :-",marks,end = " ")

#len() returns length of the set

print("Length of the set is :-",len(marks))

#remove() will remove the element from the set

marks.remove(12)
print("After removing an element :-",marks)

name = {"Ridhi","Priya","Shreyee"}

#union() merges two sets

mergedSet = marks.union(name)
print("\nMerged List:-")
print(mergedSet)

#intersection() returns all the commmon value between 2 sets

setNew = {1,2,3,4,5}
setOld = {3,4,7,8,9}
print("\nIntersection between 2 sets will  be :- ",setNew.intersection(setOld))

#difference() removes the common elements from the first set and returns it

setNew = {1,2,3,4,5}
setOld = {3,4,7,8,9}
print("\nDifference between 2 sets will  be :- ",setNew.difference(setOld))

#clear() empties the set

marks.clear()
print(marks)
