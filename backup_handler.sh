#!/bin/bash

# get path
path_with_files_to_backup=$1

# move to it
cd $path_with_files_to_backup

# set up backup dir naming
backup_date=$(date +"%m-%d-%Y")

backup_dir=${backup_date}"-backups"

# make a directory
mkdir $backup_dir


# loop through items in pwd and find lbl and sf4 files
for item in $( ls ); do 
    if [[ $item == *log* ]] 
     then
       cp $item $backup_dir
       rm $item
    elif [[ $item == *map* ]]
     then
       cp $item $backup_dir
       rm $item
    fi
done

#tar the package
tar -czvf $backup_dir.tar.gz $backup_dir

# remove the container which stores backups
rm -r $backup_dir
