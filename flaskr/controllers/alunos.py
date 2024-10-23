from flask import Blueprint, request, jsonify
from ..models.aluno import listar_alunos, adicionar_aluno, atualizar_aluno, excluir_aluno, AlunoNaoEncontrado

alunos_blueprint = Blueprint('alunos', __name__)

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(listar_alunos()), 200

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    try:
        adicionar_aluno(data)
        return jsonify({'message': 'Aluno criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    data = request.json
    try:
        atualizar_aluno(aluno_id, data)
        return jsonify({'message': 'Aluno atualizado com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    try:
        excluir_aluno(aluno_id)
        return jsonify({'message': 'Aluno excluído com sucesso!'}), 200
    except AlunoNaoEncontrado:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400
