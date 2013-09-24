#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "Coin-%s" % get.srcVERSION()

def setup():
    autotools.configure("--prefix=/usr \
                         --mandir=/usr/share/man \
                         --enable-optimization \
                         --enable-3ds-import \
                         --enable-javascript-api \
                         --enable-threadsafe \
                         --enable-exceptions \
                         --enable-man \
                         --with-mesa \
                         --disable-debug \
                         --enable-shared \
                         --disable-maintainer-mode \
                         --disable-dependency-tracking \
                         --enable-system-expat")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "NEWS", "README*", "RELNOTES", "THANKS")

    # remove conflict man file with openssl
    pisitools.remove("/usr/share/man/man3/threads.3")
    # remove conflict man file with libftdi-devel
    pisitools.remove("/usr/share/man/man3/deprecated.3")