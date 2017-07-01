from django.conf import settings
from django.http import HttpResponse
from django.views import View

from base.utils.utility import get_base_email_context, email_send, mass_email_send


class FrontHome(View):
    def get(self, request):
        return HttpResponse('Home Page GET')

    def post(self, request):
        return HttpResponse('result POST')


class CeleryMail(View):
    def get(self, request):
        subject = "{app_name} - Test Mail".format(app_name=settings.APP_NAME)
        to = ["rudra12shailesh@gmail.com"]
        context = get_base_email_context(request)
        context.update({
        })

        # email_message = get_template('email_templates/test.html').render(Context(context))
        email_send(subject, "Test Mail", to)
        return HttpResponse('Email sent to multiple users with same subject and email details')

    def post(self, request):
        return HttpResponse('result POST')


class CeleryMassMail(View):
    def get(self, request):
        emails = (
            (
                'Hey Man',
                "I'm The Dude! So that's what you call me.",
                'rudra12shailesh@gmail.com',
                ['rudra12shailesh@gmail.com']
            ),
            (
                'Hey Man2',
                "I'm The Dude! So that's what you call me.2",
                'rudra12shailesh@gmail.com',
                ['rudra12shailesh@gmail.com']
            ),
        )

        mass_email_send(emails)
        return HttpResponse('Home GET')

    def post(self, request):
        return HttpResponse('result POST')
