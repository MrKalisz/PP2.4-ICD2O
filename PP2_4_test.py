import os.path
import sys
import PP2_4

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 36 is even\n"

def test_q2_4(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: student\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q1()
	captured = capsys.readouterr()
	assert captured.out == "In: 23 is odd\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP2_4.py")
		assert exists
	except:
		sys.exit()

	PP2_4.q2()
	captured = capsys.readouterr()
	assert captured.out == "In: teacher\n"
