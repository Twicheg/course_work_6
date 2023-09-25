from django.contrib.auth.models import Permission

from users.models import User


def get_permissions(request):
    if request.user.is_staff:
        permissions = [
            ('view', 'newsletter', 'MessageSettings'),
            ('view', 'users', 'user'),
            ('change', 'users', 'user'),
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
                if not request.user.is_staff:
                    perm = Permission.objects.get(content_type__app_label=f'{j[1]}', content_type__model=f'{j[2].lower()}',
                                                  codename=f'{j[0]}_{j[2].lower()}')
                    i.user_permissions.add(perm)


    else:
        permissions = [
            ('view', 'newsletter', 'MessageSettings'),
            ('change', 'newsletter', 'MessageSettings'),
            ('add', 'newsletter', 'MessageSettings'),
            ('delete', 'newsletter', 'MessageSettings'),

            ('view', 'newsletter', 'Message'),
            ('change', 'newsletter', 'Message'),
            ('add', 'newsletter', 'Message'),
            ('delete', 'newsletter', 'Message'),

            ('view', 'clients', 'clients'),
            ('change', 'clients', 'clients'),
            ('add', 'clients', 'clients'),
            ('delete', 'clients', 'clients'),

            ('view', 'logs', 'logs'),

        ]
        for i in User.objects.all():
            for j in permissions:
                if not request.user.is_staff:
                    perm = Permission.objects.get(content_type__app_label=f'{j[1]}', content_type__model=f'{j[2].lower()}',
                                                  codename=f'{j[0]}_{j[2].lower()}')
                    i.user_permissions.add(perm)
                    print(i.email, i.has_perm(f'{j[1]}.{j[0]}_{j[2].lower()}'))

