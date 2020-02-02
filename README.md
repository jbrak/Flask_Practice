# Flask_Practice

Repository about Experimenting with the Flask Web-Framework.

## Tutorials:

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

- https://flask.palletsprojects.com/en/1.1.x


## Activate/Deactivate the python virtual environment
- `python3 -m venv venv` to create the environment

- `source venv/bin/activate` to activate the environment

- `deactivate` to exit the environment

## Things to dependencies to install on the virtual environment

- `pip3 install flask-wtf`
- `pip3 install flask-sqlalchemy`
- `pip3 install flask-migrate`
- `pip3 install Flask-APScheduler`

## Access the sqlite command line on the Mac

The built-in version of the SQLite on the Mac is installed in the `/usr/bin` directory.  At the terminal, type the following commands to access it:

```
cd /usr/bin
sqlite3
```
`.help` at the sqlite command line shows all of the commands and `.quit` exits the SQL command line tool.

SQLite Studio can be installed from [here](https://sqlitestudio.pl/index.rvt).

## Database Session commands

```
from app import db
from app.models import Data
from datetime import datetime

#Sample writing Data
db.session.rollback()
d = Data(date = datetime.now(), temp = 32.3)
db.session.add(d)
db.session.commit()

# To see the data
data = Data.query.all()
data
```
