import pytest

@pytest.fixture
def book_genre():
    books_genre = {}
    return books_genre

@pytest.fixture
def favorite():
    favorites = []
    return favorites

@pytest.fixture
def genres():
    genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    return genre

@pytest.fixture
def genre_age_ratings():
    genre_age_rating = ['Ужасы', 'Детективы']
    return genre_age_rating