import copy

T = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Q = list(T)
print(T, id(T[0]))
print(Q, id(Q[0]))

T[1][0] = 100000
print(T)
print(Q)

Q1 = copy.deepcopy(T)
T[1][0] = 100

print(T, id(T[0]))
print(Q1, id(Q1[0]))

# list(...) does not recursively make copies of the inner objects.
# It only makes a copy of the outermost list, while still referencing the same inner lists, hence,
# when you mutate the inner lists, the change is reflected in both the original list and the shallow copy.
# You can see that shallow copying references the inner lists by checking
# that id(a[0]) == id(b[0]) where b = list(a).
