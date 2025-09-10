#!flask/bin/python
from flask import Flask, request, Response

app = Flask(__name__)

post_counter = 0
get_counter = 0


@app.route('/', methods=["POST", "GET"])
def root():
    return Response(status=200)
#Add post request
@app.route('/count', methods=["POST", "GET"])
def count():
    global post_counter, get_counter
    if request.method == "POST":
        post_counter += 1
    else:
        get_counter += 1
    return f"The counter is: POST={post_counter}, GET={get_counter}"

if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')
