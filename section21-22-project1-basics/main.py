from models.MovieList import MovieList as ml
from models.Movie import Movie



def run():
    
    while True:
        print(f'MOVIE TEATHER'.center(100,'-'))
        print(f'1) Add movie\n2) List movies\n3) Delete\n4) Exit\n')
        selection = input('Choose an option: ')
        
        if selection == '1':
            movie_name = input('What it the name of the movie? ')
            ml.add_movie(Movie(movie_name))
            print('Movie successfully added.')
        elif selection == '2':
            print('All movies available:')
            print(ml.list_movies())
        elif selection == '3':
            print('Deleting all the movies...')
            ml.delete_movie_list()
        elif selection == '4':
            print('Bye :)')
            break
        else:
            print('Option incorrect, try again.')
        


if __name__ == '__main__':
    run()