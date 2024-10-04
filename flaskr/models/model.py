def get_professores():
    return jsonify({'professores': professores})

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

    def delete_professor(professor_id):
    for professor in professores:
        if professor['id'] == professor_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404