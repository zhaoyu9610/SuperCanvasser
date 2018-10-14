from SuperCanvasser import utils, models
import json


class ManagerHandler:
    def availabilities(self, request):
        if 'cookie' in request.COOKIES:
            uid = request.COOKIES['cookie']
            if utils.check_canvasser(uid) or utils.check_admin(uid):
                result = []
                for user in models.User.objects.filter(canvasser=True).all():
                    dates = []
                    for campaign_date in models.Availability.objects.filter(canvasser=user).all():
                        dates.append(campaign_date.date)
                    result.append({'user': user.email, 'availability': dates})
                utils.generate_response(request, {'availabilities': result})
            else:
                return utils.generate_error(request, 'Not canvasser')
        else:
            return utils.generate_error(request, 'Not logged in')
