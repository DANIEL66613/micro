class Turma(db.Model):
    __tablename__ = 'turmas'
    
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(200), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professores.id'), nullable=False)
    ativo = db.Column(db.Boolean, default=True)
    alunos = db.relationship('Aluno', backref='turma', lazy=True)
    
    def __repr__(self):
        return f"<Turma {self.descricao}>"
