from  usuarios_cr.config.mysqlconnection import * 

class User:
    db_name="user_schema"

    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']

    @classmethod  # User.create(data)
    def create(cls,data):
        solicitud = """INSERT INTO users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s,  NOW(), NOW()); """
        return connectToMySQL(cls.db_name).query_db(solicitud,data)

    @classmethod # User.get_all()
    def get_all(cls):
        solicitud = "SELECT * FROM users ;"
        resultado = connectToMySQL(cls.db_name).query_db(solicitud)
        #validar si el resultado contiene algo
        todas_los_users = []
        for user in resultado:
            todas_los_users.append(cls(user))
        return todas_los_users
    