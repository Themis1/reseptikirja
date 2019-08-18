from application import db
from application.models import Base

from sqlalchemy.sql import text

user_role = db.Table("userrole", db.Column("user_id", db.Integer, db.ForeignKey("account.id", ondelete="CASCADE")), db.Column("role_id", db.Integer, db.ForeignKey("role.id")))

class Role(Base):
    name = db.Column(db.String(30), nullable = False, unique=True)
    superuser = db.Column(db.Boolean, default=False, nullable=False, unique=False)

    def __init__(self, role_name, superuser = False):
        self.name = role_name
        self.superuser = superuser

    @staticmethod
    def get_default_role():
        return Role.query.filter_by(name="USER").first()

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(30), nullable=False)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)

    roles = db.relationship("Role", secondary=user_role, lazy="subquery", backref=db.backref("users", passive_deletes=True, lazy=True))
    reseptit = db.relationship("Resepti", backref='account', passive_deletes=True, lazy=True)

    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_superuser(self):
        su_role = Role.query.filter_by(superuser=True).first()
        return su_role.name in self.get_roles()

    def set_default_role(self):
        user_role = Role.get_default_role()

        if user_role.name not in self.get_roles():
            self.roles.append(user_role)
        db.session.commit()

    def get_roles(self):
        return [r.name for r in self.roles]

    def has_resepti_with_id(self, resepti_id):
        return any(p.id == int(resepti_id) for p in self.reseptit)


    def user_reseptit(account_id):
        stmt = text("SELECT Resepti.name FROM Resepti"
                    " LEFT JOIN Account ON Account.id = Resepti.account_id"
                    " WHERE Resepti.account_id  = account_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"name":row[0]})
        return response


#    def roles(self):
#        return ["ADMIN"]

#    @staticmethod
#    def find_users_with_no_vnas():
#        stmt = text("SELECT Account.id, Account.name FROM Account"
#                    " LEFT JOIN Vna ON Vna.account_id = Account.id"
#                    " LEFT JOIN Mmma ON Mmma.account_id = Account.id"
#                    " GROUP BY Account.id"
#                    " HAVING COUNT(Vna.id) = 0")
#        res = db.engine.execute(stmt)
#
#        response = []
#        for row in res:
#            response.append({"id":row[0], "name":row[1]})
#
#        return response


