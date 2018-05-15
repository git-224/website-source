
import os
import sys
sys.path.append('..')

import human2website as h2w
import human2website.toolkits.bootstrap4dualmenu as toolkit

import xmenus


ht=h2w.HumanTree(toolkit,'webpages/')

ht.setting('menu.top', toolkit.MenuDump( xmenus.menutop ).converthtml() )
ht.setting('menu.bottom', toolkit.MenuDump( xmenus.menubottom ).converthtml() )


ht.saveto('../2-24-battalion-org-au.github.io')



