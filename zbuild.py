
import os
import sys
sys.path.append('..')

import human2website.builder as builder
import human2website.toolkits.bootstrap4

import xmenus


toolkit=human2website.toolkits.bootstrap4.DualMenu()



toolkit.setting('menutop', toolkit.menu2html( xmenus.menutop ) )
toolkit.setting('menubottom', toolkit.menu2html( xmenus.menubottom ) )
toolkit.setting('title','2-24th Battalion Association')
toolkit.setting('keywords',"Tobruk, 2nd AIF, Tel El Eisa, El Alamein, Rats of Tobruk, World War 2, ANZAC, Australian Army, 9th Division, Salient, Halfaya Pass, Tarakan, New Guinea, Finschhafen, Lae, Wangaratta's Own")

ht=builder.HumanTree(toolkit,'webpages/','../2-24-battalion-org-au.github.io')

ht.precopy('/CNAME')
ht.build_final()



