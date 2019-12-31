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

### Install Dependencies Using a Virtual Environment
Afterwards, install all required packages. Its recommended to use a virtual
environment when installing Python packages. A virtual environment is an isolated
environment for Python projects. Each Python project would have its own dependencies
regardless of the dependencies other Projects will have. I use
[Pipenv](https://pipenv.readthedocs.io/en/latest/). Be sure to install Pipenv
before continueing...

### Create Virtual Environment using Python 3.7
Create virtual environment:
```bash
   pipenv --python 3.7
```
Run virtual environment environment:
```bash
   pipenv shell
```

### Download Chrome driver
Download the executable Chrome driver from
[ChromeDriver-Download](https://sites.google.com/a/chromium.org/chromedriver/downloads).
Note: Be sure to move the Chromedriver to the root directory of the project,
so we can reference the relative path of it.
