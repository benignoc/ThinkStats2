"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function
# from chap01soln import CleanFemResp

# import numpy as np
import sys

import nsfg
import thinkstats2

def readFemResp(dct_file='2002FemResp.dct',
                dat_file='2002FemResp.dat.gz'):
    """ Reads the FemResp compressed file and returns a df.

    dct_file: definition of dat_file file
    dat_file: compressed data

    returns: 
        df: dataframe of data in filename
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip')
    nsfg.CleanFemResp(df)
    return df

def ValidatePregnum(resp):
    """Validate pregnum in the respondent file

    resp: respondent df
    returns:
        Boolean: False if not equal True if equal
    """
    # Read pregnancy df
    preg = nsfg.ReadFemPreg()

    # Make map for caseid to list indices
    preg_map = nsfg.MakePregMap(preg)

    for ix, pregnum in resp.pregnum.items():
        caseid = resp.caseid[ix]
        indices = preg_map[caseid]

        # check pregnum is equal to indices count
        if len(indices) != pregnum:
            print(caseid, len(indices), pregnum)
            return False

    return True

def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    resp = readFemResp()

    assert(len(resp)==7643)
    assert(resp.pregnum.value_counts()[1]==1267)
    assert(ValidatePregnum(resp))

    print('%s: All tests passed.' % script)

if __name__ == '__main__':
    main(*sys.argv)
