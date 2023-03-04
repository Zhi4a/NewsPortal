from celery import shared_task
import time


@shared_task
def inform_for_new_posts():
    print('Дайджест начал работу')
    date_from = date.today()-timedelta(days=8)
    date_to = date.today()-timedelta(days=1)
    post_source = Post.objects.filter(Q(creation__gte=date_from) & Q(creation__lt=date_to))
    users = SubscribersCategory.objects.all().values('user_id').distinct()
    title = f'Дайджест новых постов'

    for i in range(users.count()):
        categories = CategoryUser.objects.filter(user_id=users[i]['user_id']).values('category_id', 'category_id__name')
        user = User.objects.filter(id=users[i]['user_id']).values('username', 'email')
        user_name = f"{user[0]['username']}"
        for c in range(categories.count()):
            category_name = categories[c]['category_id__name']
            posts = post_source.filter(category__id=categories[c]['category_id'])
            if posts.count() == 0:
                continue
            html_content = render_to_string(
                        'post_digest.html',
                        {
                            'date_from': date_from,
                            'date_to': date_to,
                            'title': title,
                            'user': user_name,
                            'category': category_name,
                            'posts': posts,
                            'url_start': 'http://127.0.0.1:8000/',
                        }
                    )
            msg = EmailMultiAlternatives(
                subject=title,
                body=f'Дайджест новых постов с {date_from} по {date_to}.',
                from_email='sohuga55@yandex.ru',
                to=[user[0]['email']],
            )

            msg.attach_alternative(html_content, "text/html")
            msg.send()

    print('Рассылка дайджеста завершена')
