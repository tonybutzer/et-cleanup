import fsspec
fs = fsspec.filesystem('s3', anon=False, requester_pays=True)


def get_files_wzell(path):
    files = fs.ls(f'{path}')
    return [f for f in files if 'dd_' in f]


path = 'ws-enduser/wzell/'

my_files = get_files_wzell(path)

print(len(my_files))

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


for file in my_files:
    copy_scp_delete(file)



