import numpy as np
import subprocess

"""
Набор функций использующихся для обработки матриц
"""

def meet():
    # Запускаем исполняемый файл
    subprocess.run(["./curs1.exe"])
    print("""
            Курсовая работа на тему решение матрчиных уравнений методом обратной матрицы
                Автор:Цыбузин Даниил Владиславович, студент группы 24ВВВ1
                2025 год
                """)
    

def menu():
    

   

    print("""
          
          
            Выберите подходящий тип уравнения
                        1)A*X=B
                        X=A^(-1) * B
                                

                        2)X*A = B
                        X = B*A^(-1)
                                    
                                
                        3)A*X*C = B
                        X = A^(-1)*B*C^(-1)
                """)    
    
def inversed_matrix(Matrix:np.array)->np.array:
    '''
Нахождение обратной матрицы
'''
    try:
        Ainv = np.linalg.inv(Matrix)
        return Ainv
    except:
        print("Матрица необратима, так как не является квадратной")
    

def input_int_in_range(start:int, end:int)->int:
    """
    Ввод чисел с огр диапазоном 
    """
    while True:
        try:
            inputr = int(input())
            if not(inputr<start or inputr>end):
                return inputr
            else:
                print(f"Введённое число меньше {start} или больше {end}, повторите,пожалуйста, ввод")
            
                
        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")
        
       
def input_int(var:int)->int:
    inti = 0
    l1st = ''
    if var<3:
        l1st = "AB"
    else: l1st = "ABC"

    for i in range(len(l1st)):
        try:
            print("Введите количество строк матрицы {i}:\t")
            inti = int(input())
            return inti

        except ValueError:
            print("Вы ввели не число. Попробуйте снова.")

def input_int(prompt: str) -> int:
    """
    Ввод целого числа с указанным приглашением.

    Args:
        prompt: Приглашение для ввода.

    Returns:
        Введенное целое число.
    """
    while True:
        try:
            print(prompt)
            inti = int(input())
            return inti
        except:
            print("Вы ввели не число или превысили предел. Попробуйте снова.")


def choice(prompt:str)->int:
    choic = 0
    """
    Выбор заполнить матрицу самостоятельно и случайными числами
    """
    print(f"Выберите заполнить матрицу {prompt} вручную(введите 1) или случайными числами(введите 2)")
    
    while True:
        try:
            while True:
                choic = int(input())
                if 1<=choic<=2:
                    return choic
                else: print("Вы написали число больше 2 или меньше 1")

        except:
            print("Вы ввели не число. Попробуйте снова.")


def fill_matrix(Mat:np.array, dim:tuple, choic:int)->np.array:
    """
    Заполнение матрицы
    """
    # if type(dim)
    #print("")
    if choic == 1:
        for i in range(dim[0]):
            for j in range(dim[1]):
                try:
                    Mat[i, j] = int(input())
                except ValueError:
                    print("Введи число")
        return Mat



    if choic == 2:
        for i in range(dim[0]):
            for j in range(dim[1]):
                
                Mat[i, j] = np.random.randint(-100, 100)
        return Mat

def solve(var:int,M1:np.array, M2:np.array ,M3:np.array, SOLVED:np.array):
    if var ==3:
        return solved3(M1,M2,M3,SOLVED)
    else:
        return solved12(var,M1,M2,SOLVED)

def solved12(var:int,M1:np.array, M2:np.array , SOLVED:np.array)->np.array:

    '''
    var - вариант матричного уравнения
    M1 - Матрица А
    M2 - Матрица B                    
    Решение матричного уравнения в соответствии с выбранным типом
    '''


    M1_inv= inversed_matrix(M1)

    if var == 1:
        try:
            if SOLVED is not None:
                print("""
AX=B
X=A^(-1) * B
                      """)
                print(f"Матрица A:\n{M1}\n")
                print(f"Матрица B:\n{M2}\n")
                
            SOLVED = M1_inv @ M2
            print(f"Матрица X:{SOLVED}\n")
            return SOLVED
        except:
            print("Ошибка произведения матриц, вероятно размерности матриц не совпадают")
        
        
    else:
        try:
            if SOLVED is not None:
                print("""
XA = B
X = B*A^(-1)

                      """)
                print(f"Матрица A:\n{M1}\n")
                print(f"Матрица B:\n{M2}\n")
                # print(f"Матрица X:{SOLVED}\n")
            SOLVED = M2 @ M1_inv
            print(f"Матрица X:{SOLVED}\n")
            return SOLVED
        except:
            print("Ошибка произведения матриц, вероятно размерности матриц не совпадают")

def solved3(M1:np.array, M2:np.array ,M3:np.array, SOLVED:np.array)->np.array:


    '''
    var - вариант матричного уравнения
    M1 - Матрица А
    M2 - Матрица B
    M3 - Матрица C
    Решение матричного уравнения в соответствии с выбранным типом
    '''
    M1_inv= inversed_matrix(M1)
    M3_inv= inversed_matrix(M3)

    try:
            if SOLVED is not None:
                print("""
AXC = B
X = A^(-1)*B*C^(-1)
                      """)
                print(f"Матрица A:\n{M1}\n")
                print(f"Матрица B:\n{M2}\n")
                print(f"Матрица С:\n{M3}\n")
                # 
            SOLVED = M1_inv @ M2
            SOLVED @= M3_inv #np.dot(inversed_matrix(M1),M2)
            # SOLVED = np.dot(M3)
            print(f"Матрица X:{SOLVED}\n")
            return SOLVED
    except:
            print("Ошибка произведения матриц, вероятно размерности матриц не совпадают или матрицы были не квадратными")

def write_to_files(append_filename: str, overwrite_filename: str, var: int, M1: np.array, M2: np.array, M3: np.array, SOLVED: np.array):
    try:
        # Append to the append_filename
        with open(append_filename, 'a', encoding="UTF-8") as append_file:
            if var in (1, 2):
                append_file.write(f"Вы выбрали это вариант уравнения {var}\n\n")
                append_file.write(f"Матрица A:\n{M1}\nМатрица B:\n{M2}\nМатрица X:\n{SOLVED}\n\n")

            elif var == 3:
                append_file.write(f"Вы выбрали это вариант уравнения {var}\n\n")
                append_file.write(f"Матрица A:\n{M1}\nМатрица B:\n{M2}\nМатрица C:\n{M3}\nМатрица X:\n{SOLVED}\n\n")
            else:
                print(f"Warning: Invalid value for 'var': {var}. Nothing written to {append_filename}.")

        # Overwrite the overwrite_filename
        with open(overwrite_filename, 'w', encoding="UTF-8") as overwrite_file:
            if var in (1, 2):
                overwrite_file.write(f"Матрица A:\n{M1}\nМатрица B:\n{M2}\nМатрица X:\n{SOLVED}\n")
            elif var == 3:
                overwrite_file.write(f"Матрица A:\n{M1}\nМатрица B:\n{M2}\nМатрица C:\n{M3}\nМатрица X:\n{SOLVED}\n")
            else:
                print(f"Warning: Invalid value for 'var': {var}. Nothing written to {overwrite_filename}.")

    except Exception as e:
        print(f"Error writing to file(s): {e}")