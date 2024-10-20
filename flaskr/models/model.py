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