# qa_python
# Добавил фикстуру для создания нового экземпляра класса BooksCollector перед каждым тестом
# Применил параметризацию для избежания повторяющихся кусков кода
# Тест test_add_new_book проверяет добавление книги с различными именами.
# Тест test_set_book_genre проверяет установку жанра для разных книг и жанров
# Тест test_get_books_for_children проверяет, что возвращаются только книги, подходящие для детей
# Тест test_get_books_with_specific_genre проверяет возвращение списка книг с указанным жанром.
# Тест test_add_book_in_favorites проверяет добавление книги в список избранного
# Тест test_delete_book_from_favorites проверяет удаление книги из списка избранного
# Тест test_get_list_of_favorites_books проверяет метод, который возвращает список избранных книг
# Тест test_get_books_genre проверяет возвращение словаря всех книг с их жанрами
# Тест test_add_and_get_favorites объединяет проверку добавления книги в избранное и получение списка избранных книг
# Тест test_set_book_genre_invalid проверяет, что установка жанра работает только для корректных книг и жанров.