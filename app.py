from application import app
from application.routes import *


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)