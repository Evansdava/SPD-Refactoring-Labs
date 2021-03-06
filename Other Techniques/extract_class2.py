# by Kami Bigdely
# Extract class


class Actor():
    """Class for actors"""

    def __init__(self, first_name, last_name, birth_year, movies, email):
        """Initialize variables"""
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email


e_debicki = Actor('elizabeth', 'debicki', 1990,
                  ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy',
                   'The Great Gatsby'], 'deb@makeschool.com')

j_carrey = Actor('Jim', 'Carrey', 1962,
                 ['Ace Ventura', 'The Mask', 'Dubm and Dumber',
                  'The Truman Show', 'Yes Man'], 'jim@makeschool.com')

actors = [e_debicki, j_carrey]


def send_hiring_email(email):
    print("email sent to: ", email)


for actor in actors:
    if actor.birth_year > 1985:
        print(actor.first_name, actor.last_name)
        print('Movies Played: ', end='')
        for m in actor.movies:
            print(m, end=', ')
        print()
        send_hiring_email(actor.email)
