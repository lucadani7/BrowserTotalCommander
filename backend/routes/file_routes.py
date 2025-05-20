from flask import Blueprint, request, jsonify

from backend.file_manager import FileManager

file_routes = Blueprint('file_routes', __name__)
file_manager = FileManager()


@file_routes.route('/list', methods=['GET'])
def list_files():
    path = request.args.get('path', '.')
    return jsonify(file_manager.list_files(path))


@file_routes.route('/copy', methods=['POST'])
def copy():
    data = request.json
    return jsonify(file_manager.copy(data.get('src'), data.get('dest')))


@file_routes.route('/delete', methods=['POST'])
def delete():
    return jsonify(file_manager.delete(request.json.get('path')))


@file_routes.route('/move', methods=['POST'])
def move():
    data = request.json
    return jsonify(file_manager.move(data.get('src'), data.get('dest')))


@file_routes.route('/create_file', methods=['POST'])
def create_file():
    return jsonify(file_manager.create_file(request.json.get('path')))


@file_routes.route('/create_folder', methods=['POST'])
def create_folder():
    return jsonify(file_manager.create_folder(request.json.get('path')))


@file_routes.route('/edit_file', methods=['POST'])
def edit_file():
    data = request.json
    return jsonify(file_manager.edit_file(data.get('path'), data.get('content')))
