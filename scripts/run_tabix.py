import subprocess
import os
from pathlib import Path
from os.path import join, basename
from utils import genes_data

"""
Run tabix to extract, for each gene, the location in each chromosome.
Input: gene, chromosome, location in each chromosome
Output: an extracted file for each gene with meta header reading for filtering columns
"""
script_directory = Path(__file__).parent.resolve()

if __name__ == "__main__":
    print(script_directory)
    parent_path = script_directory.parent
    tabix_dir = parent_path / "vcf/tabix_output"
    for elem in genes_data:
        print(elem)
        tabix_input_variant_filename = f"ALL.chr{elem['chromosome']}.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.vcf.gz"
        tabix_input_variant_filepath = parent_path / f"vcf/zip/{tabix_input_variant_filename}"
        tabix_output_filepath = tabix_dir / f"{elem['gene']}.chr{elem['chromosome']}.txt"

        if os.path.exists(tabix_output_filepath):
            continue

        cmd = f"tabix -hf {tabix_input_variant_filepath} {elem['chromosome']}:{elem['location']} > {tabix_output_filepath}" 
        print(cmd)
        try:
            result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
            print("Command executed successfully.")
            print("Stdout:", result.stdout)
            print("Stderr:", result.stderr)
        except subprocess.CalledProcessError as e:
            print(f"Command failed with error: {e}")
            print("Stderr:", e.stderr)
        
        pass