import pandas as pd
import os
from os.path import join, basename

ids = ['HG02070','HG01849','HG01874','HG01599','HG02525','HG02015','HG01872','HG02121','HG02083','HG02078','HG02128','HG02045','HG02087','HG02027','HG01846','HG02113','HG02088','HG02126','HG02140','HG02086','HG02023','HG01843','HG02081','HG01865','HG01597','HG01873','HG02085','HG02139','HG01847','HG02073','HG02524','HG01848','HG02079','HG02133','HG02028','HG01869','HG02523','HG02035','HG02137','HG02071','HG02029','HG01842','HG02138','HG02116','HG02084','HG02068','HG02080','HG01867','HG02025','HG02120','HG01844','HG01850','HG02136','HG02075','HG01857','HG01855','HG02077','HG02016','HG01866','HG02024','HG02522','HG02048','HG02026','HG02130','HG01861','HG01596','HG02047','HG02129','HG01841','HG02060','HG01863','HG02134','HG02059','HG02046','HG02067','HG02020','HG01878','HG02526','HG02072','HG01864','HG01870','HG02512','HG02069','HG01871','HG02141','HG02082','HG02074','HG01860','HG02049','HG02056','HG02135','HG01859','HG01845','HG02142','HG02132','HG02122','HG01868','HG02019','HG01858','HG02127','HG02032','HG02017','HG02513','HG02057','HG02040','HG02521','HG02050','HG02031','HG01853','HG02061','HG01840','HG02131','HG01851','HG02030','HG02058','HG01595','HG02018','HG01598','HG02064','HG01600','HG02514','HG01862','HG01852','HG02076']

if __name__ == "__main__":
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(script_directory)
    indir = "/home/lhvu/bio/1000-vcf/vcf/small_test"
    infile = join(indir, "ALL.chr21.shapeit2_integrated_snvindels_v2a_27022019.GRCh38.phased.short.vcf")
    skiprows = [i for i in range(19)]
    df = pd.read_csv(infile, sep = "\t", skiprows=skiprows)

    notins = list()
    ins = list()
    for e in ids:
        if e not in df.columns:
            notins.append(e)
            #print(e)
        else:
            ins.append(e)
    st = " ".join([f'-F {e}' for e in ins])
    cmd = "-F CHROM  -F POS     -F ID     -F REF    -F ALT   -F  QUAL   -F FILTER  -F INFO   -F  FORMAT " + st

    metacols = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
    ndf = df[metacols + ins] 
    pass