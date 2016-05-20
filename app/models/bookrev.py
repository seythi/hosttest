""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class bookrev(Model):
    def __init__(self):
        super(bookrev, self).__init__()
    def createUser(self, nud): #new user data
        if(True): #TODO validation
            nud['pword'] = self.bcrypt.generate_password_hash(nud['pword'])
            query="INSERT INTO users (first_name, alias, email, created_at, updated_at, pwhash) VALUES(:fname, :alias, :email, NOW(), NOW(), :pword);SELECT SCOPE_IDENTITY()"
            return self.db.query_db(query, nud)
    def getUserById(self, uid):
        query="SELECT * from users where id = :id"
        data={'id': uid}
        return self.db.query_db(query, data)[0]
    def login(self, linp):
        query="SELECT * from users where email=:email"
        tRecord=self.db.query_db(query, linp)[0]
        hashbool = self.bcrypt.check_password_hash(tRecord['pwhash'], linp['password'])
        if hashbool:
            return tRecord
        else:
            return {'invalid':True}
    def getAllBooks(self):
        query = "SELECT * from books"
        return self.db.query_db(query)
    # def getBookById(self, *args):
    #     if(len(args) == 1):
    #         data = {'id': args[0], 'col' : '*'}
    #     else:
    #         data = {'id': args[0], 'col' : args[1]}
    #     query = "SELECT :col from books where id = :id "
    #     return self.db.query_db(query, data)[0]
    def getBookById(self, args):
        
        data = {'id': args}
        
        query = "SELECT * from books where id = :id "
        return self.db.query_db(query, data)[0]
    def getReviews(self):
        query = "SELECT * from books RIGHT JOIN reviews ON books.id = reviews.book_id LEFT JOIN users on users.id = reviews.user_id;"
        out=self.db.query_db(query)
        if not out:
            return [{'content':'nocontent'}]
        return out
    def getReviewsByBookId(self, id):
        query= "SELECT * from reviews LEFT JOIN users on users.id = reviews.user_id where book_id = :id"
        data = {'id':id}
        return self.db.query_db(query,data)
    def getReviewTitlesByUser(self, uid):
        query = "SELECT * from books RIGHT JOIN reviews ON books.id = reviews.book_id LEFT JOIN users on users.id = reviews.user_id where users.id = :uid"
        data = {'uid':uid}
        return self.db.query_db(query, data)
    def newBook(self, nbdict):
        query = "INSERT into books(title, author) VALUES(:title, :author); SELECT SCOPE_IDENTITY();"
        nbdict['bid'] = self.db.query_db(query, nbdict)
        query2 = "INSERT into reviews(content, rating, user_id, book_id) VALUES(:content, :rating, :user_id, :bid)"
        self.db.query_db(query2, nbdict)
        return nbdict['bid']
    def addReview(self, rinp):
        query = "INSERT into reviews(content, rating, user_id, book_id) VALUES(:content, :rating, :user_id, :book_id)"
        return self.db.query_db(query, rinp)
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """