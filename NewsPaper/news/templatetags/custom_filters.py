from django import template

register = template.Library()

ban_words = ['редиска', 'Редиска']


@register.filter()
def currency(value):
    a = value.split(' ')
    value = []
    for i in a:
        if i in ban_words:
            i = i[0] + '*'*(len(i)-1)
        value.append(i)
    a = ' '.join(value)
    return f'{a}'
