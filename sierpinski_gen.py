""" [[1]]                     1x1

 [[1, 0],                     2x2
  [1, 1]]

 [[1, 0, 0, 0],               4x4
  [1, 1, 0, 0],
  [1, 0, 1, 0],
  [1, 1, 1, 1]]

 [[1, 0, 0, 0, 0, 0, 0, 0],   8x8
  [1, 1, 0, 0, 0, 0, 0, 0],
  [1, 0, 1, 0, 0, 0, 0, 0],
  [1, 1, 1, 1, 0, 0, 0, 0],
  [1, 0, 0, 0, 1, 0, 0, 0],
  [1, 1, 0, 0, 1, 1, 0, 0],
  [1, 0, 1, 0, 1, 0, 1, 0],
  [1, 1, 1, 1, 1, 1, 1, 1]]


  To get from stage 1 to stage 2: Append row 1. Extend the last row using a 1. Fill the first row with 0. 
  To get to stage 2 to stage 3: Append the two rows. Fill the first two rows with 0. Fill the last two rows with what was already in the matrix.
"""
def copy(mat):
    return [[mat[i][j] for j in range(len(mat[i]))] for i in range(len(mat))]

def print_mat(mat):
    s = "["
    y = ""
    for i in mat:
        for j in i:
            y += str(j) + " "
        s+=y[:-1]+",\n"
        y=" "
    print(s[:-2] + "]")


def sierpinski_gen(mat):
    k = copy(mat)
    for i in range(len(mat)): # Goes through each row
        for i in range(len(mat)): #Number of times to add 0
            mat[i].append(0)
    for i in range(len(k)):
        for j in range(len(k)):
            k[i].append(k[i][j])
        mat.append(k[i])
    return mat

def nth_sierpinski(n, mat = None):
    if mat == None:
        if n <= 1:
            return [[n]]
        else:
            return nth_sierpinski(n-1, sierpinski_gen([[1]]))
    elif n == 0:
        return mat
    else:
        return nth_sierpinski(n-1, sierpinski_gen(mat))
print_mat(nth_sierpinski(2))
