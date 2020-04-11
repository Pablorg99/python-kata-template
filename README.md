# Code Kata Python Template

This is the code kata template for python 3 created by [Pablo Rodríguez Guillén](https://github.com/Pablorg99)

### Step 1. Clone the repository

`git clone git@github.com:Pablorg99/python-kata-template.git`

### Step 2. Create your virtual environment

I use `virtualenv` for it. You can install it with `pip` (`pip install virtualenv`) or `apt` if you use a debian-based distribution (`sudo apt install virtualenv`).

To create the virtual environment with `python3` and activate it:

```
virtualenv -p python3 venv
source venv/bin/activate
```

### Step 3. Install the requirements

`pip install -r requirements.txt`

### Step 4. Execute tests

`python -m unittest -v`
