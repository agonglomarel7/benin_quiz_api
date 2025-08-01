from database import db

class Question(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    texte = db.Column(db.Text, nullable=False)

    # Clé étrangère vers Category
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('questions', lazy=True))

    def to_dict(self):
        return {
            "id": self.id,
            "texte": self.texte,
            "category_id": self.category_id,
            "category": self.category.nom
        }
