'''
Module for automatic testing for ITI1120 assignment.

Design: Jianquan Wang
Author: Jianquan Wang | jwang438@uottawa.ca
Copyright(c) 2020 All Rights Reserved
'''
import pytest
import importlib

model = importlib.import_module("assignment_to_test")
class TestCase:

    def test_P1Q1a(self):  # 5 points
        a = [1000, 1, 100, 2, 99, 200, -100]
        assert model.largest_34(a) == 199

    def test_P1Q1b(self):  # 5 points
        a = [1000, 1, 100, 2, 99, 200, -100]
        assert model.largest_third(a) == 1200

    def test_P1Q1c(self):  # 5 points
        a = [1000, 1, 100, 2, 99, 200, -100]
        assert model.third_at_least(a) is None
        a = [1, 1, 1, 2, 2, 2, 3]
        assert model.third_at_least(a) == 1

    def test_P1Q1d(self):  # 15 points
        a = [1, 5, 8, 2, 6, 55, 90]
        x = 103
        assert model.sum_tri(a, x) is True
        a = [-10, 2]
        x = -18
        assert model.sum_tri(a, x) is True
        a = [1, 1, 5, 8, 2, 6]
        x = 1000
        assert model.sum_tri(a, x) is False

    def test_P2Q1(self):  # 10
        rect = model.Rectangle(0, 0, 1, 1)
        assert hasattr(rect, 'height') or hasattr(rect, 'get_height') or hasattr(rect, 'getHeight')
        assert hasattr(rect, 'width') or hasattr(rect, 'get_width') or hasattr(rect, 'getWidth')
        assert hasattr(rect, 'x') or hasattr(rect, 'get_x') or hasattr(rect, 'getX') or hasattr(rect, 'getx')
        assert hasattr(rect, 'y') or hasattr(rect, 'get_y') or hasattr(rect, 'getY') or hasattr(rect, 'gety')
        assert hasattr(rect, '__str__')

    def test_P2Q2(self):  # 10
        assert hasattr(model.Rectangle, 'contains')
        rect = model.Rectangle(0, 0, 1, 1)
        assert rect.contains(0.99, 0.99) is True
        assert rect.contains(0.5, 2) is False

    def test_P2Q3(self):  # 10
        assert hasattr(model.Rectangle, 'union')
        rect = model.Rectangle(0, 0, 1, 1)
        rect2 = model.Rectangle(0, 0, 0.5, 0.5)
        assert str(rect.union(rect2)) == str(rect)
        assert str(rect2.union(rect)) == str(rect)

    def test_P2Q4(self):  # 10
        assert hasattr(model.Rectangle, 'intersection')
        rect = model.Rectangle(0, 0, 1, 1)
        rect2 = model.Rectangle(0, 0, 0.5, 0.5)
        assert str(rect.intersection(rect2)) == str(rect2)
        assert str(rect2.intersection(rect)) == str(rect2)

    def test_P2Q5(self):  # bonus 10
        assert hasattr(model.Rectangle, '__eq__')
        rect = model.Rectangle(0, 0, 1, 1)
        rect2 = model.Rectangle(0, 0, 0.5, 0.5)
        rect3 = model.Rectangle(0, 0, 0.5, 0.5)
        assert rect3 != rect != rect2
        assert rect2 == rect3

    def test_P3Q1(self):  # 10
        set1 = {0, 19, 8, 9, 12, 13, 14, 15}
        list1 = [0, 19, 2, 4, 5, 9, 10, 11]
        assert model.overlap(set1, list1) == {0, 19, 9}

    def test_P3Q2(self):  # bonus 10
        d = {42:"Marty", 81:"Sue", 17:"Ed", 31:"Dave", 56:"Ed", 3:"Marty", 29:"Ed"}
        result = model.reverse(d)
        assert 42 in result['Marty'] and 3 in result["Marty"]
        assert result["Sue"] == [81]
        assert 17 in result["Ed"] and 56 in result["Ed"] and 29 in result["Ed"]
        assert result["Dave"] == [31]

    def test_P3Q3(self):  # 20
        def digit_sum(n):
            '''(int)->int
            Precondition: n >=0'''
            if n == 0:
                return 0
            return n % 10 + digit_sum(n // 10)

        def digital_root(n):
            '''(int)->int
            Precondition: n >=0'''
            if n < 10:
                return n
            digsum = digit_sum(n)
            return digital_root(digsum)

        for n in range(0, 500):
            assert model.digit_sum(n) == digit_sum(n)
            assert model.digital_root(n) == digital_root(n)

if __name__ == "__main__":
    pytest.main()
