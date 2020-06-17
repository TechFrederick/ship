# ship

Services web app for SHIP, Student Homelessness Initiative Partnership of Frederick County

## Setup

Start a virtual environment.

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

Start the local webserver.

```bash
$ ./manage.py runserver
```
