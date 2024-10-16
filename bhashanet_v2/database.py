
# Added By Sanjayb
import environ

# Initialize environment variables
env = environ.Env()

# Reading .env file
environ.Env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DEFAULT_DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
            'charset': 'utf8mb4'
        }
    },
    'osticket': { 
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('OSTICKET_DATABASE_NAME'),
        'USER': env('OSTICKET_DATABASE_USER'),
        'PASSWORD': env('OSTICKET_DATABASE_PASSWORD'),
        'HOST': env('OSTICKET_DATABASE_HOST'),
        'PORT': '3306',
    },
}

DATABASE_ROUTERS = ['core_app.db_routers.MyAppRouter']