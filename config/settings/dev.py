from .base import *  # noqa

STAGE="production"
DEBUG = True
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": (BASE_DIR / "db.sqlite3"),
    }
}
###################################################################
# Django security
###################################################################

"""
IF YOU WANT SET CSRF_TRUSTED_ORIGINS = ["*"] THEN YOU SHOULD SET:
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
"""
USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
CSRF_TRUSTED_ORIGINS = ["https://khodjiyev2o.jprq.live", "https://bek.kjssst.uz/"]
CSRF_COOKIE_SECURE = True

CORS_ALLOWED_ORIGINS = [
    'http://127.0.0.1:5581',
    'https://khodjiyev2o.jprq.live',
    "https://bek.kjssst.uz/",
]

###################################################################
# CORS
###################################################################
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ["*"]
