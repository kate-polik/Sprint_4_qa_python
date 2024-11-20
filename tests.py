import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Тест 0: пример теста
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):
        # создаем экземпляр (объект) класса BooksCollector

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # Тест 1: Добавление новой книги
    @pytest.mark.parametrize("book_name", ["Колобок", "Репка"])
    def test_add_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # Тест 2: Книга с некорректной длиной имени не добавляется
    @pytest.mark.parametrize("invalid_name", ["", "А" * 41])
    def test_add_new_book_invalid_length(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    # Тест 3: Установка жанра для книги
    @pytest.mark.parametrize("book_name, genre", [("Колобок", "Фантастика"), ("Репка", "Комедии")])
    def test_set_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre()[book_name] == genre

    # Тест 4: Невозможность установки жанра несуществующей книге
    def test_set_book_genre_invalid_book(self, collector):
        collector.set_book_genre("Несуществующая книга", "Фантастика")
        assert "Несуществующая книга" not in collector.get_books_genre()

    # Тест 5: Невозможность установки несуществующего жанра
    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book("Колобок")
        collector.set_book_genre("Колобок", "Несуществующий жанр")
        assert collector.get_books_genre()["Колобок"] == ""

    # Тест 6: Возврат жанра книги
    @pytest.mark.parametrize("book_name, genre", [("Колобок", "Фантастика"), ("Репка", "Детективы")])
    def test_get_book_genre(self, collector, book_name, genre):
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    # Тест 7: Возврат всех книг в словаре
    def test_get_books_genre(self, collector):
        collector.add_new_book("Колобок")
        collector.add_new_book("Репка")
        books = collector.get_books_genre()
        assert books == {"Колобок": "", "Репка": ""}

    # Тест 8: Возврат книг, подходящих детям
    def test_get_books_for_children(self, collector):
        collector.add_new_book("Колобок")
        collector.set_book_genre("Колобок", "Мультфильмы")
        collector.add_new_book("Баба Яга")
        collector.set_book_genre("Баба Яга", "Ужасы")
        children_books = collector.get_books_for_children()
        assert children_books == ["Колобок"]

    # Тест 9: Добавление книги в избранное
    @pytest.mark.parametrize("book_name", ["Колобок", "Репка"])
    def test_add_book_in_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name in favorites

    # Тест 10: Невозможность добавления в избранное несуществующей книги
    def test_add_book_in_favorites_not_exist(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        favorites = collector.get_list_of_favorites_books()
        assert "Несуществующая книга" not in favorites

    # Тест 11: Удаление книги из избранного
    @pytest.mark.parametrize("book_name", ["Колобок", "Репка"])
    def test_delete_book_from_favorites(self, collector, book_name):
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        favorites = collector.get_list_of_favorites_books()
        assert book_name not in favorites
