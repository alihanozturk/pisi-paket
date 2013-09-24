#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

WorkDir = "apache-maven-%s" % get.srcVERSION()

def install():
    pisitools.dodir("/opt/maven")
    shelltools.copy("./*", "%s/opt/maven/" % get.installDIR())

    pisitools.dosym("/opt/maven/bin/mvn","/usr/bin/mvn")

    pisitools.remove("/opt/maven/bin/*.bat")

    pisitools.dodoc("README.txt", "NOTICE.txt", "LICENSE.txt")
    pisitools.remove("/opt/maven/*.txt")
