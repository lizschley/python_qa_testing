'''
This tool lists all the files, along with their paths within a given directory

    Purpose, with DELETE == False, just get list of all the filepaths with given criteria

    Purpose with DELETE == True: In this context, delete all the reports

Currently set up to delete .json files under the reports directory


At commandline:
    $ python utilities/delete_pickles.py
'''
import os

# change to True to delete the reports, but first check the logic (will only delete .json files currently)
DELETE = False

EXCLUDE_FIRST_LETTER = ['.']
EXCLUDE_DIR = ['untitled', 'External Libraries', 'include', 'lib', 'bin', 'static']
EXTENSION_TO_DELETE = '.json'

'''
    For the given path, get the List of all files in the directory tree
'''


def list_of_files(directory_name):
    # create a list of file and sub directories
    # names in the given directory
    file_list = os.listdir(directory_name)
    all_files = list()
    # Iterate over all the entries
    for entry in file_list:
        # Note-this excludes files and anything under the directories that start with an item in
        # EXCLUDE_FIRST_LETTER
        if do_exclude(entry):
            continue
        # Create full path
        full_path = os.path.join(directory_name, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(full_path):
            all_files = all_files + list_of_files(full_path)
        else:
            all_files.append(full_path)

    return all_files


def do_exclude(entry):
    if entry[0] in EXCLUDE_FIRST_LETTER:
        return True
    if entry in EXCLUDE_DIR:
        return True
    return False


def exclude_from_directory_with_path(entry):
    # this will need to be changed for a windows environment
    dir_list = entry.split('/')
    exclude = False
    for item in dir_list:
        if not item:
            continue
        if do_exclude(item):
            exclude = True
            break
    return exclude


def delete_files_for_extension(file_list):
    num_deleted = 0
    for elem in file_list:
        if elem.endswith(EXTENSION_TO_DELETE):
            os.remove(elem)
            print(f'deleting {elem}')
            num_deleted += 1
        # print(elem)
    return num_deleted


def base_dir():
    base_dir = os.path.realpath('.')
    if 'utilities' in base_dir:
        return os.path.realpath('..')
    return base_dir


def main():
    # you may need to change this to suit your situation
    root_dir = base_dir()

    directory_name = root_dir + '/reports'

    # Get the list of all files in directory tree at given path
    file_list = list_of_files(directory_name)

    print(('#1 filelist size, excluding files w/ excluded criteria & including'
           f'# files to be deleted == {len(file_list)}'))

    if DELETE:
        if len(EXTENSION_TO_DELETE) > 0:
            pickle_num = delete_files_for_extension(file_list)
            print(f'**** number of pickles deleted == {pickle_num} ************')
    else:
        for elem in file_list:
            print(elem)
        return

    # Print the files (shouldn't have any of the deleted files)
    file_list = list_of_files(directory_name)

    print(('#2 list size, including files (not directories) w/ excluded criteria, but not deleted files '
           f'== {len(file_list)}'))

    for elem in file_list:
        print(elem)


if __name__ == '__main__':
    main()
