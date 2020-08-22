#!/usr/bin/env python
"""
Print info on datasets in hdf5 (big) file.
"""
from __future__ import print_function
import sys
import numpy as np
import imp
import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

msg = imp.load_source('msg', './hdf5_manipulator_all/hdf5_manipulator_mod/msg.py')

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("usage: ./print file")
        sys.exit(1)

    f = h5py.File(sys.argv[1], 'r')

    k=f['img_data/hitimes-x']
    u=f['img_data/hitimes-u']
    v=f['img_data/hitimes-v']

    w=f['gen_data/W']

    #if w > 5000.0:
    print(k);
    msg.print_sample(f, 'gen_data', 'W',1, 15)
    msg.print_sample(f, 'vtx_data', 'planecodes',1, 15)
    msg.print_sample(f, 'gen_data', 'int_type',1, 15)
    msg.print_sample(f, 'event_data', 'eventids',99190, 99205)
#    xd=f['img_dataDScal/hitimes-x']
#    ud=f['img_dataDScal/hitimes-u']
#    vd=f['img_dataDScal/hitimes-v']

#    pd=f['vtx_data/planecodesDScal'][:]
   #p=f['vtx_data/planecodes'][:]
          #e=d['planecodesEcal'][:]
#    mapd=pd.max()
#    mipd=pd.min()
   # map=p.max()  #Commmented for datafiles
   # mip=p.min()

   # values = np.array(p)
   # index_min = np.argmax(values)
   # print(index_min)


   #max1 = np.max(p)
   # print('value max: {}'.format(max1))
   # maxi = np.where(p == max1)
   # print('value: {}'.format(maxi))
    #print(p[194])

   #print("Planecodes max: {} min: {}".format(p.max(),p.min()))
    #print("PlanecodesDS max: {} min: {}".format(pd.max(),pd.min()))

   #ids = f['event_data/eventids']
   #idsa=f['event_data/eventids_a']
   #idsb=f['event_data/eventids_b']

    print("\nThe following datasets were found in {}:\n" .format(sys.argv[1]))
    msg.list_dataset(f)

    print("Planecodes: ")
   #msg.print_sample(f, 'vtx_data', 'planecodes',180, 195)
   #msg.print_sample(f, 'event_data', 'eventids',180, 195)
    #print("PlanecodesDScal: ")
    #msg.print_sample(f, 'vtx_data', 'planecodesDScal',0, 20)
    #print("PlanecodesDScal1: ")
    #msg.print_sample(f, 'vtx_data', 'planecodesDScal1',0, 20)
    #msg.print_sample(f,'img_data','hitimes-x',0,1)

    print("img_data/hitimes-x value [0][0][0]: ")
    print(k[0][0][0])
#    print("img_dataDScal/hitimes-x value [0][0][0]: ")
#    print(vd[0][0][0])

   # print("the ids value for k[0][0] is: {}, idsa= {} and idsb= {}".format(ids[0][0],idsa[0][0],idsb[0][0]))

    # To show histogram
    #num_bins = mapd - mipd
    #n, bins, patches = plt.hist(pd, num_bins, facecolor='blue', alpha=0.5)
    #plt.show()

    #For x view 99190,99205
    for x in range(10):
        for y in range(2):
            fig = plt.gcf()
            plt.imshow(k[x][y],cmap='Reds',origin='lower',norm=LogNorm())
            plt.colorbar()
            #plt.show()
            plt.draw()
            fig.savefig('{}-{}-x.png'.format(x,y))
            plt.clf()


    #For v view
    for x in range(10):
        for y in range(2):
            #plt.clf()
            fig = plt.gcf()
            plt.imshow(v[x][y],cmap='Reds',origin='lower',norm=LogNorm())
            plt.colorbar()
            #plt.show()
            plt.draw()
            fig.savefig('{}-{}-v.png'.format(x,y))
            plt.clf()


    #For u view
    for x in range(10):
        for y in range(2):
            #plt.clf()
            fig = plt.gcf()
            plt.imshow(u[x][y],cmap='Reds',origin='lower',norm=LogNorm())
            plt.colorbar()
            #plt.show()
            plt.draw()
            fig.savefig('{}-{}-u.png'.format(x,y))
            plt.clf()

    #plt.imsave('11-0-u.png',u[11][0],cmap='Reds',origin='lower')
    #plt.imsave('11-0-v.png',v[11][0],cmap='Reds',origin='lower')
    #plt.imsave('11-0.png',k[11][0],cmap='Reds',origin='lower')


    #print("The max number is: {} and the min is: {}".format(g,h))
    f.close()
