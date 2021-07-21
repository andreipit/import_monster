1) sort imports
2) precommit (https://pre-commit.com/)
4) black
3) isort
5) makefile
6) requirements

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
