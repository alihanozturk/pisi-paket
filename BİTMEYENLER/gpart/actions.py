#!/usr/bin/python
# -*- coding: utf-8 -*-

# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.rawConfigure("prefix=/usr/local --bindir=$(prefix)/bin --libdir=$(prefix)/lib --mandir=$(prefix)/man --sharedir=$(prefix)/share")

def build():
    autotools.make()

def install():
    autotools.install()