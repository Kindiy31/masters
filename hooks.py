from flask import jsonify
import flask
import os
import sys

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))

sys.path.insert(0, parent_dir)
import os
app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=['GET', 'POST'])
def hand():
    return '403'
@app.route('/hook/', methods=['GET', 'POST'])
def webhook_handler():
    response_text = ('POST-запит оброблено успішно')
    os.system('git pull')
    os.system('systemctl restart masters')
    print(response_text)
    return jsonify({'message': response_text}), 200




if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)