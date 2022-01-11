#!/usr/bin/env python

import os
import glob
import sys
import fsspec
import boto3

year = 2009

bucket = 'ws-out'
input_prefix='WOTJE/Run08_13_2021/wotje_imerg_081321_o/'

out_bucket = 'ws-enduser'
output_prefix='tarzip-WOTJE/'


fs = fsspec.filesystem('s3', anon=False, requester_pays=True)

my_file_dir = f's3://{bucket}/{input_prefix}/'

my_file_list = fs.ls(my_file_dir)


def tar_compress_me(tarball_name, file_wildcard):
    cmd = f'tar cvfz {tarball_name} {file_wildcard}'
    os.system(cmd)
    return(True)


def get_files_to_local_disk(my_file_list):
    cnt=0
    for file in my_file_list:
        lfile = os.path.basename(file)
        fs.get(file,f'./tif/{lfile}')
        cnt=cnt+1
        print('.',cnt)
    


def rm(wildcard):
    # Get a list of all the file paths that ends with .txt from in specified directory
    fileList = glob.glob(wildcard)
    # Iterate over the list of filepaths & remove each file.
    for filePath in fileList:
        try:
            os.remove(filePath)
        except:
            print("Error while deleting file : ", filePath)


def s3_push_delete_local(local_file, bucket, bucket_filepath):
        out_bucket = bucket
        print('PUSH', out_bucket, bucket_filepath)
        s3 = boto3.client('s3')
        with open(local_file, "rb") as f:
            s3.upload_fileobj(f, out_bucket, bucket_filepath)
        os.remove(local_file)


def tarzip_one_year(year):
    print(year)
    my_file_dir = f's3://{bucket}/{input_prefix}{str(year)}'
    my_file_list = fs.ls(my_file_dir)
    print(my_file_list[0])
    get_files_to_local_disk(my_file_list)
    tarball_name = f'{str(year)}.tgz'
    file_wildcard = './tif/*.tif'
    tar_compress_me(tarball_name, file_wildcard)
    local_file=tarball_name
    bucket_filepath = f'{output_prefix}{local_file}'
    s3_push_delete_local(local_file, out_bucket, bucket_filepath)
    rm(file_wildcard)
    
    
# MAIN

tarzip_one_year(year)
