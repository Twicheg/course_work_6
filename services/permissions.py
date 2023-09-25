from django.contrib.auth.models import Permission

from users.models import User


def get_permissions(request):
    if request.user.is_staff:
        permissions = [
            ('view', 'newsletter', 'MessageSettings'),
            ('view', 'users', 'user'),
            ('change', 'users', 'user'),
            ('change', 'newsletter', 'MessageSettings'),
        ]
    # if request.user.is_active:
    #     permissions = [
    #         ('view', 'newsletter', 'MessageSettings'),
    #         ('view', 'users', 'user'),
    #         ('change', 'users', 'user'),
    #         ('change', 'newsletter', 'MessageSettings'),
    #     ]

        for i in User.objects.all():
            for j in permissions:
                perm = Permission.objects.get(content_type__app_label=f'{j[1]}', content_type__model=f'{j[2].lower()}',
                                              codename=f'{j[0]}_{j[2].lower()}')
                i.user_permissions.add(perm)
                print(i.email ,i.has_perm(f'{j[1]}.{j[0]}_{j[2].lower()}'))
