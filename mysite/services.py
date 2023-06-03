from mysite.models import Post
import re
import datetime

def is_url_occupied(url: str) -> bool:
    """Проверка на занятость url адреса"""
    return bool(Post.objects.filter(url=url))

# Проверка логина на длину
def is_login_valid(login):
    return len(login) > 1

# Проверка валидности почты
def match_mail(mail):
    if re.match(r"^[a-zA-Z-_.0-9]+@[a-zA-Z-_.0-9]+\.(?=.{2,3}$)[a-z]+", mail):
        return True
    else:
        return False

# Проверка номера телефона
def match_phone(phone):
    if re.match(r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$", phone):
        return True
    else:
        return False

# Проверка даты рождения
def check_date(date):
    print(date)
    if date > datetime.datetime.now().date():
        return False
    else:
        return True
