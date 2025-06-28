import subprocess
import os
from pathlib import Path
from os.path import join, basename
from utils import genes_data
import pandas as pd
import traceback

from utils import indir
from utils import root_outdir
from utils import skiprows
from utils import genome_ids
from utils import metacols
from utils import cols

script_directory = Path(__file__).parent.resolve()

import glob

"""
Input: tabix .txt output files that include all 2500 genomes
Output: filter only VN genomes and save a txt file for each gene
"""
if __name__ == "__main__":
    parent_path = script_directory.parent
    tabix_dir = parent_path / "vcf/tabix_output"

    root_outdir = parent_path / "vcf/vn_genomes"
    infiles = glob.glob(join(tabix_dir, "*.txt"))
    target_value = '0|0'
    
    for infile in infiles:
        print(infile)
        outfile = join(root_outdir, basename(infile))
        try:
            df = pd.read_csv(infile, sep = "\t", skiprows=skiprows, usecols=cols)
            mask = (df[genome_ids] == target_value).all(axis=1)
            matching_rows = df[mask]
            non_matching_rows = df[~mask]
            non_matching_rows.to_csv(outfile, index=False)
            pass
        except Exception:
            print(" ------ ERRROR ")
            print(infile)
            print(traceback.format_exc())
            pass
        pass