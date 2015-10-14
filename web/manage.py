#!/usr/bin/env python
import os
import sys
from devhunt import settings
from os.path import join

if __name__ == "__main__":
    sys.path.insert(0, join(settings.PROJECT_ROOT))
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "devhunt.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
