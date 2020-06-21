# ship

Services web app for SHIP, Student Homelessness Initiative Partnership of Frederick County

## Setup

These commands are examples that can run
on Mac terminal.
Most of the commands should be accurate
for Windows.
Differences are highlighted.

### Prerequisites

Ensure that a version of Python 3 is installed
on your machine.
You can check by running,

```bash
$ python3 -V
```

That command should print the version number
(note the capital V character!).

Deployment happens on Heroku.
You'll want the Heroku CLI installed.
See [The Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) documentation
for how to install the tools.

### Actions

Start a virtual environment.
The `source` command is specific to bash (i.e., Mac or Linux).
To start the virtual environment
on Windows,
check the `venv` documentation
in the [Python documentation](https://docs.python.org/3/library/venv.html).

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Install developer packages.

```bash
$ pip install -r requirements-dev.txt
```

Install application packages.

```bash
$ pip install -r requirements.txt
```

Apply Django database migrations locally.

```bash
$ ./manage.py migrate
```

Create a local superuser account.

```bash
$ ./manage.py createsuperuser
```

Start the local webserver.

```bash
heroku local
```

You can stop the webserver
by pressing `Control+C`.
