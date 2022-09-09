import array as arr
a=arr.array('i',[1,2,3,4,1,1,1])
print("count",a.count(1))
# print("arr.byte",a.byteswap())
#print("arr.buffer_info",a.buffer_info())
print("arr.reverse",a[::-1])
print(a)
a.reverse()
print("a",a)