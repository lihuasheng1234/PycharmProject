import numpy
n1 = numpy.arange(1,17).reshape(8,2)
# print(n1.ndim)
# print(n1.dtype)
# print(n1.shape)
# print(n1.size)

# print(numpy.arange(0,10).reshape(2,5))

# print(numpy.random.rand(9))
print(numpy.random.randn())
# print(numpy.random.mtrand.rand(9))

# print(numpy.empty(9))
# print(numpy.zeros(9))
# print(numpy.ones(9))

# print(numpy.random.randint(1,10,9))
# print(numpy.where(n1>5,n1,0))

numpy.random.seed(42)
n2 = numpy.random.randint(1,10,16).reshape(4,4)
# print(n2)
# print(n2[:,0:3:1])

# print(n2*n2)
# print(numpy.dot(n2,n2))

# print(n1)
# print(n2)
#
#
# print(numpy.hstack((n1,n2)))
# #
# # print(numpy.stack((n1,n2),axis=0))
#
# print(numpy.column_stack((n1,n2)))
# print(numpy.row_stack((n1,n2)))
# print(n1)
# print(numpy.vsplit(n1,4)[0])

# print(numpy.dtype('i8'))

a = numpy.arange(10)**3
print(a)
a[:6:2] = -1000
print(a)


