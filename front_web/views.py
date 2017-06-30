import sys

from django.conf import settings
from django.http import HttpResponse
from django.views import View

from base.utils.utility import get_base_email_context, email_send


class FrontHome(View):
    def get(self, request):
        # <view logic>
        try:
            subject = "{app_name} - Test Mail".format(app_name=settings.APP_NAME)
            to = ["rudra12shailesh@gmail.com"]
            context = get_base_email_context(request)
            context.update({
            })

            # email_message = get_template('email_templates/test.html').render(Context(context))
            email_send(subject, "Test Mail", to)
        except:
            if settings.DEBUG:
                print("Email: ", sys.exc_info())
        return HttpResponse('Home GET')

    def post(self, request):
        return HttpResponse('result POST')
