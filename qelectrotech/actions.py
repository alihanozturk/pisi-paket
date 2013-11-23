#!/usr/bin/python
# -*- coding: utf-8 -*-
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/copyleft/gpl.txt

from pisi.actionsapi import qt4
#from pisi.actionsapi import pisitools

# if pisi can't find source directory, see /var/pisi/qelectrotech/work/ and:
# WorkDir="qelectrotech-"+ get.srcVERSION() +"/sub_project_dir/"

def setup():
    qt4.configure()

def build():
    qt4.make()

def install():
    qt4.install()

# Take a look at the source folder for these file as documentation.
#    pisitools.dodoc("AUTHORS", "BUGS", "ChangeLog", "COPYING", "README")

# If there is no install rule for a runnable binary, you can 
# install it to binary directory.
#    pisitools.dobin("qelectrotech")

# You can use these as variables, they will replace GUI values before build.
# Package Name : qelectrotech
# Version : 0.3
# Summary : QElectroTech kendi elektrik şemalarına oluşturmanıza yardımcı olmak için tasarlanmış bir uygulamadır.

# For more information, you can look at the Actions API
# from the Help menu and toolbar.

# By PiSiDo 2.0.0
