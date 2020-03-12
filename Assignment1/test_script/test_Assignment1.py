'''
Module for automatic testing for ITI1120 assignment.

Design: Jianquan Wang
Author: Jianquan Wang | jwang438@uottawa.ca
Copyright(c) 2020 All Rights Reserved
'''

import importlib
import pytest


model = importlib.import_module("assignment_to_test")

class TestCase:

    def test_Q1(self):
        assert "ho, ho, ho" == model.repeat('ho', 3, ', ')
        assert "1 1 1 1" == model.repeat('1', 4, ' ')
        assert "jijiji" == model.repeat('ji', 3, '')

    def test_Q2(self):
        assert model.is_prime(2) == True
        assert model.is_prime(3) == True
        assert model.is_prime(4) == False
        assert model.is_prime(9) == False

    def test_Q4(self):
        assert model.month_apart(6, 14, 9, 21) == True
        assert model.month_apart(4, 5, 5, 15) == True
        assert model.month_apart(4, 15, 5, 15) == True
        assert model.month_apart(4, 16, 5, 15) == False
        assert model.month_apart(6, 14, 6, 8) == False
        assert model.month_apart(7, 7, 6, 8) == False
        assert model.month_apart(7, 8, 6, 8) == True
        assert model.month_apart(10, 14, 7, 15) == True

    def test_Q5(self):
        assert model.reverse_int(123) == 321
        assert model.reverse_int(908) == 809
        assert model.reverse_int(111) == 111

    def test_Q7_a(self):
        assert model.allTheSame('a', 'A', 'A') == False
        assert model.allTheSame('a', 'A', 'a') == False
        assert model.allTheSame(1, 1, 1) == True
        assert model.allTheSame(False, False, False) == True

    def test_Q7_b(self):
        assert model.allDifferent('a', 'A', 'A') == False
        assert model.allDifferent('a', 'o', 'e') == True
        assert model.allDifferent(True, 'True', 1) == False
        assert model.allDifferent(True, 'True', 2) == True

    def test_Q7_c(self):
        assert model.sorted('a', 'b', 'c') == True
        assert model.sorted(1, 1, 2) == True
        assert model.sorted('ab', 'bb', 'cb') == True
        assert model.sorted('ac', 'ab', 'aa') == False

    def test_Q8(self):
        assert model.leap(2008) == True
        assert model.leap(1900) == False
        assert model.leap(2000) == True

    def test_Q9(self):
        assert model.letter2number('A-') == 3.7
        assert model.letter2number('B+') == 3.3
        assert model.letter2number('D') == 1.0
        assert model.letter2number('F') == 0

    def test_Q10(self):
        assert model.is_palindrome('madam') == True
        assert model.is_palindrome('MadaM') == True
        assert model.is_palindrome('mAdam') == False
        assert model.is_palindrome('') == True
        assert model.is_palindrome('a') == True
        assert model.is_palindrome('uuTuuTuu') == True
        assert model.is_palindrome('uuTuuTuuu') == False

    def test_Q11(self):
        assert model.is_nneg_float("2.15") == True
        assert model.is_nneg_float("3.") == True
        assert model.is_nneg_float(".5") == True
        assert model.is_nneg_float("123") == True
        assert model.is_nneg_float("-12") == False
        assert model.is_nneg_float("1e10") == False

    def test_Q12(self):
        assert model.rps('R', 'P') == 1
        assert model.rps('R', 'S') == -1
        assert model.rps('R', 'R') == 0
        assert model.rps('P', 'P') == 0
        assert model.rps('P', 'S') == 1
        assert model.rps('P', 'R') == -1
        assert model.rps('S', 'P') == -1
        assert model.rps('S', 'S') == 0
        assert model.rps('S', 'R') == 1

    def test_Q13(self):
        import math
        n = 1
        assert model.alogical(n) == math.ceil(math.log2(n))
        n = 2
        assert model.alogical(n) == math.ceil(math.log2(n))
        n = 1.1
        assert model.alogical(n) == math.ceil(math.log2(n))
        n = 5.2
        assert model.alogical(n) == math.ceil(math.log2(n))
        n = 5.4
        assert model.alogical(n) == math.ceil(math.log2(n))

    def test_Q14(self):
        assert model.count_even_digits(8546587, 7) == 4
        assert model.count_even_digits(2, 1) == 1
        assert model.count_even_digits(20, 2) == 2
        assert model.count_even_digits(13553, 5) == 0


if __name__ == '__main__':
    pytest.main()

