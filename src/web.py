from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app("/sensors/")
def get_sensors:
    pass

@app.route('/sensor/<sensor_id>')
def get_sensor(sensor_id):
    pass


if __name__ == '__main__':
    app.debug = True
    app.run()


