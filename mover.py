import shutil
import os
import datetime
import sys
import glob


class Mover:

    def move_file(self, filename, src, dst, *timestamp):
        try:
            if timestamp:
                bkup_date = datetime.datetime.today().strftime('%Y-%m-%d-%s')
                shutil.move(os.path.join(src, filename),
                            os.path.join(dst, filename + "." + bkup_date))
            else:
                shutil.move(os.path.join(src, filename), os.path.join(dst, filename))
        except FileNotFoundError:
            print(f'File not found in path \n{src}\nExiting')
            sys.exit()
        except PermissionError:
            print(f'Cannot write to \n{dst}\nCheck path permissions\nExiting')
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
    incoming_file_path = '/users/home/mkinzler/scripts/utilities/test_incoming'
    prod_mapfile_path = '/users/home/mkinzler/scripts/utilities/test_destination'
    backup_directory = 'backups'
    backup_path = os.path.join(prod_mapfile_path, backup_directory)
    mapfile = 'mapfile'
    my_timestamp = True

    def __init__(self, checker, mover):
        self.checker = checker
        self.mover = mover

    def run_it(self):

        self.checker.check_if_new_mapfile_exists(self.incoming_file_path, self.mapfile)

        # check is backup path exists, if not then make it
        self.checker.make_backup_dir_if_not_exists(self.prod_mapfile_path, self.backup_directory)

        # move current mapfile from the prod path to the backup path, add a timestamp
        self.mover.move_file(self.mapfile, self.prod_mapfile_path, self.backup_path, self.timestamp_it)

        # then move new mapfile from source path to production path
        self.mover.move_file(self.mapfile, self.incoming_file_path, self.prod_mapfile_path)

        # move logfile to backup destination path, and timestamp it
        for logfile in glob.glob('*log*'):
            self.mover.move_file(logfile, self.incoming_file_path, self.backup_path, self.timestamp_it)


def main():
    my_runner = Runner(Checker(), Mover())
    my_runner.run_it()


if __name__ == '__main__':
    main()
