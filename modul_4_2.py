def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()

test_function()


#при вызове функции inner_function вне функции test_function программа будет выдавать ошибку,
# т к этой функции нет в глобальном пространстве.
def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


inner_function()
