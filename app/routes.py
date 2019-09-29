from app import app

@app.routes('/')
@app.route('/index')
def index():
    return "Hello Lemurs"
