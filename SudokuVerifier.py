__author__ = 'rohanmathure'

import unittest


class SudokuVerifier(object):

    def __init__(self, data):
        self.data = data
        self.blocks = [[[], [], []] for i in range(3)]
        self.columns = [[] for i in range(9)]

    def is_sudoku_valid(self):
        for row in self.data:
            if not self.is_sudoku_data_valid(row):
                return False

        for column in self.columns:
            if not self.is_sudoku_data_valid(column):
                return False

        for board in self.blocks:
            for subBoard in board:
                if not self.is_sudoku_data_valid(subBoard):
                    return False
        return True

    def is_sudoku_data_valid(self, dataList):
        initialSet = set()
        for i in range(1,10):
            initialSet.add(i)

        for data in dataList:
            if data in initialSet:
                initialSet.remove(data)
            else:
                return False

        if len(initialSet) > 0:
            return False

        return True

    def parseData(self, dataList):
        for i in range(len(dataList)):
            for j in range(len(dataList[i])):
                self.columns[j].append(dataList[i][j])
                self.blocks[int(i/3)][int(j/3)].append(dataList[i][j])


class TestSudokuVerifierTrue(unittest.TestCase):
    def setUp(self):
        dataList = [
            [4,3,5,2,6,9,7,8,1],
            [6,8,2,5,7,1,4,9,3],
            [1,9,7,8,3,4,5,6,2],
            [8,2,6,1,9,5,3,4,7],
            [3,7,4,6,8,2,9,1,5],
            [9,5,1,7,4,3,6,2,8],
            [5,1,9,3,2,6,8,7,4],
            [2,4,8,9,5,7,1,3,6],
            [7,6,3,4,1,8,2,5,9]
        ]
        self.sudokuVerifier = SudokuVerifier(dataList)
        self.sudokuVerifier.parseData(dataList)

    def test_is_sudoku_valid(self):
        self.assertEqual(self.sudokuVerifier.is_sudoku_valid(), True)

    def test_parse_data(self):
        pass


class TestSudokuVerifierCommonRow(unittest.TestCase):
    def setUp(self):
        dataList = [
            [4,3,5,2,6,9,7,8,4],
            [6,8,2,5,7,1,4,9,6],
            [1,9,7,8,3,4,5,6,1],
            [8,2,6,1,9,5,3,9,8],
            [3,7,4,6,8,2,9,1,3],
            [9,5,1,7,4,3,6,2,9],
            [5,1,9,3,2,6,8,7,5],
            [2,4,8,9,5,7,1,3,2],
            [7,6,3,4,1,8,2,5,7]
        ]
        self.sudokuVerifier = SudokuVerifier(dataList)
        self.sudokuVerifier.parseData(dataList)

    def test_is_sudoku_valid(self):
        self.assertEqual(self.sudokuVerifier.is_sudoku_valid(), False)


class TestSudokuVerifierCommonColumn(unittest.TestCase):
    def setUp(self):
        dataList = [
            [4,3,5,2,6,9,7,8,1],
            [6,8,2,5,7,1,4,9,3],
            [1,9,7,8,3,4,5,6,2],
            [8,2,6,1,9,5,3,4,7],
            [3,7,4,6,8,2,9,1,5],
            [9,5,1,7,4,3,6,2,8],
            [5,1,9,3,2,6,8,7,4],
            [2,4,8,9,5,7,1,3,6],
            [4,3,5,2,6,9,7,8,1]
        ]
        self.sudokuVerifier = SudokuVerifier(dataList)
        self.sudokuVerifier.parseData(dataList)

    def test_is_sudoku_valid(self):
        self.assertEqual(self.sudokuVerifier.is_sudoku_valid(), False)

    def test_parse_data(self):
        self.assertEqual(self.sudokuVerifier.columns[0][5], 9)
        self.assertEqual(self.sudokuVerifier.columns[1][5], 5)
        self.assertEqual(self.sudokuVerifier.columns[3][5], 7)
        for col in self.sudokuVerifier.columns:
            self.assertEqual(len(col), 9)

class TestSudokuVerifierCommonBlock(unittest.TestCase):
    def setUp(self):
        dataList = [
            [4,7,2,5,9,3,8,1,6],
            [6,4,7,2,5,9,3,8,1],
            [1,6,4,7,2,5,9,3,8],
            [8,1,6,4,7,2,5,9,3],
            [3,8,1,6,4,7,2,5,9],
            [9,3,8,1,6,4,7,2,5],
            [5,9,3,8,1,6,4,7,2],
            [2,5,9,3,8,1,6,4,7],
            [7,2,5,9,3,8,1,6,4]
        ]
        self.sudokuVerifier = SudokuVerifier(dataList)
        self.sudokuVerifier.parseData(dataList)

    def test_is_sudoku_valid(self):
        self.assertEqual(self.sudokuVerifier.is_sudoku_valid(), False)

    def test_parse_data(self):
        self.assertEqual(self.sudokuVerifier.blocks[0][1][2], 3)
        self.assertEqual(self.sudokuVerifier.blocks[1][1][2], 2)
        self.assertEqual(self.sudokuVerifier.blocks[2][2][5], 7)
        for row in self.sudokuVerifier.blocks:
            for block in row:
                self.assertEqual(len(block), 9)
