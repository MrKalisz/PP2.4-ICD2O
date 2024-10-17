import os.path
import sys
import PP2_4

min: 6 test for different order, include pos, neg, 0s
years: 40, 4, 1999, 400, 1996, 200, 2000, 0

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0','1','2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 0\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['40']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['-1','-2','-3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: -3\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['4']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0','0','1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 0\n"

def test_q2_3(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1999']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is not a leap year\n"

def test_q1_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0','1','0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 0\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['400']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_5(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['2','1','1']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 1\n"

def test_q2_5(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1996']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_6(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['2','3','3']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 2\n"

def test_q2_6(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_7(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['1','-4','2']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: -4\n"

def test_q2_7(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['2000']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is a leap year\n"

def test_q1_8(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['0','0','0']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: In: In: 0\n"

def test_q2_8(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	input_values = ['200']

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP2_4.input = mock_input

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: Is not a leap year\n"


