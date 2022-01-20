from .Movie import Movie
import os

class MovieList():
    _movies = []
    _path = 'list_movies.txt'
    
    @classmethod
    def _validate_movie(cls, movie):
        if isinstance(movie, Movie):
            return True
        raise Exception('You only can add Movies')
    
    @classmethod
    def add_movie(cls,movie):
        cls._validate_movie(movie)
        with HandlingFiles(cls._path, 'a') as file:
            file.write(f'{movie.name}\n')
    
    @classmethod
    def list_movies(cls):
        movies = ''
        try:
            with HandlingFiles(cls._path, 'r') as file:
                movies = file.read()
        except Exception as e:
            with HandlingFiles(cls._path, 'x') as file:
                movies = ''
        return movies
    
    @classmethod
    def delete_movie_list(cls):
        try:
            os.remove(cls._path)
        except Exception as e:
            pass

class HandlingFiles():
    def __init__(cls,name,operation_type):
        cls._validate_type(operation_type)
        cls._name = name
        cls._type = operation_type
        
    def _validate_type(cls, operation_type):
        if operation_type not in ('r', 'a', 'w', 'x'):
            raise Exception('Invalid Operation Type')
    
    def __enter__(cls):
        cls._name = open(cls._name, cls._type, encoding='utf8')
        return cls._name
    
    def __exit__(cls, type_error, value_error, traceback):
        if cls._name:
            cls._name.close()