from app import server
from flask import render_template

from tcbp_respon import app


@server.route("/")
def load_home():
    return render_template('home.html')

if __name__ == '__main__':
    server.run(host="192.168.1.10", port=2222, debug=True)