# create a list as below
# output=[[1,2,3],[4,5,6],[7,5,3,2,3,[2,[3]]]]
a=[1,2,3]
b=[4,5,6]
c=[7,5,3,2,3]
d=[2]
e=[3]
d.append(e) 
print(d)  # [2, [3]]

c.append(d)
print(c)  # [7, 5, 3, 2, 3, [2, [3]]]

output = [a,b,c]
print(output)  # [[1, 2, 3], [4, 5, 6], [7, 5, 3, 2, 3, [2, [3]]]]

# use these lists to create another list which will look like the list output in line 2

# use append method to do this.

