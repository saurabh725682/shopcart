from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

# Custom User Manager
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
             email = self.normalize_email(email),
             username = username,
             first_name = first_name,
             last_name = last_name,
        )        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    # Create a new superuser
    def create_superuser(self, first_name, last_name, email, username, password):
        # Create a new user instance
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            password = password,
        )
        # Set superuser permissions
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        # Save the superuser to the database
        user.save(using=self._db)
        return user


# Custom User Model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
    
    # Required fields
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    
    # Specify the username field for authentication
    USERNAME_FIELD = 'email'
    # Specify the required fields for user creation
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    # Use the custom user manager
    objects = MyAccountManager()
    
    def __str__(self):
        return self.email
    
    # Check if the user has a specific permission
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    # Check if the user has module permissions
    def has_module_perms(self, add_label):
        return True


# User Profile Model
class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=100, blank=True)
    address_line_2 = models.CharField(max_length=100, blank=True)
    profile_picture = models.ImageField(upload_to='userprofile', blank=True)
    city = models.CharField(max_length=20, blank=True)
    state = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=20, blank=True)
    
    # Return a string representation of the user profile
    def __str__(self):
        return self.user.first_name
    
    # Return the full address
    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}'
