import sys

import numpy as np

from func import *
from zastavka import zastavka



'''
1)
AX=B
X=A-1 * B

2)
XA = B
X = B*A-1


3)
AXC = B
X = A-1*B*C-1


'''
def main():
    """
    Главная функция
    """
    #функция для меню
    menu()

    variant = input_int_in_range(start=1, end=4)
    
    A = np.empty((1,1))
    B = np.empty((1,1))
    C = np.empty((1,1))


    if variant==1:

        a_size = input_int("Введите размерность матрицы A:\t")
        A = np.empty((a_size,a_size))

        b_rows = input_int("Введите количество строк матрицы B:\t")
        b_cols = input_int("Введите количество столбцов матрицы B:\t")
        B =  np.empty((b_rows,b_cols))

        X = np.empty((a_size,a_size))
        
        # print("Выберите заполнить матрицу вручную(введите 1) или случайными числами(введите 2)")
        choic1 = choice(prompt='A')
        A = fill_matrix(A, (a_size,a_size), choic1)
        
        # print("Заполнить матрицу вручную(введите 1) или случайными(введите 2) числами")
        choic2 = choice(prompt='B')
        B = fill_matrix(B, (b_rows,b_cols), choic2)
        
    if variant==2:

        a_size = input_int("Введите размерность матрицы A:\t")
        A = np.empty((a_size,a_size))

        b_rows = input_int("Введите количество строк матрицы B:\t")
        b_cols = input_int("Введите количество столбцов матрицы B:\t")
        B =  np.empty((b_rows,b_cols))

        X = np.empty((a_size,a_size))
        
        # print("Выберите заполнить матрицу вручную(введите 1) или случайными числами(введите 2)")
        choic1 = choice(prompt='A')
        A = fill_matrix(A, (a_size,a_size), choic1)
        
        # print("Заполнить матрицу вручную(введите 1) или случайными(введите 2) числами")
        choic2 = choice(prompt='B')
        B = fill_matrix(B, (b_rows,b_cols), choic2)

    if variant==3:

        a_size = input_int("Введите размерность матрицы A:\t")
        A = np.empty((a_size,a_size))

        b_rows = input_int("Введите количество строк матрицы B:\t")
        b_cols = input_int("Введите количество столбцов матрицы B:\t")
        B =  np.empty((b_rows,b_cols))

        c_size = input_int("Введите размерность матрицы C:\t")

        # print("Выберите заполнить матрицу вручную(введите 1) или случайными числами(введите 2)")
        choic1 = choice("A")
        A = fill_matrix(A, (a_size,a_size), choic1)
        
        # print("Заполнить матрицу вручную(введите 1) или случайными(введите 2) числами")
        choic2 = choice("B")

        B = fill_matrix(B, (b_rows,b_cols), choic2)

        C = np.empty((c_size,c_size))

        X = np.empty((a_size,c_size))

        # print("Заполнить матрицу вручную(введите 1) или случайными(введите 2) числами")
        choic3 = choice("C")
        C = fill_matrix(C, (c_size,c_size), choic3)

    if variant == 4:
      print("Вы вышли из программы")
      sys.exit(0)


    X = solve(variant, A, B, C, X)
    print(A.dtype)
    result_in_file = "результат.txt"
    history_in_file = "история.txt"
    write_to_files(history_in_file,result_in_file ,variant,A,B,C,X)
    
if __name__=="__main__":
    """
    Точка входа в программу

    """
    #функция для заставки
    zastavka()
    while True:
        v = input("Продолжить или выйти из программы (Y/N): ")
        if v.lower() == "y":
            main()
            break  # Выход из цикла после успешного выполнения main()
        elif v.lower() == "n":
            print("вы вышли из программы")
            sys.exit(0)
        else:print("Некорректный ввод. Пожалуйста, введите 'Y' или 'N'.")