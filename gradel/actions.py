#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

WorkDir="gradel-0.12.1"

def install():
    shelltools.system("./compile.sh")
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())
    shelltools.system("./install.sh")