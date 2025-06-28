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
from collections import defaultdict

if __name__ == "__main__":
    parent_path = script_directory.parent
    tabix_dir = parent_path / "vcf/tabix_output"

    root_outdir = parent_path / "vcf/all_vn_genomes"
    infiles = glob.glob(join(tabix_dir, "*.txt"))
    target_value = '0|0'
    
    dir2files = defaultdict(list)
    for infile in infiles:
        if os.path.getsize(infile) <= 0:
            continue
        
        print(f"Input file: {infile}")
        sdir = basename(infile).replace(".txt", "")
        subdir = join(root_outdir, sdir)
        if not os.path.exists(subdir):
            os.makedirs(subdir, exist_ok=True)

        try:
            df = pd.read_csv(infile, sep = "\t", skiprows=skiprows, usecols=cols)
            if df.empty:
                continue

            for col in df.columns:
                if col in metacols:
                    continue
                
                all_equal_target_value = (df[col] == target_value).all()

                if not all_equal_target_value:
                    outfile = join(subdir, f"{col}.csv")
                    ndf = df[metacols + [col]][df[col] != target_value]
                    if ndf.empty:
                        continue 
                    ndf.to_csv(outfile, index=False)
                    dir2files[sdir].append(col) 
                    pass
        except Exception:
            print(" ------ ERRROR ")
            print(infile)
            print(traceback.format_exc())
            pass

    sorted_dict = sorted(dir2files.items(), key=lambda item: len(item[1]), reverse=True)
    for k,v in sorted_dict:
        #print(f"{k}, {len(v)}, {v}")
        print(f"{k}, {len(v)}")
    pass