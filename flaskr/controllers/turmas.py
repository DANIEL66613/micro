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