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

    def test_Q1(self):
        assert model.coprime(1, 7) == True
        assert model.coprime(7, 1) == True
        assert model.coprime(21, 14) == False
        assert model.coprime(14, 21) == False
        assert model.coprime(14, 15) == True
        assert model.coprime(7, 7) == False

    def test_Q2(self):
        l = model.all_coprime_pairs([21, 1, 7, 14, 15])
        assert len(l) == 6
        l_ans = [(21, 0), (1, 7), (1, 14), (1, 15), (7, 15), (14, 15)]
        for ans in l_ans:
            tmp_tuple = (ans[1], ans[0])
            assert (ans in l) or (tmp_tuple in l)

        l = model.all_coprime_pairs([18, 6, 9])
        assert len(l) == 0

    def test_Q3(self):
        a1 = [1, 2, 3, 4, 1, 2, 3, 4, 5]
        a2 = [2, 3, 4]
        model.zero_out(a1, a2)
        assert a1 == [1, 0, 0, 0, 1, 0, 0, 0, 5]

        a3 = [5, 5, 5, 18, 5, 42, 5, 5, 5, 5]
        a4 = [5, 5]
        model.zero_out(a3, a4)
        assert a3 == [0, 0, 5, 18, 5, 42, 0, 0, 0, 0]

    def test_Q4(self, capsys):
        model.coin_flip('Q4/Q4_1.in')
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        ans = open('Q4/Q4_1_ans.out').read().replace('\r', '').rstrip()
        assert out == ans

    def test_Q5(self, capsys):

        def ruleCheck(l:list):
            nonrepeat = []
            parenFlag = True
            repeat = ''
            for char in l:
                if char.isdigit():
                    assert 1 <= int(char) <= 6  # the die only has value in the scope [1, 6]
                    if parenFlag:
                        nonrepeat.append(int(char))
                    else:
                        repeat += char

                else:  # head and tail of repeat value
                    if len(nonrepeat) >= 2:
                        for i in range(len(nonrepeat) - 1):
                            assert nonrepeat[i] != nonrepeat[i + 1]
                    nonrepeat = []

                    parenFlag = not parenFlag
                    if parenFlag:  # '1)'
                        assert 1 <= int(char[0]) <= 6
                    else:  # '(1'
                        assert 1 <= int(char[1]) <= 6

                    repeat += char

                    if parenFlag and repeat != '':
                        assert len(repeat) >= 4  # should contain a pair of parentheses and at least two repeat value
                        assert repeat.count(repeat[1]) == (len(repeat) - 2)  # values in parentheses should be same
                        repeat = ''  # init

        model.Run()
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        out_l = out.split(' ')
        ruleCheck(out_l)

        model.Run()
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        out_l = out.split(' ')
        ruleCheck(out_l)

        model.Run()
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        out_l = out.split(' ')
        ruleCheck(out_l)


    def test_Q6(self):
        assert model.craps() == 1 or model.craps() == 0
        assert 0.4 <= model.testCraps(10000) <= 0.6

    def test_Q7(self):
        l = [[2, 4, 4], [2, 8, 88, 14], [30, 60, 92]]
        assert model.is_all_even(l) is True
        l = [[2, 4, 4], [2, 8, 88, 14], [30, 60, 191]]
        assert model.is_all_even(l) is False

    def test_Q8(self):
        l = [[18, 14, 29], [12, 7, 25], [2, 22, 5]]
        assert model.rangel(l) == 28
        l = [[11, 14, 29], [20, 7, 25], [2, 22, 5]]
        assert model.rangel(l) == 28
        l = [[11, 14, 29], [12, 7, 25], [22, 2, 5]]
        assert model.rangel(l) == 28
