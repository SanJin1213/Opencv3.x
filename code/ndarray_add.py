import numpy as np

src1 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
src2 = np.array([[23, 123, 90], [100, 250, 0]], np.uint8)
dst = src1 + src2
print(dst)
