from sys_path_hacks.warn import warn_deprecated_import

warn_deprecated_import('lms.djangoapps', 'commerce.api.v1.serializers')

from lms.djangoapps.commerce.api.v1.serializers import *
