import glob
import os
import sys


def file_rename(file_list, replace_name):
    for file_name in file_list:
        if file_name == './file_edit_program.py':
            print(file_name, 'は実行中のプログラムのためpassしました')
            continue
        new_file_name = file_name.replace(replace_name[0], replace_name[1])
        if file_name != new_file_name:
            print(file_name, 'から', new_file_name, 'に名前を変更しました')
        os.rename(file_name, new_file_name)


def proof_within_file(file_list, replace_name):
    for file_name in file_list:
        if file_name == './file_edit_program.py':
            print(file_name, 'は実行中のプログラムのためpassしました')
            continue
        with open(file_name) as file:
            line_data_list = file.read()

        replaced_data = line_data_list.replace(replace_name[0], replace_name[1])

        with open(file_name, mode='w') as file:
            file.write(replaced_data)
        if line_data_list != replaced_data:
            print(file_name, 'に含まれる', replace_name[0], 'を', replace_name[1], 'に置換しました')


def main():
    args = sys.argv
    file_list = glob.glob('./*.py')
    replace_name = ['nock', 'nock']
    file_rename(file_list, replace_name)
    file_list = glob.glob('./*.py')
    proof_within_file(file_list, replace_name)


if __name__ == '__main__':
    main()
