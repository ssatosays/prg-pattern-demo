from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/post_only', methods=['POST'])
def post_only():
    print('-- post_only')
    print(request.form)
    print('-- post_only')
    return render_template('post_only.html')


@app.route('/post_redirect', methods=['POST'])
def post_redirect():
    print('-- post_redirect')
    print(request.form)
    print('-- post_redirect')
    return redirect(url_for('get'))


@app.route('/get', methods=['GET'])
def get():
    return render_template('get.html')


if __name__ == '__main__':
    app.run()
