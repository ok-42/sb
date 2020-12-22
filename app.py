from flask import Flask
print("import")

application = Flask(__name__)
print("application")


@application.route('/', methods=['GET'])
def index():
    return "Home page"
