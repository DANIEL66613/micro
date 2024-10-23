from flask import Blueprint, request, jsonify
from ..models.professor import Professores, adicionar_professor, atualizar_professor, excluir_professor, listar_professores, ProfessorNaoEncontrado

professores_blueprint = Blueprint('professores', __name__)

@professores_blueprint.route('/professores', methods=['GET'])
def get_professores():
    try:
        professores = listar_professores()
        return jsonify(professores), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    if not data or 'nome' not in data or 'idade' not in data or 'materia' not in data:
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400

    try:
        adicionar_professor(data)
        return jsonify({'mensagem': 'Professor criado com sucesso!'}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    data = request.json
    try:
        atualizar_professor(professor_id, data)
        return jsonify({'mensagem': 'Professor atualizado com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@professores_blueprint.route('/professores/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    try:
        excluir_professor(professor_id)
        return jsonify({'mensagem': 'Professor removido com sucesso!'}), 200
    except ProfessorNaoEncontrado:
        return jsonify({'erro': 'Professor não encontrado'}), 404
    except Exception as e:
        return jsonify({'erro': str(e)}), 500
