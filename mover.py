# RUNS ON BTVM sfc9mhtvp01

import shutil
import os
import datetime
import sys
import glob


class Mover:

    def move_file(self, src, dst, filename):
        try:
            shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
        except FileNotFoundError:
            print("File not found, exiting.")

    def backup_current_file(self, dst, bkup_path, filename):
        try:
            bkup_date = datetime.datetime.today().strftime('%Y-%m-%d-%s')
            shutil.move(os.path.join(dst, filename),
                        os.path.join(bkup_path, filename + "." + bkup_date))
        except FileNotFoundError:
            print(f"File not found in path \n{dst}\nExiting")
            sys.exit()


class Checker:

    def check_if_new_mapfile_exists(self, src, filename):
        if not os.path.isfile(os.path.join(src, filename)):
            print(f"new mapfile doesn't exist in \n{src}\nExiting.")
            sys.exit()
        return

    def make_backup_dir_if_not_exists(self, dst, bkup_dirname):
        if not os.path.exists(os.path.join(dst, bkup_dirname)):
            os.makedirs(os.path.join(dst, bkup_dirname))
        return


class Runner:
    incoming_file_path = '/users/home/mkinzler/scripts/utilities/oasisMerger'
    prod_mapfile_path = '/users/home/mkinzler/scripts/utilities/test_dest'
    backup_directory = "oasis_mapfile_backups"
    backup_path = os.path.join(prod_mapfile_path, backup_directory)
    mapfile = 'red_oasis_map'

    def __init__(self, checker, mover):
        self.checker = checker
        self.mover = mover

    def run_it(self):
        # instantiate objects
        my_checker = Checker()
        my_mover = Mover()

        # first, check if new mapfile exists in source path, else exit
        my_checker.check_if_new_mapfile_exists(self.incoming_file_path, self.mapfile)

        # if it does exist, then make backup of the old mapfile
        my_checker.make_backup_dir_if_not_exists(self.prod_mapfile_path, self.backup_directory)
        my_mover.backup_current_file(self.prod_mapfile_path, self.backup_path, self.mapfile)

        # move new mapfile from src to dest (prod) location
        my_mover.move_file(self.incoming_file_path, self.prod_mapfile_path, self.mapfile)

        # move logfile to backup destination path
        for logfile in glob.glob('*log*'):
            my_mover.backup_current_file(self.incoming_file_path, self.backup_path, logfile)


def main():
    my_runner = Runner(Checker(), Mover())
    my_runner.run_it()


if __name__ == '__main__':
    main()
# everything works
