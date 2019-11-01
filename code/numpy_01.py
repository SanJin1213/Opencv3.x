import numpy as np

# create a new array
m = np.array(
    [[0, 0, 0],
     [1, 1, 1],
     [2, 2, 2]])

print(m[1, 1])
print(m[:, 2])
print(m[1, :])
print(m[0:2, 1:2])

# 输出结果
# 1
# [0 1 2]
# [1 1 1]
# [[0]
#  [1]]
