
from database import db

class Reponse(db.Model):
    __tablename__ = 'reponses'

    id = db.Column(db.Integer, primary_key=True)
    texte = db.Column(db.Text, nullable=False)
    est_correcte = db.Column(db.Boolean, default=False)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    question = db.relationship('Question', backref=db.backref('reponses', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "texte": self.texte,
            "est_correcte": self.est_correcte,
            "question_id": self.question_id
        }
