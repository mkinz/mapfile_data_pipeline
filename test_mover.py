import os
import pytest

from mover import Checker
from mover import Mover


def test_read_access_to_incoming_path():
    incoming_file_path = '/incoming/file/path/'
    assert os.access(incoming_file_path, os.R_OK)


def test_write_access_to_prod_mapfile_path():
    prod_mapfile_path = '/production/file/path/'
    assert os.access(prod_mapfile_path, os.W_OK)


def test_write_access_to_prod_backup_directory_path():
    backup_directory = '/production/file/path/backups/'
    assert os.access(backup_directory, os.W_OK)


def test_check_if_new_file_exists():
    incoming_file_path = '/incoming/file/path/'
    myfile = 'my_test_file'
    dut = Checker()
    with pytest.raises(SystemExit):
        dut.check_if_new_mapfile_exists(incoming_file_path, myfile)


def test_make_backup_dir():
    prod_mapfile_path = '/incoming/file/path/'
    backup_directory = 'backups'
    dut = Checker()
    assert dut.make_backup_dir_if_not_exists(prod_mapfile_path, backup_directory) == None


def test_mover_exits_if_file_not_found_error():
    dut = Mover()
    with pytest.raises(SystemExit):
        dut.move_file('hello', '/incoming/file/path/', '/production/file/path/', True)


def test_mover_exits_if_no_write_permission():
    dut = Mover()
    with pytest.raises(SystemExit):
        dut.move_file('real_file', '/production/file/path/', '/', True)
