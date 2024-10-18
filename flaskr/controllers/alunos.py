from flask import Blueprint, request, jsonify

# Criação do blueprint corretamente com letra maiúscula
alunos_blueprint = Blueprint('alunos', __name__)


@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos())

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    return jsonify(adicionar_aluno(data)), 400

@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    data = request.json
    return jsonify(atualizar_aluno(id_aluno, data)), 404

@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    return jsonify(excluir_aluno(aluno_id)), 404
