from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Aluno(db.Model):
    __tablename__ = 'alunos'
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    turma_id = db.Column(db.Integer, db.ForeignKey('turmas.id'), nullable=False)
    data_nascimento = db.Column(db.String(10), nullable=False)
    nota_primeiro_semestre = db.Column(db.Float)
    nota_segundo_semestre = db.Column(db.Float)
    media_final = db.Column(db.Float)
    
    def __repr__(self):
        return f"<Aluno {self.nome}>"
