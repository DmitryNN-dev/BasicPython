import webbrowser

# позволяет добавлять функционал до и после выполнения некой функции

# декоратор:
def validator(func):
    def wrapper(url):
        # print("это текст до функции")
        if "." in url:
            func(url)
        else:
            print("неверный url")
        # print("это текст в конце функции")
    return wrapper

# задикорируем:
@validator
def open_url(url):
    webbrowser.open(url)

open_url("your_url_of_website")