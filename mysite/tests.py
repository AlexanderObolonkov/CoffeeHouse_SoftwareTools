from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug


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
