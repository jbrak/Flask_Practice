from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello Lemurs"

@app.route('/joe')
def joe():
    return "Hello Joe!"
