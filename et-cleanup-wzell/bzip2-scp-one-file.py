import sys
import fsspec


fs = fsspec.filesystem('s3', anon=False, requester_pays=True)

one_file = 'dummy'

if sys.argv[1]:
    one_file = sys.argv[1]

print('Processing: ', one_file)


import os

def scp_me(zfile):
    caldera = '/caldera/projects/usgs/water/impd/butzer/wzell'
    os.system(f'scp {zfile} butzer@tallgrass.cr.usgs.gov:{caldera}')


def bzip2_me(file):
    print('bzip2 this file:', file)
    os.system(f'bzip2 -z {file}')
    return(f'{file}.bz2')


def copy_scp_delete(file):
    fs = fsspec.filesystem('s3', anon=False, requester_pays=True)
    print(file)
    fs.get(file,'./')
    lfile = os.path.basename(file)
    zfile = bzip2_me(lfile)
    scp_me(zfile)
    print(zfile)
    os.unlink(zfile)


copy_scp_delete(one_file)



