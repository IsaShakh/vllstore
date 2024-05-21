import rules
from users.models import User
from tools.rules.rules_utils import object_level_predicate

@object_level_predicate
def is_myself(user, obj):
    return obj.id == user.id
# USERS
rules.add_perm(User.get_perm('add'), rules.is_superuser)
rules.add_perm(User.get_perm('change'), rules.is_superuser)
rules.add_perm(User.get_perm('delete'), rules.is_superuser)
rules.add_perm(User.get_perm('view'), rules.is_authenticated & (rules.is_superuser | is_myself))

