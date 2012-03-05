# clarox -nographics -nojournal -noecho -batch journalfilename.py
# from cubit cmd script editor
#   f = file("file.py"); cmdtext = f.read() ; exec(cmdtext)
cubit.cmd('set developer on')
cubit.cmd('   reset')

cubit.cmd('create brick width 12.5 height .2 ')
coilList = [(0,0),(3,0),(-3,0),(0,3),(0,-3),(4,4),(4,-4),(-4,4),(-4,-4)]
major = 1.5
minor = 1.0
for xloc,yloc in coilList:
  cyl = cubit.cylinder(10,minor ,major,minor/major)
  cubit.cmd('move volume %d x %f y %f z 0 ' % (cyl.id() , xloc,yloc )  )
  cubit.cmd('subtract volume %d from volume 1 ' % cyl.id() )
pi = 3.14
cubit.cmd('tweak volume 1 bend root 0 0 0 axis 1 0 0 direction 0 0 -1 radius 2 angle %f Center_bend' % (2*pi) )
