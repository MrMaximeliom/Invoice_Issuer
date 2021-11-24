from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from Util.utils import rand_slug
# this class is responsible of User account management
class UserAccountManager(BaseUserManager):
    def create_user(self, full_name, phone_number,email, password=None, **extra_fields):
        # check if user entered his/her full_name and raise exception if not
        if not full_name:
            raise ValueError(_('Users must provide their full name'))
        # check if user entered his/her phone_number and raise exception if not
        if not phone_number:
            raise ValueError(_('Users must provide their phone number'))
        # check if user entered his/her email and raise exception if not
        if not email:
            raise ValueError(_('Users must provide their email'))
        user = self.model(
            full_name=full_name,
            phone_number=phone_number,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    # function that creates a super user
    def create_superuser(self, full_name, phone_number,email,
                         password):
        user = self.create_user(
            full_name=full_name,
            phone_number=phone_number,
            email=self.normalize_email(email),
            password=password
        )
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user

# the base User class which describes user attributes and functions
# it will represent the "User Model"
class User(AbstractBaseUser):
    # full name field
    full_name = models.CharField(
        verbose_name=_('Full Name'),
        max_length=350,
        blank=False,
        null=False
    )
    # phone number field
    phone_number = models.CharField(
        verbose_name=_('Phone Number'),
        blank=False,
        null=False,
        max_length=100,
        unique=True
    )
    # email field
    email = models.EmailField(
        verbose_name=_('Email Address'),
        max_length=255,
        unique=True,
        blank=False,
        null=False
    )
    # is customer field , default is "yes" meaning any new user will be a customer
    is_customer = models.BooleanField(
        verbose_name=_("Is Customer"),
        blank=False,
        null=False,
        default=True
    )
    # user street address
    street_address = models.CharField(
        max_length=550,
        verbose_name=_("Street Address"),
        blank=True
    )
    # user city
    city = models.ForeignKey(
        "address.City",
        null=True,
        on_delete=models.SET_NULL,
        verbose_name=_("City")
    )

    # is user active? field , default yes
    is_active = models.BooleanField(default=True)
    # is user staff? field , default no
    staff = models.BooleanField(default=False)
    # is user admin? field , default no
    admin = models.BooleanField(default=False)
    # last login date field , it will be created by default
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    # user slug field , will be created by default
    slug = models.SlugField(
        default=slugify(rand_slug()),
        verbose_name=_('User Slug')
    )
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + str(self.full_name))
        return super().save(*args, **kwargs)
    # "email field" is the field that will be used in the login process with the password field
    USERNAME_FIELD = 'email'
    # listing required fields
    REQUIRED_FIELDS = ['password', 'full_name','phone_number'
                       'username','is_customer']
    objects = UserAccountManager()
    def get_full_name(self):
        # The user is identified by their full name
        return self.full_name

    def get_user_name(self):
        return self.username

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # return self.user_role == 3
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        # return self.user_role == 1
        return self.admin
