from mysite.models import Post


def is_url_occupied(url: str) -> bool:
    """Проверка на занятость url адреса"""
    return bool(Post.objects.filter(url=url))
