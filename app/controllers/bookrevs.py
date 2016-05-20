"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class bookrevs(Controller):
    def __init__(self, action):
        super(bookrevs, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('bookrev')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        if session.has_key('id'):
            return redirect('/logout')#TEMP
        return self.load_view('index.html')
    def register(self):
        #REGISTER FORM
        nud = request.form.copy()
        resp = self.models['bookrev'].createUser(nud)
        if unicode(resp).isnumeric():
            userfoo = self.models['bookrev'].getUserById(resp)
            session.update(userfoo)
            return redirect("/books")
        return redirect("/home")
    def login(self):
        #LOGIN FORM
        linp = request.form.copy() #login input
        attemptdict = self.models['bookrev'].login(linp)
        if attemptdict.has_key('invalid'):
            return redirect("/home")
        else:
            session.update(attemptdict)
            return redirect("/books")
    def logout(self):
        session.clear()
        return redirect("/home")
    def add(self):
        return self.load_view('add.html')
    def addbook(self):
        nbdict = request.form.copy()
        nbdict['user_id'] = session['id']
        bid = self.models['bookrev'].newBook(nbdict)
        target = "/books/" + str(bid)
        return redirect(target)
    def books(self):
        reviews  = self.models['bookrev'].getReviews()
        reviews.reverse()
        books = self.models['bookrev'].getAllBooks()
        return self.load_view('books.html', reviews=reviews, books = books)
    def specbook(self, id):
        book = self.models['bookrev'].getBookById(id)
        reviews = self.models['bookrev'].getReviewsByBookId(id)
        return self.load_view('specBook.html', book = book, reviews = reviews)
    def review(self):
        rinp=request.form.copy()
        self.models['bookrev'].addReview(rinp)
        target = "/books/" + str(rinp['book_id'])
        return redirect(target)