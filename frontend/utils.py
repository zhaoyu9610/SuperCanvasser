from backend import models


def getRoles(uid):
        user = models.User.objects.filter(id=uid)
        return [user.admin, user.manager, user.canvasser]


def generate_error_data(request, msg):
    return {}
