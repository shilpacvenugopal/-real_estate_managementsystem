# #!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # Add the path to your project directory
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/realestate_management')

    from django.core.management import execute_from_command_line

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realestate_management.settings")

    execute_from_command_line(sys.argv)
