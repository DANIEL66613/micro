from flask import Blueprint, request, jsonify

# Criação do blueprint corretamente com letra maiúscula
alunos_blueprint = Blueprint('alunos', __name__)

# Lista para armazenar alunos
alunos = []

@alunos_blueprint.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'alunos': alunos})

@alunos_blueprint.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    novo_aluno = {
        'id': len(alunos) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'data_nascimento': data['data_nascimento'],
        'nota_primeiro_semestre': data['nota_primeiro_semestre'],
        'nota_segundo_semestre': data['nota_segundo_semestre'],
        'media_final': data['media_final']
    }
    alunos.append(novo_aluno)
    return jsonify(novo_aluno), 201


@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            data = request.json
            aluno['nome'] = data.get('nome', aluno['nome'])
            aluno['idade'] = data.get('idade', aluno['idade'])
            aluno['turma'] = data.get('turma', aluno['turma'])
            aluno['data_nascimento'] = data.get('data_nascimento', aluno['data_nascimento'])
            aluno['nota_primeiro_semestre'] = data.get('nota_primeiro_semestre', aluno['nota_primeiro_semestre'])
            aluno['nota_segundo_semestre'] = data.get('nota_segundo_semestre', aluno['nota_segundo_semestre'])
            aluno['media_final'] = data.get('media_final', aluno['media_final'])
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404


@alunos_blueprint.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404
