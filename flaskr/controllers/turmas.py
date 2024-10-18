from flask import Blueprint, request, jsonify

# Criação do blueprint para turmas
turmas_blueprint = Blueprint('turmas', __name__)

# Lista temporária para armazenar as turmas
turmas = []

@turmas_blueprint.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify({'turmas': turmas})

@turmas_blueprint.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    # Validação básica dos dados, a linha a seguir verifica se a variável data não esta vazia e se cada item dentro das aspas tbm estão contidos nela
    if not data or 'descricao' not in data or 'professor' not in data or 'ativo' not in data:
        return jsonify({'erro': 'Dados inválidos ou incompletos'}), 400

    nova_turma = {
        'id': len(turmas) + 1,
        'descricao': data['descricao'],
        'professor': data['professor'],
        'ativo': data['ativo']  # Assumindo que é um campo booleano ou equivalente
    }
    turmas.append(nova_turma)
    return jsonify(nova_turma), 201

@turmas_blueprint.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            data = request.json
            turma['descricao'] = data.get('descricao', turma['descricao'])
            turma['professor'] = data.get('professor', turma['professor'])
            turma['ativo'] = data.get('ativo', turma['ativo'])
            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

@turmas_blueprint.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma removida'})
    return jsonify({'mensagem': 'Turma não encontrada'}), 404
