# Captain D's Web Scraper
This project is for the analysis and reporting of the restaurant ratings at
select locations for Captain D's. If you are interested in the setup of the
web scraper, then read below.

## Getting Started
* Install Latest Version of Python. If you do not have Python on your machine,
install the latest [version](https://www.python.org/downloads/).
You can check current version of Python3 by running the following command:
```bash
python3 --version
```

* Install Pipenv
It's recommended to use a virtual
environment when installing Python packages. A virtual environment is an isolated
environment for Python projects. Each Python project would have its own dependencies
regardless of the dependencies other Projects will have. I use
[Pipenv](https://pipenv.readthedocs.io/en/latest/). Be sure to install Pipenv
before continueing...

* Download Chrome driver
Download the executable Chrome driver from
[ChromeDriver-Download](https://sites.google.com/a/chromium.org/chromedriver/downloads).
Download the current version of Chrome you are using. I happen to be using V79.

Note: Be sure to move the Chromedriver to the root directory of the project,
so we can reference the relative path of it.

Once you have...
1. installed the latest version of [Python](https://www.python.org/downloads/),
2. installed [Pipenv](https://pipenv.readthedocs.io/en/latest/),
3. downloaded the [ChromeDriver-Download](https://sites.google.com/a/chromium.org/chromedriver/downloads),

... you can now follow the below steps to cloning the repo and running
the Python script!

#### Clone Repo
```bash
   git clone https://github.com/josephiznot/restaurant-reviewer.git && cd restaurant-reviewer
```

#### Install dependencies
```bash
   pipenv install
```
#### Run Python script using virtual environment:
```bash
   pipenv run python index.py
```
