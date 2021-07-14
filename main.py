
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=' ')
    print()

def calculate(matrix: list) -> int:
    """Просходит подсчет кратеров.
    Args:
        matrix матрица из файла
    Return:
          Возвращает count_craters количество кратеров
    """
    count_craters = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] == 1:
                count_craters += 1
                checks_adjacent_numbers(matrix, row, column)
    return count_craters


def checks_adjacent_numbers(matrix: list, row: int, col: int) -> bool:
    """Просходит вычесление кратеров на матрице
    Args:
        matrix матрица из файла,
        row строка матрицы
        col колонка матрицы
    Return:
        Возвращает True если если был найден кратер на матрице
        """
    matrix[row][col] = 0
    row_ = [-1, 1, 0, 0]
    col_ = [0, 0, 1, -1]

    for i in range(len(row_)):
        print(f'проверяем x = {row_[i]} y = {col_[i]} при  {row}-row {col}-col')
        x = row + row_[i]
        y = col + col_[i]
        if x < 0 or y < 0 or x >= len(matrix) or y >= len(matrix[0]) or matrix[x][y] == 0:
            continue
        else:
            checks_adjacent_numbers(matrix, x, y)
            return True
