#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

#WorkDir = ""

from pisi.actionsapi import get
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def setup():
    autotools.configure()

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    
    pisitools.dodoc("COPYING", "LICENSE", "RELEASE.NOTES", "doc/snort_manual.pdf")

    # Copy all config dir except MakeFiles
    pisitools.insinto("/etc/snort", "etc/*")
    pisitools.remove("/etc/snort/Makefile*")

    # Create logdir or snort will not start
    pisitools.dodir("/var/log/snort")