from flask import Flask
print("import")

application = Flask(__name__)
print("application")


@application.route('/', methods=['GET'])
def index():
    return "Home page"


print(__name__)
if __name__ == "__main__":
    print("run")
    application.run()
