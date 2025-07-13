# $VERSION == 1.0.0

from math import sqrt
from random import random
from random import randint

precision = 1 * 10 ** -9

class SizeError(Exception):
    pass

class MatrixError(Exception):
    pass

class Matrix():

    def __init__(self, d):

        if type(d) == str:
            ## valid string matrices:
            ##    [ 1, 2, 3 ] => Row vector
            ##    [ 1, 2, 3; 4, 5, 6; 7, 8, 9 ] => General Matrix
            ##    [ 1; 2; 3 ] => Column Vector

            d = d.replace("[", "")
            d = d.replace("]", "")

            rows = d.split(';')

            m = []

            for row in rows:
                self.rows = len(rows)
                elements = row.split(',')
                newRow = []
                for e in elements:
                    self.cols = len(elements)
                    newRow.append(float(e))
                m.append(newRow)

            self.matrix = list(m)
        elif type(d) == list:
            self.rows = len(d)
            self.cols = len(d[0])
            self.matrix = d

    def __repr__(self):
        m = ''
        for row in self.matrix:
            r = '[  '
            for col in row:
                r += str(col) + '  '
            r = r.strip()
            m += r + '  ]\n'
        return m

    def getMatrix(self):
        return self.matrix

    def transpose(self):
        return Matrix(list(map(list, zip(*self.matrix))))

    def size(self, dim=None):
        if dim == None:
            return f'{self.rows}x{self.cols}'
        elif dim == 0:
            return self.rows
        elif dim == 1:
            return self.cols

    def __neg__(self):
        newMatrix = []
        for row in range(0, self.rows):
            newRow = []
            for col in range(0, self.cols):
                newRow.append(-self.matrix[row][col])
            newMatrix.append(newRow)
        return Matrix(newMatrix)

    def __pos__(self):
        return self

    # ~d - used for finding the transpose of a matrix
    def __invert__(self):
        return self.transpose()

    # Adds two matrices togther, must be of the same size
    def __add__(self, other):

        # If a constant value is added to a matrix, just add each individual value by
        # the constant - similar to how Octave does this
        
        if isinstance(other, float) or isinstance(other, int):
            newMatrix = []
            for row in self.matrix:
                newRow = []
                for element in row:
                    newRow.append(element + other)
                newMatrix.append(newRow)
            return Matrix(newMatrix)

        # Two matrices are added by adding their corresponding elements, but they must
        # be of the same size
        
        if self.size() != other.size():
            raise SizeError('Matrices must be of equal size to add together.')
        
        newMatrix = []
        for row in range(0, self.rows):
            newRow = []
            for col in range(0, self.cols):
                newRow.append(self.matrix[row][col] + other.matrix[row][col])
            newMatrix.append(newRow)
        return Matrix(newMatrix)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):

        # If a constant value is added to a matrix, just add each individual value by
        # the constant - similar to how Octave does this
        
        if isinstance(other, float) or isinstance(other, int):
            newMatrix = []
            for row in self.matrix:
                newRow = []
                for element in row:
                    newRow.append(element - other)
                newMatrix.append(newRow)
            return Matrix(newMatrix)

        # Two matrices are added by adding their corresponding elements, but they must
        # be of the same size
        
        if self.size() != other.size():
            raise SizeError('Matrices must be of equal size to add together.')
        
        newMatrix = []
        for row in range(0, self.rows):
            newRow = []
            for col in range(0, self.cols):
                newRow.append(self.matrix[row][col] - other.matrix[row][col])
            newMatrix.append(newRow)
        return Matrix(newMatrix)

    def __rsub__(self, other):
        return -self + other

    # multiply a matrix by a constant or another matrix
    def __mul__(self, other):

        # if multiplier is a constant, then multiply each element in the matrix
        # by that constant
        if isinstance(other, float) or isinstance(other, int):
            
            newMatrix = []
            for row in self.matrix:
                newRow = []
                for element in row:
                    newRow.append(element * other)
                newMatrix.append(newRow)
            return Matrix(newMatrix)

        # if the multiplier is another matrix, then perform matrix multiplication
        else:
            
            if (self.cols != other.rows):
                raise SizeError('Matrices of size ' + self.size() + ' cannot multiply with matrix of size ' + other.size())
            newMatrix = []
            for row in range(0, self.rows):
                newRow = []
                for col in range(0, other.cols):
                    newRow.append(dot(self.getRow(row+1), other.getCol(col+1)))
                newMatrix.append(newRow)
            return Matrix(newMatrix)
                    

    def __rmul__(self, other):
        return self * other

    def __pow__(self, exp):
        if self.rows != self.cols:
            return MatrixError('Can only do exponents for square matrices.')
        elif not isinstance(exp, int):
            return MatrixError('Can only use integer exponenets for matrices.')
        if exp == 0:
            return eye(self.rows)
        if exp < 0:
            self = self.inverse()
            exp = -exp
        for i in range(0, exp-1):
            self *= self
        return self
        

    # Find the dot product between two vectors
    def dot(self, other):
        if isVector(self) and isVector(other):
            return dot(getVector(self), getVector(other))
                                               
    
    def getRow(self, row):
        return self.matrix[row-1]


    def addRow(self, row, pos=None):
        if isinstance(row, Matrix):
            row = getVector(row)
        if (pos == None) or (pos == -1):
            self.matrix.insert(self.rows, row)
        elif (pos < 1) or (pos > self.rows + 1):
            raise MatrixError('Row must be inserted within the range of the matrix rows.')
        else:
            self.matrix.insert(pos-1, row)
        self.rows += 1
        return self

    def delRow(self, row):
        del(self.matrix[row-1])
        self.rows -= 1


    def getCol(self, col):
        col -= 1
        newCol = []
        for i in range(0, self.rows):
            newCol.append(self.matrix[i][col])
        return newCol


    def addCol(self, col, pos=None):
        if(pos == None) or (pos == -1):
            pos = self.cols
        elif (pos < 1) or (pos > self.cols + 1):
            raise IndexError("Column must be inserted within the range of matrix columns.")
        else:
            pos -= 1
        if isinstance(col, Matrix):
            col = getVector(col)
        if len(col) != self.rows:
            raise SizeError("Column to insert must have the same number of rows as existing matrix.")
        for i in range(0, self.rows):
            self.matrix[i].insert(pos, col[i])
        self.cols += 1
        return self


    def delCol(self, col):
        if col == -1:
            col = self.cols-1
        else:
            col -= 1
        if (col < 0) or (col >= self.cols):
            raise IndexError("Column to delete must be within range of matrix.")
        for i in range(0, self.rows):
            del(self.matrix[i][col])
        self.cols -= 1
        return self

    def setElement(self, row, col, val):
        self.matrix[row-1][col-1] = val

    def rowSwap(self, row1, row2):
        row1 -= 1
        row2 -= 1
        t_row1 = self.matrix[row1]
        t_row2 = self.matrix[row2]
        del(self.matrix[row1])
        self.matrix.insert(row1, t_row2)
        del(self.matrix[row2])
        self.matrix.insert(row2, t_row1)
        return self

    def mulRow(self, row, c):
        row -= 1
        for col in range(0, self.cols):
            self.matrix[row][col] *= c
        return self

    def mulRowAdd(self, pivot_row, update_row, c):
        pivot_row -= 1
        update_row -= 1
        for i in range(0, self.cols):
            self.matrix[update_row][i] += self.matrix[pivot_row][i] * c
        return self

    def inverse(self):
        inv = copyMatrix(self.matrix)
        if(inv.rows == inv.cols):
            for i in range(0, inv.rows):
                newCol = [0,] * i + [1,] + [0,] * (inv.rows - i - 1)
                inv.addCol(newCol)
            for i in range(0, inv.rows):
                if abs(inv.matrix[i][i]) < precision:
                    print(inv, f'i == {i}', f'matrix[i][i] == {inv.matrix[i][i]}')
                    raise MatrixError('Matrix is not invertible, dependent system.')
                else:
                    inv.mulRow(i+1, 1 / inv.matrix[i][i])
                for row in range(0, inv.rows):
                    if row != i:
                        inv.mulRowAdd(i+1, row+1, -inv.matrix[row][i])
            for i in range(0, inv.rows):
                inv.delCol(1)
            return inv.clean()
        else:
            raise SizeError('Can only invert square matrices.')


    # Returns a specified element within the matrix
    def el(self, row, col):
        return self.matrix[row-1][col-1]


    # Calculates the determinant of a square matrix
    def det(self):

        if self.rows != self.cols:
            raise MatrixError('Can only find determinants of square matrices.')

        m = self.matrix

        # for 2x2 matrices, use the det(A) = ac - ba formula
        if self.rows == 2:
            return m[0][0] * m[1][1] - m[0][1] * m[1][0]
        
        # for 3x3 matrices, use the cofactor matrix formula
        if self.rows == 3:
            a, b, c = m[0][0], m[0][1], m[0][2]
            m0 = m[1][1] * m[2][2] - m[1][2] * m[2][1]
            m1 = m[1][0] * m[2][2] - m[1][2] * m[2][0]
            m2 = m[1][0] * m[2][1] - m[1][1] * m[2][0]
            return a * m0 - b * m1 + c * m2

        # for larger matrices, use elementary row operations to create an upper-
        # triangular matrix and use the produce of the main diagonal to get the
        # value of the determinant
        
        else:
            
            T = copyMatrix(self)

            for c in range(1, self.cols):
                for r in range(c+1, self.rows+1):
                    T.mulRowAdd(c, r, -T.el(r,c) / T.el(c,c))

            det = 1
            for i in range(1, T.cols+1):
                det = det * T.el(i, i)

            return det       
        

    def clean(self):
        for i in range(0, self.rows):
            for j in range(0, self. cols):
                if abs(self.matrix[i][j]) % 1 < precision:
                    self.matrix[i][j] = int(self.matrix[i][j])
                elif abs(self.matrix[i][j] % 1 - 1) < precision:
                    self.matrix[i][j] = int(self.matrix[i][j]) + 1
        return self


    def cross(self, other, col=False):
        if isVector(self, 3) and isVector(other, 3):
            m = Matrix([ getVector(self), getVector(other) ]).matrix
            m0 = m[0][1] * m[1][2] - m[0][2] * m[1][1]
            m1 = m[0][0] * m[1][2] - m[0][2] * m[1][0]
            m2 = m[0][0] * m[1][1] - m[0][1] * m[1][0]
            if col == False:
                return Matrix(f'[ {m0}, {m1}, {m2} ]')
            else:
                return Matrix(f'[ {m0}; {m1}; {m2} ]')
            
        else:
            raise MatrixError('Can only cross product 3 dimensional vectors')
        

    def mag(self):
        if isVector(self):
            v = getVector(self)
            return sqrt(sum(map(lambda x: x ** 2, v)))
        else:
            raise MatrixError('Magnitude is only defined for vectors.')

    # compute the row-reduced echelon form for a matrix
    def rref(self):
        return self

def isVector(matrix, size=None):
    if size == None:
        if (matrix.rows == 1) or (matrix.cols == 1):
            return True
        else:
            return False
    else:
        if (matrix.rows == 1) and (matrix.cols == size):
            return True
        elif (matrix.rows == size) and (matrix.cols == 1):
            return True
        else:
            return False

def copyMatrix(matrix):
    if isinstance(matrix, Matrix):
        matrix = matrix.matrix
    return Matrix([ [ matrix[i][j] for j in range(0, len(matrix[0])) ] for i in range(0, len(matrix)) ])
        

def getVector(matrix):
    if matrix.rows == 1:
        return [ matrix.matrix[0][i] for i in range(0, matrix.cols) ]
    if matrix.cols == 1:
        return [ matrix.matrix[i][0] for i in range(0, matrix.rows) ]
    raise MatrixError('Matrix does not represent a single vector')

    
def zeros(m, n=None):
    if n == None:
        n = m
    matrix = []
    for i in range(0, n):
        matrix.append( [0,] * m)
    return Matrix(matrix)

    
def ones(m, n=None):
    if n == None:
        n = m
    matrix = []
    for i in range(0, n):
        matrix.append( [1,] * m)
    return Matrix(matrix)


def eye(rows, cols=None):
    if cols == None:
        cols = rows

    matrix = zeros(rows, cols).getMatrix()
    for i in range(0, min(rows,cols)):
        matrix[i][i] = 1

    return Matrix(matrix)


def rand(rows, cols=None, minv=None, maxv=None):
    if cols == None:
        cols = rows
    if (minv == None) and (maxv == None):
        return Matrix([ [ random() for col in range(0, cols) ] for row in range(0, rows)])
    elif (minv != None) and (maxv != None):
        return Matrix([ [ randint(minv, maxv) for col in range(0, cols) ] for row in range(0, rows) ])
    else:
        raise MatrixError('Both a minimum and maximum value must be specified for random matrix.')


def dot(l1, l2):
    if len(l1) == len(l2):
        return sum(map(lambda  x, y: x * y, l1, l2))
    else:
        raise SizeError("Dot product requires vectors of same dimension.")
    

A = Matrix('[3, 1, -5, 4; 2, -3, 3, -2; 5, -3, 4, 1; -2, 4, -3, -5]')
print(f'A == \n{A}')
print(f'det(A) == \n{A.det()}')










