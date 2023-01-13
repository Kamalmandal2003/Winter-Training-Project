import numpy as np

arr = np.array([
    [1,4,3,1],
    [5,4,9,6],
    [3,4,5,7]
]
)

print(arr, arr.shape)

s_arr = arr[:2, 1:3]
print(s_arr, s_arr.shape)


# Extract last row and col 0, col 1
print(arr[-1, :2])

# Extract second row 
print(arr[-2, :])
# Extract third col 
print(arr[:, 2:3])
# Extact col 1 and col 2

print(arr[:, 1:3])



arr = np.array([
    [5,4,3,1],
    [7,3,9,3],
    [6,4,2,4]
])

print(arr)
bool_idx = [arr > 3]
print(bool_idx)

print(arr[arr > 3]) 

x=np.array([
    [2,3],
    [4,6]
])
y=np.array([
    [6,7],
    [8,3]
])
print(x,y)
print(x+y)
print(np.add(x,y))
print(np.subtract(x,y))
print(np.multiply(x,y))
print(np.divide(x,y))