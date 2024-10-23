from ..config import db

class Turma(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))  # Nome da turma
    descricao = db.Column(db.String(100))
    professor = db.Column(db.String(100))
    ativo = db.Column(db.Boolean)

    def __init__(self, nome, descricao, professor, ativo):
        self.nome = nome
        self.descricao = descricao
        self.professor = professor
        self.ativo = ativo

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'professor': self.professor,
            'ativo': self.ativo
        }

class TurmaNaoEncontrada(Exception):
    pass

def turma_por_id(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada
    return turma.to_dict()

def listar_turmas():
    turmas = Turma.query.all()
    return [turma.to_dict() for turma in turmas]

def adicionar_turma(turma_data):
    nova_turma = Turma(
        nome=turma_data['nome'],
        descricao=turma_data['descricao'],
        professor=turma_data['professor'],
        ativo=turma_data['ativo']
    )
    db.session.add(nova_turma)
    db.session.commit()

def atualizar_turma(id_turma, novos_dados):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada
    turma.nome = novos_dados['nome']
    turma.descricao = novos_dados['descricao']
    turma.professor = novos_dados['professor']
    turma.ativo = novos_dados['ativo']
    db.session.commit()

def excluir_turma(id_turma):
    turma = Turma.query.get(id_turma)
    if not turma:
        raise TurmaNaoEncontrada
    db.session.delete(turma)
    db.session.commit()
