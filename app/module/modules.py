from app.extensions import db


class Mock(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    date = db.Column(db.DateTime, nullable=False)
    users_amount = db.Column(db.Integer, nullable=False)
    tasks = db.Column(db.String(500), nullable=False)
    place = db.Column(db.String(500), nullable=False)

    users = db.relationship("MockUserAssociation", back_populates="mocks")

    def __repr__(self):
        return (f'<Mock: id "{self.id}", date "{self.date}", users_amount "{self.users_amount}", '
                f'tasks "{self.tasks}", place "{self.place}">')


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False, unique=True)
    mocks_amount = db.Column(db.Integer, nullable=False)
    average_points = db.Column(db.Float, nullable=False)
    tasks = db.Column(db.String(500), nullable=False)
    max_amount = db.Column(db.Integer, nullable=False)

    mocks = db.relationship("Mock", backref='subject', lazy=True)
    temporary_mocks = db.relationship("TemporaryMock", backref='subject', lazy=True)

    def __repr__(self):
        return (f'<Subject: id "{self.id}", name "{self.name}", mocks amount "{self.mocks_amount}", '
                f'link to the tasks "{self.tasks}", max amount> "{self.max_amount}"')


# mock_user = db.Table('mock_user',
#                      db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#                      db.Column('mock_id', db.Integer, db.ForeignKey('mock.id'))
#                      )


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

    login = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)

    reg_date = db.Column(db.DateTime, nullable=False)

    mocks = db.relationship("MockUserAssociation", back_populates="users")

    def __repr__(self):
        return (f'<User: id "{self.id}", name "{self.name}", surname "{self.surname}", login "{self.login}", '
                f'password "{self.password}", registration date "{self.reg_date}">')


class TemporaryMock(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)

    users_amount = db.Column(db.Integer, nullable=False)
    max_amount = db.Column(db.Integer, nullable=False)

    date = db.Column(db.DateTime, nullable=False)
    tasks = db.Column(db.String(500), nullable=False)
    place = db.Column(db.String(500), nullable=False)

    def __repr__(self):
        return (f'<Mock: id "{self.id}", date "{self.date}", users amount "{self.users_amount}", '
                f'tasks "{self.tasks}", place "{self.place}">')


class MockUserAssociation(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), primary_key=True)
    mock_id = db.Column(db.Integer, db.ForeignKey("mock.id"), primary_key=True)

    task_link = db.Column(db.String(500), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    work_comments = db.Column(db.String(1000), nullable=False)

    users = db.relationship("User", back_populates="mocks")
    mocks = db.relationship("Mock", back_populates="users")

    def __repr__(self):
        return (f'<Mock-user: user_id "{self.user_id}", mock_id "{self.mock_id}", task link "{self.task_link}", '
                f'points "{self.points}", work comments "{self.work_comments}">')


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)
    surname = db.Column(db.String(150), nullable=False)
    points = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(500))

    def __repr__(self):
        return (f'<Comment: id "{self.id}", name "{self.name}", surname "{self.surname}", '
                f'points "{self.points}", comments "{self.comments}">')


