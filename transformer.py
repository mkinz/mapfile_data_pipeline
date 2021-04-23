import pandas as pd
import re
import datetime


class Loader:
    """
    Class for loading data. Can load directly to dataframe,
    or to list for transformation.
    """

    def load_data_to_list(self, input_file):
        with open(input_file, 'r') as f:
            input_file_data = [line for line in f]
        return input_file_data

    def load_data_to_dataframe(self, input_file):
        return pd.read_csv(input_file, header=None)


class Cleaner:
    '''
    Class for cleaning an input file.
    It can remove leading hashes and whitespaces,
    and filters out data levels longer than len(30)
    '''

    def remove_hashes(self, list_of_input_file_data) -> list:

        symbols_to_remove = ['#']
        cleaned_data = []

        for line in list_of_input_file_data:
            if not any(symbol in line for symbol in symbols_to_remove):
                cleaned_data.append(line.strip())
        return cleaned_data

    def filter_longer_than_30_chars(self, list_of_input_file_data) -> list:

        # split on the space, capturing space group to maintain spacing
        split_data = []
        for item in list_of_input_file_data:
            split_data.append(re.split(r'(\s+)', item))

        # apply len(30) filter
        filtered_data = [a for a in split_data if len(a[0]) <= 30]

        # rejoin data, and lstrip to removing leading whitespace
        add_spaces_back = ["".join(a).lstrip().strip() for a in filtered_data]
        return add_spaces_back

    def filter_blank_lines(self, list_of_input_file_data):
        non_empty_lines = [line for line in list_of_input_file_data if line.strip() != ""]
        return non_empty_lines

    def make_dataframe(self, list_of_input_file_data):
        return pd.DataFrame(list_of_input_file_data)


class Joiner:
    '''
    This class provided methods for joining two dataframes together
    and writing the joined files to disk.
    '''

    def join_files(self, dataframe_a, dataframe_b):
        newfile = dataframe_a.append(dataframe_b)
        return newfile

    def write_joined_files_to_disk(self, joined_dataset):
        return joined_dataset.to_csv("oasis_map_files/red_oasis_map", index=False, header=None)


class Logger:
    '''
    This class provides logging capability.
    '''

    def build_logger_header(self):
        logger_header = [f"Application run on: "
                         f"{datetime.datetime.now()}\n",
                         'The following data levels will be removed '
                         'from the addendum file because they are >30 characters:\n\n']
        return logger_header

    def build_logger_contents_of_removed_items(self, list_of_lines_from_input) -> list:

        split_data = []
        for item in list_of_lines_from_input:
            split_data.append(re.split(r'(\s+)', item))

        items_to_remove = [line for line in split_data if len(line[0]) > 30 and not line[0].startswith("#")]
        filtered_items = ["".join(a).strip() for a in items_to_remove]
        return filtered_items

    def create_log_in_memory(self, header_information, list_of_logged_data):
        logger = []
        for header_item in header_information:
            logger.append(header_item)
        for logged_item in list_of_logged_data:
            logger.append(logged_item + '\n')

        return logger

    def write_log_to_disk(self, log_in_memory):
        with open('logs/joined_mapfile_log','w') as f:
            for line in log_in_memory:
                f.write(line)
        return


class Runner:

    mapfile_path = '/path/to/mapfile'
    addendum_path = '/path/to/addendum'

    def __init__(self, loader, cleaner, joiner, logger):
        self.loader = loader
        self.cleaner = cleaner
        self.joiner = joiner
        self.logger = logger

    def run_it(self):

        # LOAD data

        mapfile_dataframe = self.loader.load_data_to_dataframe(self.mapfile_path)
        addendum_datalist = self.loader.load_data_to_list(self.addendum_path)

        # CLEAN data

        # remove hashes in addendum
        list_of_items_from_addendum_with_hashes_removed = self.cleaner.remove_hashes(addendum_datalist)

        # filter addendum data where datalevel length is >30
        filtered_addendum_data = self.cleaner.filter_longer_than_30_chars(
            list_of_items_from_addendum_with_hashes_removed)

        # filter empty lines in addendum
        filtered_empty_lines = self.cleaner.filter_blank_lines(filtered_addendum_data)

        # build new dataframe object of cleaned data
        addendum_dataframe = self.cleaner.make_dataframe(filtered_empty_lines)

        # JOIN data

        # join the map and addendum files together
        joined_data = self.joiner.join_files(mapfile_dataframe, addendum_dataframe)

        # LOG data

        header_info = self.logger.build_logger_header()
        contents_info = self.logger.build_logger_contents_of_removed_items(addendum_datalist)
        logger_in_memory = self.logger.create_log_in_memory(header_info, contents_info)

        # WRITE data

        self.joiner.write_joined_files_to_disk(joined_data)
        self.logger.write_log_to_disk(logger_in_memory)


def main():
    my_runner = Runner(Loader(), Cleaner(), Joiner(), Logger())
    my_runner.run_it()


if __name__ == '__main__':
    main()

# everything works
