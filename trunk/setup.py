# coding: iso-8859-1
from distutils.core import setup
import py2exe
import sys

# If run without args, build executables, in quiet mode.
if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

cronService = dict(
    modules = ["pycron"],
    icon_resources = [(0, "pycron.ico"),]
    )

includes = ["encodings.*",
           ]

excludes = ["pywin", "pywin.debugger", "pywin.debugger.dbgcon",
            "pywin.dialogs", "pywin.dialogs.list", "perfmon", "ctypes",
            "email", "EasyDialogs", ]

setup(
    options = {"py2exe": {#"compressed": 1, --> setup is smaller if files are not compressed!
                          "optimize": 2
                          ,"includes": includes
                          ,"excludes": excludes
                         }},
    zipfile = "shared.zip",
    service = [cronService],
    version='0.5.9.1',
    description="A cron service written in Python",
    windows = [{"script": "pyCronEditor.py",
                "icon_resources": [(1, "pycron.ico")]
               }],
    console = [{"script": "pycron.py",
                "icon_resources": [(1, "pycron.ico")],
                "dest_base": "pycron_console"
               }],
    )
