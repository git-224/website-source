import yaml
import pprint


class   MenuItem_Meta(object):
  def __init__(self,parent):
    self.parent=parent
  def   is_submenu(self): return False
  def   html_name_me(self):
    return self.name
  def   html_name(self):
    return self.parent.html_name()+'_'+self.html_name_me()


class MenuItem_Html(MenuItem_Meta):
  def __init__(self,parent,line):
    MenuItem_Meta.__init__(self,parent)
    #print 'HMTL,line is',[line]
    self.line=line
  def   dumphuman(self,off=''):
    print off+'[html[%s]]'%(self.line)
  def   dumphtml(self,off=''):
    return [ off+self.line ]

class MenuItem_Link(MenuItem_Meta):
  def __init__(self,parent,line):
    MenuItem_Meta.__init__(self,parent)
    #print 'LINK,line is',[line]
    url,text=popword(line)
    self.url=url
    self.text=text
  def   dumphuman(self,off=''):
    print off+'[link[%s -> %s]]'%(self.url,self.text)
  def   dumphtml(self,off=''):
    if self.parent.is_submenu():
      return [ off+'<a class="dropdown-item" href="%s">%s</a>'%(self.url,self.text) ]

    return [ off+'<li class="nav-item active">',
             off+'  <a class="nav-link" href="%s">%s</a>'%(self.url,self.text),
             off+'</li>' ]


class MenuItem_Img(MenuItem_Meta):
  def __init__(self,parent,line):
    MenuItem_Meta.__init__(self,parent)
    #print 'IMG,line is',[line]
    self.src=line
  def   dumphuman(self,off=''):
    print off+'[img[%s]]'%(self.src)
  def   dumphtml(self,off=''):
    return [ off+'<img src="%s" class="d-inline-block align-top" alt="">'%(self.src) ]

class MenuItem_Rule(MenuItem_Meta):
  def __init__(self,parent,line):
    MenuItem_Meta.__init__(self,parent)
  def   dumphuman(self,off=''):
    print off+'[rule]'
  def   dumphtml(self,off=''):
    return [ off+'<div class="dropdown-divider"></div>' ]




class MenuItem_Submenu(MenuItem_Meta):
  def __init__(self,parent,name,itemlist):
    MenuItem_Meta.__init__(self,parent)
    self.name=name
    self.contents=contents_load( self,itemlist )
  def   is_submenu(self): return True
  def   dumphuman(self,off=''):
    print off+'<sm>',self.name
    for c in self.contents:
      c.dumphuman(off+'..')
  def   dumphtml(self,off=''):
    rv=[]
    rv.append( off+'<li class="nav-item dropdown active">' )
    rv.append( off+'  <a class="nav-link dropdown-toggle" href="#" id="%s" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">'%(self.html_name()) )
    rv.append( off+'    '+self.name )
    rv.append( off+'  </a>')
    rv.append( off+'  <div class="dropdown-menu" aria-labelledby="%s">'%(self.html_name()) )
    for c in self.contents:
      rv+=c.dumphtml(off+'    ')
    rv.append( off+'  </div>')
    rv.append( off+'</li>')
    return rv

#####################################
ITEMS={ 'rule':MenuItem_Rule, 'image':MenuItem_Img, 'link':MenuItem_Link,
        'html':MenuItem_Html,
      }
def popword(st):
  return st.split(None,1)

def contents_load(self,itemlist):
  rv=[]
  for i in itemlist:
    if type(i)==type({}): 
      rv.append( MenuItem_Submenu(self,i['name'],i['contents'])  )
    else:
      rest=''
      k=i
      if k not in ITEMS: k,rest=popword(i)
      #print [k,rest]
      rv.append( ITEMS[ k ]( self,rest ) )
  return rv
#####################################


class Menu_Menu(MenuItem_Meta):
  def __init__(self,parent,contents=[]):
    MenuItem_Meta.__init__(self,parent)
    self.align='left'
    self.contents=contents_load( self,contents )
  def   html_name_me(self):
    return 'menu%s'%(self.align)
  def   dumphuman(self,off=''):
     for c in self.contents:
       c.dumphuman(off+'..')
  def   dumphtml(self,off=''):
     rv=[]
     for c in self.contents:
       rv+=c.dumphtml(off+'  ')
     return rv

class Menu_Home(MenuItem_Meta):
  def __init__(self,parent,url,content=[]):
    MenuItem_Meta.__init__(self,parent)
    self.url=url
    self.contents=contents_load(  self,content  )
  def   dumphuman(self,off=''):
    print off+'<home>.url',self.url
    for c in self.contents:
      c.dumphuman(off+'..')
  def   dumphtml(self,off=''):
    rv=[]
    rv.append( off+'<a class="navbar-brand" href="%s">'%(self.url))
    rv.append( off+'  <button type="button" class="btn btn-success navbar-btn">')
    for c in self.contents:
      rv+=c.dumphtml(off+'    ')
    rv.append( off+'  </button>')
    rv.append( off+'</a>')
    return rv




#

class Menu_NavBar(MenuItem_Meta):
  def __init__(self,config):
    MenuItem_Meta.__init__(self,None)
    self.location=config.get('location','top')
    self.sticky=config.get('sticky',False)
    self.home=Menu_Home( self,config['home']['url'], config['home']['contents'] )
    self.menu=Menu_Menu( self,config['menu'] )
    self.menuright=None
    if config.get('menuright'):
      self.menuright=Menu_Menu( config['menuright'] )
      self.menuright.align='right'
  def   html_name(self):
    return self.html_name_me()
  def   html_name_me(self):
    return 'navbar%s'%(self.location)

  def   dumphuman(self):
    print 'NAVBAR',self,self.location,self.sticky
    self.home.dumphuman('h.')
    self.menu.dumphuman('m.')
    if self.menuright: self.menuright.dumphtml('r.')
  def   dumphtml(self):
    rv=[]
    flags=''
    if self.sticky: flags='fixed-top'
    rv.append('')
    rv.append('<!-- begin menubar %s -->'%(self.location))
    rv.append('')
    rv.append('<nav class="navbar %s navbar-expand-lg navbar-dark bg-dark nav-pills">'%(flags))
    rv.append('')
    rv+=self.home.dumphtml('  ')
    rv.append('')
    rv.append('  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#%s" aria-controls="%s" aria-expanded="false" aria-label="Toggle navigation">'%(self.html_name(),self.html_name()) )
    rv.append('    <span class="navbar-toggler-icon"></span>')
    rv.append('  </button>')
    rv.append('')
    rv.append('  <div class="collapse navbar-collapse" id="%s">'%(self.html_name()) )
    rv.append('    <ul class="navbar-nav">')
    rv.append('')

    rv+=self.menu.dumphtml('    ')
    if self.menuright:
      rv.append('')
      rv+=self.menuright.dumphtml('    ')

    rv.append('')
    rv.append('    </ul>')
    rv.append('  </div>')
    rv.append('</nav>')
    rv.append('')
    rv.append('<!-- end menubar %s -->'%(self.location))
    rv.append('')

    return rv


t=yaml.load( open('top.yaml') )
nb=Menu_NavBar(t)
for l in nb.dumphtml():
  print l

t=yaml.load( open('bottom.yaml') )
nbb=Menu_NavBar(t)
for l in nbb.dumphtml():
  print l
