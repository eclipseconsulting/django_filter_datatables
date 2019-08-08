import logging

from django.contrib.auth.models import Group, Permission
from django.core.exceptions import MultipleObjectsReturned

logger = logging.getLogger('account_helper')


def setup_group_permissions(group_name, codenames):
    group, created = Group.objects.get_or_create(name=group_name)
    if created:
        logger.info('created {0} group'.format(group_name))

    permissions = []
    for codename in codenames:
        try:
            # permission = Permission.objects.get(codename=codename)
            permission = Permission.objects.get(
                codename=codename[0],
                content_type__app_label=codename[1],
                content_type__model=codename[2],
            )

            permissions.append(permission)
        except Permission.DoesNotExist:
            logger.error('permission: ' + codename + ' not found')
        except MultipleObjectsReturned:
            logger.error('Multiple records exist for permission {0}'.format(codename))

    for p in permissions:
        group.permissions.add(p)
