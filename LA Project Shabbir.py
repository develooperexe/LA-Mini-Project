import numpy as np
import tkinter as tk
from tkinter import messagebox, simpledialog

def matrix_input(r, c, title="Enter matrix"):
    matrix = []
    for i in range(r):
        row = []
        for j in range(c):
            element = simpledialog.askinteger(f"{title}", f"Element [{i+1}][{j+1}]: ")
            row.append(element)
        matrix.append(row)
    return matrix

def display_matrix(matrix, title="Matrix"):
    result = f"{title}:\n"
    for row in matrix:
        result += " ".join(f"{str(element):<5}" for element in row) + "\n"
    messagebox.showinfo(title, result)

def matrix_addition():
    r = simpledialog.askinteger("Matrix Addition", "Enter the number of rows: ")
    c = simpledialog.askinteger("Matrix Addition", "Enter the number of columns: ")

    matrix1 = matrix_input(r, c, "Matrix 1")
    matrix2 = matrix_input(r, c, "Matrix 2")

    result = [[matrix1[i][j] + matrix2[i][j] for j in range(c)] for i in range(r)]
    display_matrix(result, "Result (Addition)")

def matrix_subtraction():
    r = simpledialog.askinteger("Matrix Subtraction", "Enter the number of rows: ")
    c = simpledialog.askinteger("Matrix Subtraction", "Enter the number of columns: ")

    matrix1 = matrix_input(r, c, "Matrix 1")
    matrix2 = matrix_input(r, c, "Matrix 2")

    result = [[matrix1[i][j] - matrix2[i][j] for j in range(c)] for i in range(r)]
    display_matrix(result, "Result (Subtraction)")

def matrix_multiplication():
    p = simpledialog.askinteger("Matrix Multiplication", "Enter the number of rows for Matrix 1: ")
    n = simpledialog.askinteger("Matrix Multiplication", "Enter the number of columns for Matrix 1 / rows for Matrix 2: ")
    q = simpledialog.askinteger("Matrix Multiplication", "Enter the number of columns for Matrix 2: ")

    matrix1 = matrix_input(p, n, "Matrix 1")
    matrix2 = matrix_input(n, q, "Matrix 2")

    result = [[sum(matrix1[i][k] * matrix2[k][j] for k in range(n)) for j in range(q)] for i in range(p)]
    display_matrix(result, "Result (Multiplication)")

def matrix_transpose():
    p = simpledialog.askinteger("Matrix Transpose", "Enter the number of rows: ")
    q = simpledialog.askinteger("Matrix Transpose", "Enter the number of columns: ")

    matrix1 = matrix_input(p, q, "Matrix 1")

    result = [[matrix1[j][i] for j in range(p)] for i in range(q)]
    display_matrix(result, "Result (Transpose)")

def eigen_values():
    n = simpledialog.askinteger("Eigenvalue Calculation", "Enter the dimension (n x n) of the square matrix: ")

    matrix = matrix_input(n, n, "Matrix")

    np_matrix = np.array(matrix)
    eigen_vals, _ = np.linalg.eig(np_matrix)

    result = f"Eigenvalues: {eigen_vals}\n"
    messagebox.showinfo("Eigenvalues", result)

    remove_vals = messagebox.askquestion("Remove Eigenvalues", "Do you want to remove any eigenvalues?")
    if remove_vals == 'yes':
        to_remove = simpledialog.askstring("Remove Eigenvalues", "Enter the eigenvalues to remove (comma-separated): ")
        to_remove = list(map(float, to_remove.split(',')))
        filtered_eigen_vals = [val for val in eigen_vals if val not in to_remove]

        result = f"Remaining Eigenvalues after removal: {filtered_eigen_vals}\n"
        messagebox.showinfo("Remaining Eigenvalues", result)


def create_gui():
    root = tk.Tk()
    root.title("Matrix Operations")
    root.geometry("400x400")

    tk.Label(root, text="Matrix Operations", font=("Helvetica", 16)).pack(pady=20)

    tk.Button(root, text="Matrix Addition", width=25, command=matrix_addition).pack(pady=5)
    tk.Button(root, text="Matrix Subtraction", width=25, command=matrix_subtraction).pack(pady=5)
    tk.Button(root, text="Matrix Multiplication", width=25, command=matrix_multiplication).pack(pady=5)
    tk.Button(root, text="Matrix Transpose", width=25, command=matrix_transpose).pack(pady=5)
    tk.Button(root, text="Find Eigenvalues", width=25, command=eigen_values).pack(pady=5)
    tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    create_gui()