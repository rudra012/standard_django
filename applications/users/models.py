from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from base.model_choices import DEVICE_TYPE
from base.models import UUIDModel, BaseModel
from base.utils.utility import email_send


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        # if not username:
        #     raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        if extra_fields.get('is_active') is None:
            extra_fields['is_active'] = True
        user = self.model(email=email, is_staff=is_staff,
                          is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class User(AbstractBaseUser, UUIDModel, PermissionsMixin, BaseModel):
    first_name = models.CharField(_('First Name'), max_length=120, blank=True)
    last_name = models.CharField(_('Last Name'), max_length=120, blank=True)
    email = models.EmailField(_('email address'), unique=True, db_index=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text='Designates whether the user can log into this admin site.')

    # For notification on mobile phone
    device_type = models.CharField(max_length=1, choices=DEVICE_TYPE, null=True, blank=True)
    device_id = models.CharField(max_length=255, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name.strip()

        # def clean(self):
        #     self.username = self.username.lower()


@receiver(post_save, sender=User)
def create_user_signal(sender, instance, **kwargs):
    # print("post_save: sender, instance, created, **kwargs")
    # print(sender, instance, kwargs)
    if kwargs.get('created', False):
        # Send verification mail on user creation
        print("created")
        subject = "{app_name} - Account Verification Mail".format(app_name=settings.APP_NAME)
        to = [instance.email]
        # context = {
        # }
        # email_message = get_template('email_templates/test.html').render(Context(context))
        email_send(subject, "Account Verification Mail", to)
