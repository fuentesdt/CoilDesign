# clarox -nographics -nojournal -noecho -batch journalfilename.py
# from cubit cmd script editor
#   f = file("file.py"); cmdtext = f.read() ; exec(cmdtext)
cubit.cmd('set developer on')
cubit.cmd('   reset')

cubit.cmd('create brick width 12.5 height .1 ')
coilList = [(0,0),(3,0),(-3,0),(0,3),(0,-3),(4,4),(4,-4),(-4,4),(-4,-4)]
height= 0.2
major = 1.2
minor = 0.8
radialThickness = .2
for xloc,yloc in coilList:
  cylIn = cubit.cylinder(height,minor ,major,minor)
  cubit.cmd('move volume %d x %f y %f z 0 ' % (cylIn.id() , xloc,yloc )  )
  cylOut = cubit.cylinder(height,minor+ radialThickness ,major +radialThickness ,(minor + radialThickness))
  cubit.cmd('move volume %d x %f y %f z 0 ' % (cylOut.id() , xloc,yloc )  )
  cubit.cmd('subtract volume %d from volume %d ' % ( cylIn.id(),cylOut.id() ) )
  cubit.cmd('tweak volume %d bend root 0 0 0 axis 1 0 0 direction 0 0 -1 radius 2 angle %f Center_bend' % (cylOut.id(),2*pi) )
#  cubit.cmd('subtract volume %d from volume %d ' % ( cylOut.id(), 1 ) )
#cubit.cmd('volume all merge' )
#cubit.cmd('unite volume 3 5 7 9 11 13 15 17 19' )
#cubit.cmd('intersect volume 1 with  volume 3 5 7 9 11 13 15 17 19' )
pi = 3.14
cubit.cmd('tweak volume 1 bend root 0 0 0 axis 1 0 0 direction 0 0 -1 radius 2 angle %f Center_bend' % (2*pi) )
