# Exercise 2

## Subject

	"Transforme o algoritmo anterior em uma API Rest. Você receberá como
	parâmetro uma lista com os valores de An e deverá retornar a saída do
	algoritmo no formato JSON."

## Contents

* [activate.sh](activate.sh) - shell script to set and/or activate the virtual environment.
* [run.sh](run.sh) - shell script to run the application.
* [app.py](app.py) - application's source code.
* [list.json](list.json) - JSON file to be used as input in the application.
* [post.sh](post.sh) - shell script to POST `list.json` to the application.
* [requirements.txt](requirements.txt) - list of all necessary packages to run the application.

## How to run

After cloning this repository, `cd` to `ex2` directory and follow the instructions bellow.

**1. To set and/or activate the virtual environment, run:**
```
$ source activate.sh
```
*Note: if the virtual environment is not yet set, you'll be prompted to install/update `python3-venv` and a `venv` directory will be created.*

**2. Once inside `venv`, to start the application, run:**
```
(venv) $ source run.sh
```
*Note: when running the virtual environment for the first time, you'll be prompted to install all necessary packages to run the application.*

**3. Edit the list values in `list.json` as you like.**
```
{
	"list": [1, 2, 3]
}
```
*Note: the application only accepts values within the range 0 <= value <= 15.*

**4. To input this list to the application, in another shell window run:**
```
$ sh post.sh
```

**5. To kill the application press `ctrl+C` and to deactivate the virtual environment, run:**
```
(venv) $ deactivate
```

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