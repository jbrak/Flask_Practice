# Flask_Practice

Repository about Experimenting with the Flask Web-Framework.

## Tutorials:

- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world

- https://flask.palletsprojects.com/en/1.1.x


## Activate/Deactivate the python virtual environment

- `source venv/bin/activate` to activate the environment

- `deactivate` to exit the environment

## Things to dependencies to install on the virtual environment

- `pip install flask-wtf`
- `pip install flask-sqlalchemy`
- `pip install flask-migrate`

## Access the sqlite command line on the Mac

The built-in version of the SQLite on the Mac is installed in the `/usr/bin` directory.  At the terminal, type the following commands to access it:

```
cd /usr/bin
sqlite3
```
`.help` at the sqlite command line shows all of the commands and `.quit` exits the SQL command line tool.

SQLite Studio can be installed from [here](https://sqlitestudio.pl/index.rvt).
