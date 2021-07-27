1) sort imports
2) precommit (https://pre-commit.com/)
4) black
3) isort
5) makefile
6) requirements
7) tests
8) actions

-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
1) sort imports
	import standard
	import external
	import my_packages
	* ort all by alphabet


-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
2) precommit (https://pre-commit.com/)

1. install
	py --version # install python from python.org (all default)
	py -m pip --version  # pip is already installed with python:
	py -m pip install pre-commit # see warning /.../Scripts not in path
	py -m pre-commit --version # see warning /.../Scripts not in path

	error: typing "pre-commit" -> not found
	fix: windows evironment variables - add :
		C:\Users\user\AppData\Local\Programs\Python\Python39\Scripts

2. config file # file .pre-commit-config.yaml:
	default_stages: [commit, push]
	exclude: '^venv/*'
	repos:
	  - repo: https://github.com/asottile/seed-isort-config
	    rev: v1.9.3
	    hooks:
	      - id: seed-isort-config
	  - repo: https://github.com/pre-commit/mirrors-isort
	    rev: v4.3.21
	    hooks:
	      - id: isort
	  - repo: https://github.com/pre-commit/mirrors-autopep8
	    rev: v1.4.4
	    hooks:
	      - id: autopep8
	  - repo: https://github.com/pre-commit/pre-commit-hooks
	    rev: v2.3.0
	    hooks:
	      - id: fix-encoding-pragma
	      - id: trailing-whitespace
	      - id: end-of-file-fixer
	      - id: flake8
	      - id: double-quote-string-fixer
	      - id: check-docstring-first

3. put info to .git/hooks/pre-commit
	pre-commit install

4. test
	git add .
	git commit -m "smth"

	error: /usr/bin/env: 'python': Permission denied windows
	fix: winStartBttn - manage app execution aliases - turn all off
	reason: typing 'python' in cmd opens microsoft store
5. "# noqa" - skip bad lines
Adding # noqa to a line indicates that the linter (a program that automatically checks code quality) should not check this line. Any warnings that code may have generated will be ignored.

-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
3) isort
	already done in pre-commit

-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
4) black
	https://pypi.org/project/black/
	black - already in pre-commit
	can work standalone:
	- during 1st pre-commit - error and it fixes all styles
	- during 2nd pre-commit - no errors

Details (cmd or shell):
py -m pip install black
black test.py # removes double empty lines, adds spaces in x=x+3



add pyproject.toml to root for line length control (just add, nothing else!):
[tool.black]
line-length = 88
target-version = ['py37']

example: line-lenght = 8  => black test.py => will split all lines more then 8 !!!



-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
5) makefile
	just cmd commands: install requirements, run black etc
	* executing arbitrary commands to transform a source file to a target result

 "Make" - build automation tool that automatically builds executable programs
 	and libraries from source code by reading files called "Makefiles"
 Application:
 	manage any project where some files must be updated automatically from others whenever the others change

WINDOWS badway (using VS and not working):
	https://docs.microsoft.com/en-us/cpp/build/reference/nmake-reference?view=msvc-160
	1) run "Developer Command Prompt for VS 2019"
	2)
	cd C:\Users\user\Desktop\import_monster
	cd C:\Program Files (x86)\Microsoft Visual Studio\2019\Community\Common7\Tools
	run VsMSBuildCmd.bat
	run vcvars.bat
	run vcvars.bat
	install msvc extension in VS 2019 # c++ compiler; close VS - installation will start

WINDOWS goodway:
	download make from SourceForge: gnuwin32
	https://sourceforge.net/projects/gnuwin32/files/make/3.81/make-3.81.exe/download?use_mirror=iweb&download=

	install it
	go to the install folder
	C:\Program Files (x86)\GnuWin32\bin

	copy the all files in the bin to the folder that contains Makefile
	libiconv2.dll libintl3.dll make.exe

	open the cmd (you can do it with right click with shift) in the folder that contains Makefile and run
	.\make.exe
	.\make.exe install

	done.

	Plus, you can add arguments after the command, such as

	make.exe skel

# Makefile example start:-------------------
PACKAGES="seminar_package"

install:
	@pip install -r requirements.txt
# Makefile example end:-------------------



-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
6) requirements
	always add versions
	divide on 2 files: for developeres and for users

-----------------------------------------------------------
-----------------------------------------------------------
-----------------------------------------------------------
7) tests
7.1) unit test - built in (django uses), pytest - external but more convinient
7.2) pycharm feature - press play near fun and it will run pytest
7.3) create arguments (fun will be called 3 times with 3 different args)
	@pytest.mark.parametrize(
	    "test_case,expected_result",
	    [
	        ((1, [1, 2, 3]), [1, 1, 2, 3]), # (test_case, expected_result)
	        (([1, 2], (3, 4, 5)), [[1, 2], 3, 4, 5]), # (test_case, expected_result)
	        (("a", "asd"), ["a", "a", "s", "d"]), # (test_case, expected_result)
	    ],
	)
	def test_multiple_mutable_structure(self, test_case, expected_result):
	    assert list(prepend(*test_case)) == expected_result
7.4) fixtures - 2nd way to create arguments (generated args)
	@pytest.fixture
	def our_great_fixture():
	    lst = [1]
	    print(f"Our list: {lst!r}")

	    yield lst

	    lst.clear()
	    print(f"Our list: {lst!r}")


	def test_simple(our_great_fixture):
	    assert our_great_fixture == [1]

7.5) call smth before or after test
way1: automatically
* you dont need to pass any args to your test fun
* auto_fixture will be run by default
	@pytest.fixture(autouse=True)  # just put it in any file
	def auto_fixture():
	    print("Set Up")
	    yield
	    print("Tear Down")
way2: inside fixture:
	* setUp tearDown - before and after test in unitests



----------------------------------------------------
----------------------------------------------------
----------------------------------------------------
8) actions
8.1) hello world (my experience)
create github repo / actions / Python Package
* will create github_actions_test\.github\workflows\python-package.yml
# create tests/test_naive.py:
def func(x):
    return x + 1
def test_answer():
    assert func(3) == 4
after you pushed, go to Actions, see CommitsList => SUCCESS!
	* like on kaggle last commit is running in the cloud
	* cloud is docker, docker settings are in python-package.yml too
https://docs.github.com/en/actions/guides/building-and-testing-python
see github_actions_test.zip
8.2) import_monster errors:
isort puts adding to sys.path after importing parent package
fix: create tests/pathmagic, but don't use just sys.path.insert(0, '..')
