import numpy as np


class Matrix:
    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            raise ValueError("Matrix data must be a numpy array.")
        self.data = data

    def __add__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError("Matrices must have the same dimensions for addition.")
        return Matrix(self.data + other.data)

    def __mul__(self, other):
        if self.data.shape != other.data.shape:
            raise ValueError(
                "Matrices must have the same dimensions for element-wise multiplication."
            )
        return Matrix(self.data * other.data)

    def __matmul__(self, other):
        if self.data.shape[1] != other.data.shape[0]:
            raise ValueError(
                "Matrices have incompatible dimensions for matrix multiplication."
            )
        return Matrix(self.data @ other.data)

    def __str__(self):
        return str(self.data)

    def dump_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(str(self.data))


class MatrixMixin:
    def save_to_file(self, filename: str):
        with open(filename, "w") as f:
            f.write(str(self.data))

    def __str__(self):
        return np.array2string(self.data)

    @property
    def shape(self):
        return self.data.shape

    @shape.setter
    def shape(self, new_shape):
        self.data = self.data.reshape(new_shape)


class EnhancedMatrix(MatrixMixin, Matrix):
    pass


def task_1():
    """Задача 3.1"""

    np.random.seed(0)
    matrix_a = Matrix(np.random.randint(0, 10, (10, 10)))
    matrix_b = Matrix(np.random.randint(0, 10, (10, 10)))

    matrix_add = matrix_a + matrix_b
    matrix_mul = matrix_a * matrix_b
    matrix_matmul = matrix_a @ matrix_b

    matrix_a.dump_to_file("./artifacts/3_1/matrix_a.txt")
    matrix_b.dump_to_file("./artifacts/3_1/matrix_b.txt")

    matrix_add.dump_to_file("./artifacts/3_1/matrix+.txt")
    matrix_mul.dump_to_file("./artifacts/3_1/matrix*.txt")
    matrix_matmul.dump_to_file("./artifacts/3_1/matrix@.txt")


def task_2():
    """Задача 3.2"""
    matrixE_a = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))
    matrixE_b = EnhancedMatrix(np.random.randint(0, 10, (10, 10)))

    matrixE_add = matrixE_a + matrixE_b
    matrixE_mul = matrixE_a * matrixE_b
    matrixE_matmul = matrixE_a @ matrixE_b

    matrixE_add.dump_to_file("./artifacts/3_2/matrix+.txt")
    matrixE_mul.dump_to_file("./artifacts/3_2/matrix*.txt")
    matrixE_matmul.dump_to_file("./artifacts/3_2/matrix@.txt")

    matrixE_a.save_to_file("./artifacts/3_2/matrix_a.txt")
    matrixE_b.save_to_file("./artifacts/3_2/matrix_b.txt")


if __name__ == "__main__":
    task_1()
    task_2()
