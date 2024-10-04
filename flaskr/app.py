from flask import Flask, jsonify, request

meuApp = Flask(__name__)

professores = [
    {"nome":"caio","id":1,"idade":"30","materia":"matematica","observacoes":"abcd"},
    {"nome":"lucas","id":2,"idade":"30","materia":"portugues","observacoes":"abcde"},
]

turma = [
    {"descricao":"ASD1A","id":1,"professor":"caio","ativo": True},
    {"descricao":"ADS1B","id":2,"professor":"Odair","ativo": True},
]

alunos = [
    {"nome":"Daniel","id":1,"idade":"30","turma":"ADS1A","data_nascimento":"01/01/1900","nota_primeiro_semestre":"10","nota_segundo_semestre":"10","media_final":"10"},
    {"nome":"João","id":2,"idade":"30","turma":"ADS1A","data_nascimento":"01/01/1900","nota_primeiro_semestre":"10","nota_segundo_semestre":"10","media_final":"10"},
]

# -------------------------------ROTA HOME -----------------------------#


@meuApp.route('/')
def home():
    return "BEM VINDO A HOME DO SEU SERVIDOR FLASK!"



# ---------------- ROTAS PARA PROFESSORES ----------------
@meuApp.route('/professores', methods=['GET'])
def get_professores():
    return jsonify({'professores': professores})


@meuApp.route('/professores', methods=['POST'])
def create_professor():
    data = request.json
    novo_professor = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'materia': data['materia'],
        'observacoes': data['observacoes']
    }
    professores.append(novo_professor)
    return jsonify(novo_professor), 201


@meuApp.route('/professores/<int:professor_id>', methods=['PUT'])
def update_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            data = request.json
            professor['nome'] = data.get('nome', professor['nome'])
            professor['idade'] = data.get('idade', professor['idade'])
            professor['materia'] = data.get('materia', professor['materia'])
            professor['observacoes'] = data.get('observacoes', professor['observacoes'])
            return jsonify(professor)
    return jsonify({'mensagem': 'Professor não encontrado'}), 404


@meuApp.route('/professores/<int:professor_id>', methods=['DELETE'])
def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

# ---------------- ROTAS PARA TURMAS ----------------

@meuApp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify({'turmas': turma})


@meuApp.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    nova_turma = {
        'id': len(turma) + 1,
        'descricao': data['descricao'],
        'professor': data['professor'],
        'ativo': data['ativo']
    }
    turma.append(nova_turma)
    return jsonify(nova_turma), 201


@meuApp.route('/turmas/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for t in turma:
        if t['id'] == turma_id:
            data = request.json
            t['descricao'] = data.get('descricao', t['descricao'])
            t['professor'] = data.get('professor', t['professor'])
            t['ativo'] = data.get('ativo', t['ativo'])
            return jsonify(t)
    return jsonify({'mensagem': 'Turma não encontrada'}), 404


@meuApp.route('/turmas/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for t in turma:
        if t['id'] == turma_id:
            turma.remove(t)
            return jsonify({'mensagem': 'Turma removida'})
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

# ---------------- ROTAS PARA ALUNOS ----------------

@meuApp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'alunos': alunos})


@meuApp.route('/alunos', methods=['POST'])
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


@meuApp.route('/alunos/<int:aluno_id>', methods=['PUT'])
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


@meuApp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

if __name__ == '__main__':
     meuApp.run(debug=True)