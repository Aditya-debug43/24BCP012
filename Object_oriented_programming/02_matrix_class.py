class Matrix:
    def __init__(self, mat):
        self.mat = mat

    def __add__(self, other):
        return Matrix([[self.mat[i][j] + other.mat[i][j] for j in range(3)] for i in range(3)])

    def __mul__(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.mat[i][k] * other.mat[k][j]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.mat[j][i] for j in range(3)] for i in range(3)])

    def display(self):
        for row in self.mat:
            print(row)

a = Matrix([[1,2,3],[4,5,6],[7,8,9]])
b = Matrix([[9,8,7],[6,5,4],[3,2,1]])
a.add(b).display()
a.mul(b).display()
a.transpose().display()