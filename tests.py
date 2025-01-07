from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2


import pytest


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.mark.parametrize(
    "book_name, expected",
    [("Дюна", True), ("Оно", True), ("", False), ("A" * 41, False)],
)
def test_add_new_book(collector, book_name, expected):
    collector.add_new_book(book_name)
    assert (book_name in collector.get_books_genre()) == expected


@pytest.mark.parametrize(
    "book_name, genre, expected_genre",
    [
        ("Дюна", "Фантастика", "Фантастика"),
        ("Оно", "Ужасы", "Ужасы"),
        ("Дюна", "Неизвестный жанр", ""),
        ("Такой книги нет", "Фантастика", None),
    ],
)
def test_set_book_genre(collector, book_name, genre, expected_genre):
    collector.add_new_book("Дюна")
    collector.add_new_book("Оно")
    collector.set_book_genre(book_name, genre)
    assert collector.get_book_genre(book_name) == expected_genre


@pytest.mark.parametrize(
    "books, genre, expected",
    [
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], "Фантастика", ["Дюна"]),
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], "Ужасы", ["Оно"]),
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], "Детективы", []),
    ],
)
def test_get_books_with_specific_genre(collector, books, genre, expected):
    for book_name, book_genre in books:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
    result = collector.get_books_with_specific_genre(genre)
    assert result == expected


@pytest.mark.parametrize(
    "books, expected",
    [
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], ["Дюна"]),
        ([("Дюна", "Фантастика"), ("Враг", "Детективы")], ["Дюна"]),
        ([("Моана", "Мультфильмы"), ("Холоп", "Комедии")], ["Моана", "Холоп"]),
    ],
)
def test_get_books_for_children(collector, books, expected):
    for book_name, book_genre in books:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)
    result = collector.get_books_for_children()
    assert result == expected


@pytest.mark.parametrize(
    "book_name, expected",
    [
        ("Дюна", True),
        ("Оно", True),
        ("Такой книги нет", False),
    ],
)
def test_add_book_in_favorites(collector, book_name, expected):
    if book_name != "Такой книги нет":
        collector.add_new_book(book_name)
    collector.add_book_in_favorites(book_name)
    result = book_name in collector.get_list_of_favorites_books()
    assert result == expected


@pytest.mark.parametrize(
    "initial_favorites, book_to_remove, expected",
    [
        (["Дюна", "Оно"], "Дюна", ["Оно"]),
        (["Дюна", "Оно"], "Оно", ["Дюна"]),
        (["Дюна", "Оно"], "Такой книги нет", ["Дюна", "Оно"]),
    ],
)
def test_delete_book_from_favorites(
    collector, initial_favorites, book_to_remove, expected
):
    for book in initial_favorites:
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
    collector.delete_book_from_favorites(book_to_remove)
    result = collector.get_list_of_favorites_books()
    assert result == expected


@pytest.mark.parametrize(
    "books, favorites, expected",
    [
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], ["Дюна"], ["Дюна"]),
        ([("Дюна", "Фантастика"), ("Оно", "Ужасы")], ["Дюна", "Оно"], ["Дюна", "Оно"]),
        ([("Дюна", "Фантастика")], [], []),
    ],
)
def test_get_list_of_favorites_books(collector, books, favorites, expected):
    for book_name, genre in books:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    for favorite in favorites:
        collector.add_book_in_favorites(favorite)
    result = collector.get_list_of_favorites_books()
    assert result == expected


@pytest.mark.parametrize(
    "books, expected",
    [
        (
            [("Дюна", "Фантастика"), ("Оно", "Ужасы")],
            {"Дюна": "Фантастика", "Оно": "Ужасы"},
        ),
        ([("Враг", "Детективы")], {"Враг": "Детективы"}),
        ([], {}),
    ],
)
def test_get_books_genre(collector, books, expected):
    for book_name, genre in books:
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
    result = collector.get_books_genre()
    assert result == expected


@pytest.mark.parametrize(
    "book_name, genre, expected",
    [
        ("Дюна", "Фантастика", True),
        ("Оно", "Ужасы", True),
        ("Такой книги нет", "Фантастика", False),
    ],
)
def test_add_and_get_favorites(collector, book_name, genre, expected):
    if book_name != "Такой книги нет":
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.add_book_in_favorites(book_name)
    result = book_name in collector.get_list_of_favorites_books()
    assert result == expected

@pytest.mark.parametrize(
     "book_name, genre, expected",
    [
        ("Дюна", "Фантастика", "Фантастика"),
        ("Оно", "Ужасы", "Ужасы"),
        ("Такой книги нет", None, None),
      ],
)
def test_get_book_genre(collector, book_name, genre, expected):
    if book_name != "Такой книги нет":
          collector.add_new_book(book_name)
          collector.set_book_genre(book_name, genre)
    result = collector.get_book_genre(book_name)
    assert result == expected
