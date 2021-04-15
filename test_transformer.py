from oasis_mapfile_transformer import Cleaner
from pandas import DataFrame

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
    list_of_stuff_for_dataframe = ['a','b','c']
    dut = Cleaner().make_dataframe(list_of_stuff_for_dataframe)
    assert isinstance(dut, DataFrame)
