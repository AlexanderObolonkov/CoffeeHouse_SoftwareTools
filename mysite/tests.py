import unittest

from django.core.exceptions import ValidationError
from django.core.validators import validate_email


def is_email(email: str) -> bool:
    """Обёртка для функкции validate_email Django с bool возвратом"""
    try:
        validate_email(email)
    except ValidationError:
        return False
    else:
        return True

class EmailTestCase(unittest.TestCase):
    """Класс терстирования валидации email"""
    def test_false_mail(self):
        """Тестирует список неправильных адресов на неправильность"""
        list_mail_incorrect = ['', '1', 'm1@', '@mail', 'бу@домен.com',
                               'xdd@mailru.', 'xddmail.ru', 'xdd@mailru',
                               'xd d@mail.ru', 'x@dd4@mail.ru',
                               'xd..d@mail.ru', 'xd"d@mail.ru']
        for email in list_mail_incorrect:
            self.assertFalse(is_email(email))

    def test_true_mail(self):
        """Тестирует список неправильных адресов на неправильность"""
        list_mail_correct = ['m.m@mail.ru', 'm1@gmail.com',
                             'disp.style.email.with+symbols@example.com',
                             'other.email-with-dash@axample.com',
                             'x@emaple.com', '"unusual.@.@unusual"@em.com',
                             '01snab@mail.ru', 'example@localhost',
                             'DiFfReNtReGiStEr123@gmail.com',
                             'support@host-food.ru', 'inbox@0-pro.ru',
                             'an@7300744.ru']
        for email in list_mail_correct:
            self.assertTrue(is_email(email))


if __name__ == '__main__':
    unittest.main()
