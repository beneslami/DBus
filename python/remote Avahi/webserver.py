from flask import Flask
from avahi.service import AvahiService

avahi_name = ""

## Web server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'My avahi name is ' + avahi_name


if __name__ == "__main__":
    avahiservice = AvahiService("Simple webserver", "_http._tcp", 80)
    avahi_name = avahiservice.get_name()
    app.run(host='0.0.0.0', port=80)