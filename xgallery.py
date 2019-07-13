
import os


root="/nas/8t-single/syncthing/share_2-24-battalion/photos/"
root="/nas/8t-single/syncthing/share_2-24-battalion/photos/2019/Wang-HS"

dst='../2-24.battalion.org.au/www/gallery'


class Album:
  def __init__(self,srcpath):
    self.images={}
    self.subalbums={}


a=Album()
for d,sd,sf in os.walk(root):
  if '.DS_Store' in sf: sf.remove('.DS_Store')
  d=d[len(root)-1:]
  print(d,sd,sf)


if not os.path.exists(dst):
  os.mkdir(dst)

a.write(dst)





