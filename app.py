
# app.py

from flask import Flask

from controllers import users_controller
from repositories.factories import create_users_repository

app = Flask(__name__)



app.add_url_rule('/api/users', 'get_all_users', users_controller.get_all_users_handler, methods=['GET'])
app.add_url_rule('/api/users/<user_id>', 'get_user_by_id', users_controller.get_user_by_id_handler, methods=['GET'])
app.add_url_rule('/api/users', 'add_user', users_controller.add_user_handler, methods=['POST'])
app.add_url_rule('/api/users/<user_id>', 'update_user', users_controller.update_user_handler, methods=['PUT', 'PATCH'])
app.add_url_rule('/api/users/<user_id>', 'remove_user', users_controller.remove_user_handler, methods=['DELETE'])

if __name__ == '__main__':
    app.run(debug=True)