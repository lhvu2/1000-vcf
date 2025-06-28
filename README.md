# 1000-vcf

Link to download .gz files for all chromosomes:

https://hgdownload.soe.ucsc.edu/gbdb/hg38/1000Genomes/

# Order
1. run_tabix.py
2. als_genes_all_vn_genomes_txt.py
3. create_per_vn_genome_csv.py

## Use a tool
https://pypi.org/project/vcf2pandas/
pip install vcf2pandas


# All VN Genomes 
## Gene List with Chromosome and Number of VN genomes that have at least one NON 0|0

| Gene Name              | Chromosome | Number of VN Genomes |
|-------------------|------------|-------|
| NEK1              | 4          | 99    |
| FIG4              | 6          | 99    |
| MATR3             | 5          | 99    |
| ELP3              | 8          | 99    |
| CHRNA3            | 15         | 99    |
| ALS2              | 2          | 99    |
| SETX              | 9          | 99    |
| EWSR1             | 22         | 99    |
| OPTN              | 10         | 99    |
| SPG11             | 15         | 99    |
| PFN1              | 17         | 99    |
| CREST             | 20         | 99    |
| TUBA4A            | 2          | 99    |
| ANG               | 14         | 99    |
| CHMP2B            | 3          | 99    |
| NEFH              | 22         | 99    |
| TAF15             | 17         | 99    |
| SQSTM1            | 5          | 99    |
| VAPB              | 20         | 99    |
| ERBB4             | 2          | 99    |
| C9ORF72           | 9          | 99    |
| FUS               | 16         | 99    |
| ATXN2             | 12         | 99    |
| hnRNPa1           | 12         | 99    |
| DAO               | 12         | 99    |
| PON1-3            | 7          | 99    |
| TARDBP            | 1          | 98    |
| SIGMAR1           | 9          | 98    |
| DCTN1             | 2          | 97    |
| CHCHD10           | 22         | 97    |
| hnRNPA2B1         | 7          | 93    |
| SOD1              | 21         | 92    |
| VCP               | 9          | 81    |
| PRPH              | 12         | 12    |




| Gene           | Chromosome | File Path                                               |
|----------------|------------|----------------------------------------------------------|
| NEK1           | 4          | bio/1000-vcf/vcf/tabix_output/NEK1.chr4.txt             |
| TARDBP         | 1          | bio/1000-vcf/vcf/tabix_output/TARDBP.chr1.txt           |
| FIG4           | 6          | bio/1000-vcf/vcf/tabix_output/FIG4.chr6.txt             |
| MATR3          | 5          | bio/1000-vcf/vcf/tabix_output/MATR3.chr5.txt            |
| ELP3           | 8          | bio/1000-vcf/vcf/tabix_output/ELP3.chr8.txt             |
| CHRNA3         | 15         | bio/1000-vcf/vcf/tabix_output/CHRNA3.chr15.txt          |
| ALS2           | 2          | bio/1000-vcf/vcf/tabix_output/ALS2.chr2.txt             |
| SETX           | 9          | bio/1000-vcf/vcf/tabix_output/SETX.chr9.txt             |
| EWSR1          | 22         | bio/1000-vcf/vcf/tabix_output/EWSR1.chr22.txt           |
| OPTN           | 10         | bio/1000-vcf/vcf/tabix_output/OPTN.chr10.txt            |
| SPG11          | 15         | bio/1000-vcf/vcf/tabix_output/SPG11.chr15.txt           |
| PFN1           | 17         | bio/1000-vcf/vcf/tabix_output/PFN1.chr17.txt            |
| DCTN1          | 2          | bio/1000-vcf/vcf/tabix_output/DCTN1.chr2.txt            |
| CREST          | 20         | bio/1000-vcf/vcf/tabix_output/CREST.chr20.txt           |
| TUBA4A         | 2          | bio/1000-vcf/vcf/tabix_output/TUBA4A.chr2.txt           |
| ANG            | 14         | bio/1000-vcf/vcf/tabix_output/ANG.chr14.txt             |
| CHMP2B         | 3          | bio/1000-vcf/vcf/tabix_output/CHMP2B.chr3.txt           |
| NEFH           | 22         | bio/1000-vcf/vcf/tabix_output/NEFH.chr22.txt            |
| hnRNPA2B1      | 7          | bio/1000-vcf/vcf/tabix_output/hnRNPA2B1.chr7.txt        |
| TAF15          | 17         | bio/1000-vcf/vcf/tabix_output/TAF15.chr17.txt           |
| SOD1           | 21         | bio/1000-vcf/vcf/tabix_output/SOD1.chr21.txt            |
| SQSTM1         | 5          | bio/1000-vcf/vcf/tabix_output/SQSTM1.chr5.txt           |
| SIGMAR1        | 9          | bio/1000-vcf/vcf/tabix_output/SIGMAR1.chr9.txt          |
| VAPB           | 20         | bio/1000-vcf/vcf/tabix_output/VAPB.chr20.txt            |
| ERBB4          | 2          | bio/1000-vcf/vcf/tabix_output/ERBB4.chr2.txt            |
| VCP            | 9          | bio/1000-vcf/vcf/tabix_output/VCP.chr9.txt              |
| C9ORF72        | 9          | bio/1000-vcf/vcf/tabix_output/C9ORF72.chr9.txt          |
| FUS            | 16         | bio/1000-vcf/vcf/tabix_output/FUS.chr16.txt             |
| ATXN2          | 12         | bio/1000-vcf/vcf/tabix_output/ATXN2.chr12.txt           |
| hnRNPa1        | 12         | bio/1000-vcf/vcf/tabix_output/hnRNPa1.chr12.txt         |
| PRPH           | 12         | bio/1000-vcf/vcf/tabix_output/PRPH.chr12.txt            |
| DAO            | 12         | bio/1000-vcf/vcf/tabix_output/DAO.chr12.txt             |
| PON1-3         | 7          | bio/1000-vcf/vcf/tabix_output/PON1-3.chr7.txt           |
| CHCHD10        | 22         | bio/1000-vcf/vcf/tabix_output/CHCHD10.chr22.txt         |


# ALL Genomes:
| Gene           | Chromosome | Value |
|----------------|------------|-------|
| FIG4           | chr6       | 2548  |
| MATR3          | chr5       | 2548  |
| ELP3           | chr8       | 2548  |
| CHRNA3         | chr15      | 2548  |
| ALS2           | chr2       | 2548  |
| SETX           | chr9       | 2548  |
| EWSR1          | chr22      | 2548  |
| OPTN           | chr10      | 2548  |
| SPG11          | chr15      | 2548  |
| PFN1           | chr17      | 2548  |
| CREST          | chr20      | 2548  |
| CHMP2B         | chr3       | 2548  |
| NEFH           | chr22      | 2548  |
| SQSTM1         | chr5       | 2548  |
| VAPB           | chr20      | 2548  |
| ERBB4          | chr2       | 2548  |
| C9ORF72        | chr9       | 2548  |
| FUS            | chr16      | 2548  |
| ATXN2          | chr12      | 2548  |
| PON1-3         | chr7       | 2548  |
| TAF15          | chr17      | 2547  |
| ANG            | chr14      | 2546  |
| TUBA4A         | chr2       | 2537  |
| DAO            | chr12      | 2534  |
| TARDBP         | chr1       | 2530  |
| CHCHD10        | chr22      | 2521  |
| hnRNPa1        | chr12      | 2466  |
| SIGMAR1        | chr9       | 2438  |
| VCP            | chr9       | 2394  |
| hnRNPA2B1      | chr7       | 2377  |
| DCTN1          | chr2       | 2299  |
| SOD1           | chr21      | 2257  |
| PRPH           | chr12      | 1332  |


