# Job application test - Vivo's 4th platform

This repository contains coding developed for *Vivo's 4th Platform\** job application.

🐍 **Python** was the programming language chosen to solve the test.

*\* To learn more about [Vivo's 4th Platform](https://www.telefonica.com/en/web/press-office/-/telefonica-presents-aura-a-pioneering-way-in-the-industry-to-interact-with-customers-based-on-cognitive-intelligence).*

---

## Contents

![Code size in bytes](https://img.shields.io/github/languages/code-size/appinha/job_app_test-vivo_4th_platform?color=blueviolet)
![Number of lines of code](https://img.shields.io/tokei/lines/github/appinha/job_app_test-vivo_4th_platform?color=blueviolet)
![Code language count](https://img.shields.io/github/languages/count/appinha/job_app_test-vivo_4th_platform?color=blue)
![GitHub top language](https://img.shields.io/github/languages/top/appinha/job_app_test-vivo_4th_platform?color=blue)
![GitHub last commit](https://img.shields.io/github/last-commit/appinha/job_app_test-vivo_4th_platform)

* 📄 [Test subject (PDF)](prova_desenvolvedores_4p.pdf)
* 📁 [Exercice 1](ex1/) - an algorithm that counts how many times each element in a given array occurs in a given matrix.
* 📁 [Exercice 2](ex2/) - exercise 1 algorithm transformed into an API RESTful.
* 📁 [Exercice 3](ex3/) - an API that reads a race log file and calculates race results.

---

## Study reference

### Virtual Environment

**1. Install venv**
```
$ sudo apt install python3-venv
```

**2. Create new virtual environment** - creates `venv\`
```
$ cd my_flask_app
$ python3 -m venv venv
```

**3. Activate virtual environment** - `(venv) $` is shown in shell's prompt
```
$ source venv/bin/activate
```

**4. Deactivate virtual environment**
```
(venv) $ deactivate
```

### Numpy

**1. Installing Numpy**
```
(venv) $ pip install numpy
```

### Pandas

**1. Installing Pandas**
```
(venv) $ pip install pandas
```

### Flask

**1. Installing Flask and packages**
```
(venv) $ pip install Flask
(venv) $ pip install flask-restful
```

*Note: Within the virtual environment, you can use the command pip instead of pip3 and python instead of python3.*

**2. Verify the installation**
```
(venv) $ python3 -m flask --version
```

**3. Run the application**
```
(venv) $ export FLASK_APP=app.py
(venv) $ flask run
```

*Note: for Debug mode to be activated, run the following instead:*
```
(venv) $ export FLASK_ENV=development
(venv) $ export FLASK_APP=app.py
(venv) $ flask run
```

### Useful links

* [Flask installation - from documentation](https://flask.palletsprojects.com/en/1.1.x/installation/)
* [Flask installation - tutorial](https://linuxize.com/post/how-to-install-flask-on-ubuntu-18-04/)
* [Flask-RESTful documentation](https://flask-restful.readthedocs.io/en/latest/)
* [How do you POST a JSON file with curl??](https://gist.github.com/ungoldman/11282441)
* [RESTful-Flask parsing JSON Arrays with parse_args()](https://stackoverflow.com/questions/45613160/restful-flask-parsing-json-arrays-with-parse-args)
* [Pandas - convert minutes to second](https://stackoverflow.com/questions/50308629/python-pandas-column-convert-minutes-to-second)