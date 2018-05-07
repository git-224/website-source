

CARDS=[
    ['images/new_patch.jpg','1111111111111','iowedjiowedjiowej diojwe diojw diojwioedjw idjwiode jiowjd iowjd iowjdi wejdiowejd iojwd iojwe idw',None ],
    [None,'title2 of the card here','iowedjiowedjiowej diojwe diojw diojwioedjw idjwiode jiowjd iowjd iowjdi wejdiowejd iojwd iojwe idw',None ],
    [None,'title3 of the card here','iowedjiowedjiowej diojwe diojw diojwioedjw idjwiode jiowjd iowjd iowjdi wejdiowejd iojwd iojwe idw',None ],
    [None,'title4 of the card here','iowedjiowedjiowej diojwe diojw diojwioedjw idjwiode jiowjd iowjd iowjdi wejdiowejd iojwd iojwe idw',None ],

  ]



class   Card:
  def   __init__(self,im,title,txt,links):
    self.im=im
    self.title=title
    self.txt=txt
    self.links=links
  def   dumphtml(self,off=''):
    rv=[]
    rv.append(off+'<div class="card shadow col-sm-6 col-md-4 col-lg-3 p-3 mb-5 bg-white rounded">')
    if self.im:
      rv.append(off+'  <img class="card-img-top" src="%s" alt="Card image cap">'%(self.im))
    rv.append(off+'  <div class="card-body">')
    rv.append(off+'    <h5 class="card-title">%s</h5>'%(self.title))
    rv.append(off+'''  <p class="card-text">%s</p>'''%(self.txt))
    rv.append(off+'    <a href="#" class="btn btn-primary">Go somewhere</a>')
    rv.append(off+'  </div>')
    rv.append(off+'</div>')
    return rv


rv=[]
rv.append('<div class="container card-group container-fluid">')
rv.append('  <div class="row" style=".row { display: flex; flex-wrap: wrap; };">')
n=0
for c in CARDS+CARDS+CARDS:
#  if n%3==0:
#    if n!=0:
#      rv.append('  </div>') # end row
#    rv.append(  '  <div class="row">')
  cd=Card(*c)
#  rv.append('    <div class="col-sm">')
  rv+=cd.dumphtml('      ')
#  rv.append('    </div>') # end col-sm
  n+=1

#rv.append('  </div>') # end row
rv.append('  </div>')
rv.append('</div>')

for l in rv:
  print l


