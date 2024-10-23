import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_three_books(self, book_genre):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Буратино')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 3

    def test_set_book_genre_add_book_with_genre(self, book_genre):
        name = 'Гордость и предубеждение и зомби'
        genre = 'Ужасы'
        collector = BooksCollector()
        if name in collector.books_genre:
            collector.books_genre[name] == genre
            collector.set_book_genre(name, genre)
            assert collector.books_genre('Гордость и предубеждение и зомби') == 'Ужасы'
        else:
            assert 'Book not found!'

    def test_set_book_genre_add_book_with_genre(self, book_genre):
        name = 'Буратино'
        genre = 'Мультфильмы'
        collector = BooksCollector()
        if name in collector.books_genre:
            collector.books_genre[name] == genre
            collector.set_book_genre(name, genre)
            assert collector.books_genre('Буратино') == 'Мультфильмы'
        else:
            assert 'Book not found!'

    def test_set_book_genre_add_book_without_genre(self, book_genre):
        collector = BooksCollector()
        genre = None
        collector.set_book_genre('Дубровский', genre)
        assert collector.set_book_genre('Дубровский', genre) not in collector.books_genre

    def test_get_book_genre_from_books_genre(self, book_genre):
        name = 'Гордость и предубеждение и зомби'
        collector = BooksCollector()
        if name in collector.books_genre:
            collector.get_book_genre(name)
            assert collector.books_genre('Гордость и предубеждение и зомби') == 'Ужасы'

    def test_get_books_with_specific_genre_show_books(self, book_genre, genres):
        collector = BooksCollector()
        key = 'Ужасы'
        for key in collector.genre:
            if key in collector.books_genre.items():
                key == collector.genre
                assert collector.get_books_with_specific_genre('Ужасы') == ['Гордость и предубеждение и зомби']

    def test_get_books_genre_show_books_genre(self, book_genre):
        collector = BooksCollector()
        collector.get_books_genre()
        assert collector.get_books_genre() == collector.books_genre

    def test_get_books_for_children_show_books(self, book_genre, genre_age_ratings):
        collector = BooksCollector()
        name = 'Буратино'
        genre = 'Мультфильмы'
        for name, genre in collector.books_genre.items():
            if genre not in collector.genre_age_rating and genre in collector.genre:
                assert collector.get_books_for_children() == ['Буратино']
            else:
                assert 'Books not found!'

    def test_add_book_in_favorites_add_one_book(self, book_genre, favorite):
        collector = BooksCollector()
        name = 'Гордость и предубеждение и зомби'
        if name in collector.books_genre:
            if name not in collector.favorites:
                collector.add_book_in_favorites(name)
                assert 'Гордость и предубеждение и зомби' in collector.favorites

    def test_add_book_in_favorites_add_one_book(self, book_genre, favorite):
        collector = BooksCollector()
        name = 'Что делать, если ваш кот хочет вас убить'
        if name in collector.books_genre:
            if name not in collector.favorites:
                collector.add_book_in_favorites(name)
                assert 'Что делать, если ваш кот хочет вас убить' in collector.favorites

    def test_get_list_of_favorites_books_show_books(self, favorite):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == collector.favorites

    def test_delete_book_from_favorites_delete_one_book(self, favorite):
        collector = BooksCollector()
        name = 'Что делать, если ваш кот хочет вас убить'
        if name in collector.favorites:
            collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')
            assert 'Что делать, если ваш кот хочет вас убить' not in collector.favorites
        else:
            'Book not found!'

@pytest.mark.parametrize('name', ['', 'Девушка, которая взрывала воздушные замки'])
def test_add_new_book_add_incorrect_name_books(name):
    collector = BooksCollector()
    if name == None:
        assert collector.add_new_book(name) == 'Incorrect books name!'

@pytest.mark.parametrize('genre', ['Ужасы', 'Детективы'])
def test_get_books_for_children_incorrect_genre(genre):
    collector = BooksCollector()
    for name, genre in collector.books_genre.items():
        if genre in collector.genre_age_ratings:
            assert name not in collector.get_books_for_children()