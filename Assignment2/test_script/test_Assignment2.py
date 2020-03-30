'''
Module for automatic testing for ITI1120 assignment.

Design: Jianquan Wang
Author: Jianquan Wang | jwang438@uottawa.ca
Copyright(c) 2020 All Rights Reserved
'''

# step 1: ensure you have pytest module, if not, 'pip3 install pytest' or 'pip install pytest'
# step 2: ensure in your terminal, 'python' is python 3.x, if yours is 'python3', change all the build_cmd variables below to 'python3'
# step 3: copy student's code to assignment_to_test.py
# step 3.5: check test_Q4, test_Q7, test_Q8, test_Q9 's docstring
# step 4: run this script
# optional: you can add your test case

import subprocess
import importlib
import pytest
import os

model = importlib.import_module("assignment_to_test")
dir_work = './'
os.chdir(dir_work)

class TestCase:

    @pytest.mark.skip(reason='not-assignment-question')
    def test_templete(self):
        build_cmd = 'python -c "from assignment_to_test import func_input_test; func_input_test()"'
        fin = open('Q0/Q0.in', 'r+')
        fout = open('Q0/Q0.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q0/Q0.out').read().replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q0/Q0_ans.out').read().replace('\r', '').rstrip()
        assert out == ans


    def test_Q1(self, capsys):
        # test print_factors(15)
        assert model.print_factors(15) == False  # check return
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q1/Q1_1_ans.out').read().replace('\r', '').rstrip()
        assert out == ans  # check print
        ########################
        # test print_factor(12)
        assert model.print_factors(12) == True  # check return
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q1/Q1_2_ans.out').read().replace('\r', '').rstrip()
        assert out == ans  # check print
        ########################
        # test print_factor(1)
        assert model.print_factors(1) == False  # check return
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q1/Q1_3_ans.out').read().replace('\r', '').rstrip()
        assert out == ans  # check print

    def test_Q2(self, capsys):
        # test triangle(5)
        model.triangle(5)
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        ans = open('Q2/Q2_1_ans.out').read().replace('\r', '').rstrip()
        assert out == ans
        # test triangle(1)
        model.triangle(1)
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        ans = open('Q2/Q2_2_ans.out').read().replace('\r', '').rstrip()
        assert out == ans
        # test_triangle(6)
        model.triangle(6)
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        ans = open('Q2/Q2_3_ans.out').read().replace('\r', '').rstrip()
        assert out == ans
        # test_triangle(10)
        model.triangle(10)
        out, err = capsys.readouterr()
        out = out.replace('\r', '').rstrip()
        ans = open('Q2/Q2_4_ans.out').read().replace('\r', '').rstrip()
        assert out == ans

    def test_Q3(self):
        import math
        assert abs(math.pi - model.approxPi(0.1)) <= 0.1
        assert abs(math.pi - model.approxPi(0.01)) <= 0.01
        assert abs(math.pi - model.approxPi(0.003)) <= 0.003
        assert abs(math.pi - model.approxPi(1e-5)) <= 1e-5
        assert abs(math.pi - model.approxPi(1)) <= 1

    def test_Q4(self):
        # TAs: There are three kind of format of examples in question 4 description, so please
        # rewrite the student's code to follow the format of example #3 then test it
        # If they have typo in their printing string, help them fix it and test again

        # test case 1
        build_cmd = 'python -c "from assignment_to_test import longest_name; longest_name(7)"'
        fin = open('Q4/Q4_1.in', 'r+')
        fout = open('Q4/Q4_1.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q4/Q4_1.out').read().replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q4/Q4_1_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 2
        build_cmd = 'python -c "from assignment_to_test import longest_name; longest_name(2)"'
        fin = open('Q4/Q4_2.in', 'r+')
        fout = open('Q4/Q4_2.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q4/Q4_2.out').read().replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q4/Q4_2_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 3
        build_cmd = 'python -c "from assignment_to_test import longest_name; longest_name(3)"'
        fin = open('Q4/Q4_3.in', 'r+')
        fout = open('Q4/Q4_3.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q4/Q4_3.out').read().replace('\r', '').rstrip()  # remove \r and space and \n at the end of string
        ans = open('Q4/Q4_3_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

    def test_Q5(self):
        l = []
        assert model.is_fib_like(l) == True
        l = [42]
        assert model.is_fib_like(l) == True
        l = [18, 42]
        assert model.is_fib_like(l) == True
        l = [1, 1, 1]
        assert model.is_fib_like(l) == False
        l = [0, 0, 0, 0, 0]
        assert model.is_fib_like(l) == True
        l = [1, 1, 2, 3, 5, 8, 13, 21]
        assert model.is_fib_like(l) == True
        l = [2, 1, 3, 4, 7, 11, 18, 29]
        assert model.is_fib_like(l) == True
        l = [1, 1, 2, 3, 5, 12, 17]
        assert model.is_fib_like(l) == False

    def test_Q6(self):
        assert model.gcd(0, 0) == 0
        assert model.gcd(1, 7) == 1
        assert model.gcd(7, 1) == 1
        assert model.gcd(8, 8) == 8
        assert model.gcd(18, 9) == 9
        assert model.gcd(100, 0) == 100
        assert model.gcd(0, 100) == 100

    def test_Q7(self):
        # TAs: due to name of function test_password has 'test_' head part, which is a 'keyword' in pytest,
        # please rewrite the student's code, change the function name to 'password' for testing.
        # If they have typo in their printing string, help them fix it and test again

        # test case 1: example 1
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_1.in', 'r+')
        fout = open('Q7/Q7_1.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_1.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_true_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 2: example 2
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_2.in', 'r+')
        fout = open('Q7/Q7_2.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_2.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 3: order doesn't matter
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_3.in', 'r+')
        fout = open('Q7/Q7_3.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_3.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_true_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 4: length
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_4.in', 'r+')
        fout = open('Q7/Q7_4.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_4.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 5: has number?
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_5.in', 'r+')
        fout = open('Q7/Q7_5.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_5.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 6: has lowercase?
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_6.in', 'r+')
        fout = open('Q7/Q7_6.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_6.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 7: has uppercase?
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_7.in', 'r+')
        fout = open('Q7/Q7_7.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_7.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

        # test case 8: has special char?
        build_cmd = 'python -c "from assignment_to_test import password; password()"'
        fin = open('Q7/Q7_8.in', 'r+')
        fout = open('Q7/Q7_8.out', 'w+')
        p = subprocess.Popen(build_cmd, shell=True, cwd=dir_work, stdin=fin, stdout=fout, stderr=subprocess.PIPE)
        fin.close()
        fout.close()
        p.communicate()
        out = open('Q7/Q7_8.out').read().replace('\r', '').rstrip()
        ans = open('Q7/Q7_false_ans.out').read().replace('\r', '').rstrip()
        assert ans in out

    def test_Q8(self):
        # TAs: if student's code use input() in their function, change it to the parameter of function
        # since the description of question not clear
        assert model.encrypt_string('Ottawa@2020') == 'Tyyf|fE7575'
        assert model.encrypt_string('Ojbk#1994') == 'Togp(6>>9'
        assert model.encrypt_string("PythonITI1120G%") == 'U~ymtsNYN6675L*'

    def test_Q9(self):
        # TAs: Same as above
        assert model.decrypt_string('Tyyf|fE7575') == 'Ottawa@2020'
        assert model.decrypt_string('Togp(6>>9') == 'Ojbk#1994'
        assert model.decrypt_string('U~ymtsNYN6675L*') == 'PythonITI1120G%'


if __name__ == '__main__':
    pytest.main()
