from pandas import DataFrame

from oasis_mapfile_transformer import Loader
from oasis_mapfile_transformer import Cleaner
from oasis_mapfile_transformer import Joiner
from oasis_mapfile_transformer import Logger


# Test Loader

def test_load_to_list():
    addendum_path = '/path/to/file'
    dut = Loader().load_data_to_list(addendum_path)
    assert isinstance(dut, list)


def test_load_to_dataframe():
    mapfile_path = '/path/to/file'
    dut = Loader().load_data_to_dataframe(mapfile_path)
    assert isinstance(dut, DataFrame)


# Test Cleaner

def test_remove_hashes():
    list_with_hashes = ['#spam', 'eggs']
    dut = Cleaner().remove_hashes(list_with_hashes)
    assert dut == ['eggs']


def test_filter_longer_than_30_chars():
    list_of_long_strings = ['asdfasdfasdfasdfasdfasdfasdfasdfa', 'abc']
    dut = Cleaner().filter_longer_than_30_chars(list_of_long_strings)
    assert dut == ['abc']


def test_filter_empty_lines_in_list():
    list_of_stuff_with_blanks = ['a', 'b', '', 'c']
    dut = Cleaner().filter_blank_lines(list_of_stuff_with_blanks)
    assert dut == ['a', 'b', 'c']


def test_filter_many_space_empty_lines_in_list():
    list_of_stuff_with_many_space_blanks = ['a', 'b', '          ', 'c']
    dut = Cleaner().filter_blank_lines(list_of_stuff_with_many_space_blanks)
    assert dut == ['a', 'b', 'c']


def test_make_dataframe():
    list_of_stuff_for_dataframe = ['a', 'b', 'c']
    dut = Cleaner().make_dataframe(list_of_stuff_for_dataframe)
    assert isinstance(dut, DataFrame)


# Test Joiner

def test_join_dataframes_together():
    df1 = ['a', 'b']
    df2 = ['c', 'd']
    df3 = df1.append(df2)
    dut = Joiner().join_files(df1, df2)
    assert dut == df3


# Test Logger

def test_create_logger_header():
    dut = Logger().build_logger_header()
    assert isinstance(dut, list)


def test_create_logger_contents():
    sample_contents = ['Anchored_OPC_Final_lessthan_MINSPACE                    10000  201']
    dut = Logger().build_logger_contents_of_removed_items(sample_contents)
    assert dut == sample_contents


def test_create_logger_in_memory():
    sample_header = ['Test']
    sample_contents = ['Anchored_OPC_Final_lessthan_MINSPACE                    10000  201']
    dut = Logger().create_log_in_memory(sample_header, sample_contents)
    assert dut[0] == sample_header[0]
    assert dut[1].strip() == sample_contents[0].strip()
