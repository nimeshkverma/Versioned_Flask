from flask import Blueprint, jsonify

v1 = Blueprint('v1', __name__)


@v1.route('/dummy/', methods=['GET'])
def dummy_view():
    return jsonify(
        {
            "API_URL": "/1/dummy",
            "API_VERSION": 1
        }
    )
