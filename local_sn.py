import numpy as np
import glob
from collections import namedtuple
from astropy.io import fits
from  matplotlib import pyplot as plt
from astropy.io import ascii
from astropy.table import Table

my_files = glob.glob('/Users/MCilento/STARLIGHT/local_sp files/*.BN')
print(my_files)

for path in my_files:
    with open(path) as ofile:
        lines = ofile.readlines()

        if len(lines) < 5:
            continue


        for num, line in enumerate(lines):
            if len(line.split()) > 3:
                if line.split()[3] == 'Mini_j(%)':
                    table_start_value = num + 1

            if len(line.split()) > 1:
                if line.split()[1] == '[N_base]':
                    n_base_value = int(line.split()[0])

        lines = lines[table_start_value: table_start_value + n_base_value + 1]

        data = ascii.read(lines)
        t = Table(data)

        t.keep_columns(['col2', 'col3', 'col5', 'col6'])

        #my_x_j = np.array(t['col2'])
        #my_Mini_j = np.array(t['col3'])
        #my_age = np.array(t['col5'])
        #my_Z_j = np.array(t['col6'])

        print(t)





if __name__ == '__main__':
    print('hello world')