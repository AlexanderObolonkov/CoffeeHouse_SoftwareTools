from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug
from mysite.services import is_url_occupied, is_login_valid, match_mail, match_phone, check_date,is_name_valid

class URLTestCase(TestCase):
    """Тестовый случай URL"""

    @staticmethod
    def is_url(url: str) -> bool:
        """Обёртка для проверки url"""
        try:
            validate_slug(url)
        except ValidationError:
            return False
        else:
            return True

    def test_false_url(self):
        """Проверка негативных случаев"""
        list_url_incorrect = ['##gfgf', 'русские_буквы', '  ', 'spa ces',
                              '!someslug', '!@#$%^&*()"№;%:?*.', '異体字']
        for url in list_url_incorrect:
            self.assertFalse(URLTestCase.is_url(url))

    def test_true_url(self):
        """Проверка позитивных случаев"""
        list_url_correct = ['valid', 'still_valid', '1234', 'still-valid']
        for url in list_url_correct:
            self.assertTrue(URLTestCase.is_url(url))


class CreatedDateTestCase(TestCase):
    @staticmethod
    def is_correct_date(date_string: str) -> bool:
        """Обёртка для проверки соответсвия даты формату"""
        try:
            datetime.strptime(date_string, '%d.%m.%Y')
        except ValueError:
            return False
        else:
            return True

    def test_false_url(self):
        """Проверка негативных случаев"""
        list_incorrect_date = ['мусор', '23/02/2004', '1.2.23', '2000-04-12',
                               '30.02.2004', '1.1.1', '120.50.2004']
        for date_ in list_incorrect_date:
            self.assertFalse(CreatedDateTestCase.is_correct_date(date_))

    def test_correct_date(self):
        """Проверка позитивных случаев"""
        list_correct_date = ['10.02.2004', '01.01.1991', '29.02.2004']
        for date_ in list_correct_date:
            self.assertTrue(CreatedDateTestCase.is_correct_date(date_))


class EmailTestCase(TestCase):
    def test_match_mail_true(self):
        emails = ["gajkin.kirill@yandex.ru", "kirill.new@gmail.com", "yuriy@mail.com", "sasha@gmail.com", "alexandra.haskova@yandex.ru",
                  "kirill.gaykin@gmail.com", "ricardrajonhart@gmail.com", "vovapupkin@mail.com", "genius877@yandex.ru", "vasilievskiy.central@yandex.ru"];
        for i in emails:
            self.assertTrue(match_mail(i), f"{i} mail is not valid")

    def test_match_mail_false(self):
        emails = ["1", "kirill", "@", "@gmail", "kiriLL@gmail", "kirill.gmail.com", "kirill.ru", "kirill@.ru",
                  "kirill@gmailcom", "kirill@gmail.r", "kirill@gmail.comma", "123456789"];
        for i in emails:
            self.assertFalse(match_mail(i), f"{i} mail is valid")


class PhoneTestCase(TestCase):
    def test_match_phone_true(self):
        phones = ['89118445162', '+79118445162', '+7(911) 844 51-62', '8445162', '844-51-62', '84451-62', '844-5162']
        for i in phones:
            self.assertTrue(match_phone(i), f"phone is not valid")

    def test_match_phone_false(self):
        phones = ['8', '---', '12345', '321', '+7', '+7888888888888888']
        for i in phones:
            self.assertFalse(match_phone(i), f"phone is valid")
class NameTestCase(TestCase):
    """Проверка имени компании"""
    def test_name_true(self):
        """Проверка позитивных случаев"""
        names=["company","1_compane","i","random_company"]
        for name in names:
            self.assertTrue(is_name_valid(name))
    def test_name_false(self):
        """Проверка негативных случаев"""
        names=["","123","15434334589"]
        for name in names:
            self.assertFalse(is_name_valid(name))

class PartnerEmailTestCase(TestCase):
    """Проверка email партнеров"""
    def test_email_true(self):
        """Проверка позитивных случаев"""
        emails=["coompany@email.com","company_with_1_digit@yandex.ru","company.dotted.email@gmail.com"]
        for email in emails:
            self.assertTrue(match_mail(email))
    def test_email_false(self):
        """Проверка негативных случаев"""
        emails=["1423","company","compane@","company@mail","compane@mailru","company.mail.ru","company@company@mail.ru"]
        for email in emails:
            self.assertFalse(match_mail(email))