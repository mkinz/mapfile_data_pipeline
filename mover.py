import shutil
import os
import datetime
import sys

class Mover:

    def move_file(self, src, dst, filename):
        try:
            shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
        except FileNotFoundError:
            print("File not found, exiting.")

    def backup_current_oasis_file(self, dst, bkup_dirname, filename):
        try:
            bkup_date = datetime.datetime.today().strftime('%Y-%m-%d-%s')
            shutil.move(os.path.join(dst, filename),
                    os.path.join(dst, bkup_dirname, filename+"."+bkup_date))
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

    source_path = '/users/home/mkinzler/scripts/utilities/test_source'
    destination_path = '/users/home/mkinzler/scripts/utilities/test_dest'
    bkup_dirname = "oasis_mapfile_backups"
    mapfile = 'red_oasis_map'

    def __init__(self, checker, mover):
        self.checker = checker
        self.mover = mover

    def run_it(self):

        #instantiate objects
        myChecker = Checker()
        myMover = Mover()

        # first, check if new mapfile exists in source path, else exit
        myChecker.check_if_new_mapfile_exists(self.source_path, self.mapfile)

        # if it does exist, then make backup of the old mapfile
        myChecker.make_backup_dir_if_not_exists(self.destination_path, self.bkup_dirname)
        myMover.backup_current_oasis_file(self.destination_path, self.bkup_dirname, self.mapfile)

        # move new mapfile from src to dest (prod) location
        myMover.move_file(self.source_path, self.destination_path, self.mapfile)

def main():
    myRunner = Runner(Checker(), Mover())
    myRunner.run_it()

if __name__ == '__main__':
    main()


