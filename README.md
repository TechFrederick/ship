# SHIP Haven

Services web app for SHIP, Student Homelessness Initiative Partnership of Frederick County

## Deployment

These instruction assume that you are already a collaborator
on SHIP's Heroku account.

The SHIP Haven web application is deployed to Heroku.
Follow the [Heroku documentation](https://devcenter.heroku.com/articles/git#creating-a-heroku-remote)
to add a Heroku remote
to your local repository clone.

To trigger a deploy, run:

```bash
$ git push heroku master
```

This will build a new Heroku slug,
run the `release` command
in the `Procfile`
to run any Django migrations,
and make the new version of the application live.

## Developer Setup

These commands are examples that can run
on a Mac terminal.
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

The application needs to read environment variables
to run properly
(because that's the Heroku model
of providing configuration via environment variables).
To set those variables locally,
copy the `.env.sample` file
as `.env`.

```bash
$ cp .env.sample .env
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
