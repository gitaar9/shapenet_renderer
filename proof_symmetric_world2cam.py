import numpy as np
from os.path import join


def read_array(path):
    with open(path, 'r') as f:
        lines = f.readlines()
    numbers = lines[0].strip().split()
    a = np.asarray(numbers).reshape(4, 4).astype(float)
    return a


base_path = 'inference_poses/cars/1a64bf1e658652ddb11647ffa4306609/pose/'
a0 = read_array(join(base_path, '000000.txt'))
a1 = read_array(join(base_path, '000001.txt'))
a2 = read_array(join(base_path, '000002.txt'))
a3 = read_array(join(base_path, '000003.txt'))


sign01 = np.sign(a0) != np.sign(a1)
sign23 = np.sign(a2) != np.sign(a3)

print(sign01)
print(sign23)
print(sign01 == sign23)

mult_matrix = (sign01.astype(float) * -2) + 1
print(mult_matrix)

print(np.multiply(a0, mult_matrix) == a1)
print(np.multiply(a1, mult_matrix) == a0)
print(np.multiply(a2, mult_matrix) == a3)
print(np.multiply(a3, mult_matrix) == a2)

print(a0)
