#!/usr/bin/env pythontry:
try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:
    pass 
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "HomebrewSite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
