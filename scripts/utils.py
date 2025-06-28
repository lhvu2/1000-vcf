indir = "/home/lhvu/bio/1000-vcf/vcf/"
outdir = "/home/lhvu/bio/1000-vcf/vcf/parsed"

metacols = ['#CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT']
genome_ids = ['HG02070', 'HG01849', 'HG01874', 'HG01599', 'HG01872', 'HG02121', 'HG02078', 'HG02128', 'HG02087', 'HG01846', 'HG02113', 'HG02088', 'HG02140', 'HG02086', 'HG02023', 'HG01843', 'HG02081', 'HG01865', 'HG01597', 'HG01873', 'HG02085', 'HG02139', 'HG01847', 'HG02073', 'HG01848', 'HG02079', 'HG02133', 'HG02028', 'HG01869', 'HG02035', 'HG02137', 'HG02029', 'HG01842', 'HG02138', 'HG02116', 'HG02084', 'HG01867', 'HG02025', 'HG01844', 'HG01850', 'HG02136', 'HG02075', 'HG01857', 'HG01855', 'HG02016', 'HG01866', 'HG02522', 'HG02048', 'HG02026', 'HG02130', 'HG01861', 'HG01596', 'HG02047', 'HG01841', 'HG02060', 'HG01863', 'HG02134', 'HG02067', 'HG02020', 'HG01878', 'HG02072', 'HG01864', 'HG01870', 'HG02512', 'HG02069', 'HG01871', 'HG02141', 'HG02082', 'HG01860', 'HG02049', 'HG01859', 'HG01845', 'HG02142', 'HG02122', 'HG01868', 'HG02019', 'HG01858', 'HG02127', 'HG02032', 'HG02017', 'HG02513', 'HG02057', 'HG02040', 'HG02521', 'HG02050', 'HG02031', 'HG01853', 'HG02061', 'HG01840', 'HG02131', 'HG01851', 'HG02058', 'HG01595', 'HG01598', 'HG02064', 'HG01600', 'HG01862', 'HG01852', 'HG02076']
cols = metacols + genome_ids

skiprows = [i for i in range(19)]

genes_data = [
    {"gene": "SOD1", "chromosome": "21", "location": "31659693-31668931", "url": "https://www.ncbi.nlm.nih.gov/gene/?term=6647%5Buid%5D"},
    {"gene": "FUS", "chromosome": "16", "location": "31180110-31194871", "url": "https://www.ncbi.nlm.nih.gov/gene/?term=2521"},
    {"gene": "TARDBP", "chromosome": "1", "location": "11012654-11030528", "url": "https://www.ncbi.nlm.nih.gov/gene/23435"},
    {"gene": "C9ORF72", "chromosome": "9", "location": "27546546-27573866", "url": "https://www.ncbi.nlm.nih.gov/gene/203228"},
    {"gene": "ATXN2", "chromosome": "12", "location": "111452214-111599673", "url": "https://www.ncbi.nlm.nih.gov/gene/6311"},
    {"gene": "SQSTM1", "chromosome": "5", "location": "179806393-179838078", "url": "https://www.ncbi.nlm.nih.gov/gene/8878"},
    {"gene": "VCP", "chromosome": "9", "location": "35056064-35072625", "url": "https://www.ncbi.nlm.nih.gov/gene/7415"},
    {"gene": "OPTN", "chromosome": "10", "location": "13100082-13138308", "url": "https://www.ncbi.nlm.nih.gov/gene/10133"},
    # {"gene": "UBQLN2", "chromosome": "X chromosome", "location": "56563627-56567868", "url": "https://www.ncbi.nlm.nih.gov/gene/29978"},
    {"gene": "ANG", "chromosome": "14", "location": "20684177-20694186", "url": "https://www.ncbi.nlm.nih.gov/gene/283"},
    {"gene": "SETX", "chromosome": "9", "location": "132261356-132356744", "url": "https://www.ncbi.nlm.nih.gov/gene/23064"},
    {"gene": "SIGMAR1", "chromosome": "9", "location": "34634722-34637787", "url": "https://www.ncbi.nlm.nih.gov/gene/10280"},
    {"gene": "MATR3", "chromosome": "5", "location": "139274101-139331677", "url": "https://www.ncbi.nlm.nih.gov/gene/9782"},
    {"gene": "TAF15", "chromosome": "17", "location": "35809484-35847242", "url": "https://www.ncbi.nlm.nih.gov/gene/8148"},
    {"gene": "EWSR1", "chromosome": "22", "location": "29268268-29300521", "url": "https://www.ncbi.nlm.nih.gov/gene/2130"},
    {"gene": "ALS2", "chromosome": "2", "location": "201700267-201780933", "url": "https://www.ncbi.nlm.nih.gov/gene/57679"},
    {"gene": "VAPB", "chromosome": "20", "location": "58389229-58451101", "url": "https://www.ncbi.nlm.nih.gov/gene/9217"},
    {"gene": "FIG4", "chromosome": "6", "location": "109691296-109825426", "url": "https://www.ncbi.nlm.nih.gov/gene/9896"},
    {"gene": "NEK1", "chromosome": "4", "location": "169392809-169612583", "url": "https://www.ncbi.nlm.nih.gov/gene/4750"},
    {"gene": "ELP3", "chromosome": "8", "location": "28090232-28191153", "url": "https://www.ncbi.nlm.nih.gov/gene/55140"},
    {"gene": "CHMP2B", "chromosome": "3", "location": "87227309-87255556", "url": "https://www.ncbi.nlm.nih.gov/gene/25978"},
    {"gene": "hnRNPa1", "chromosome": "12", "location": "54280726-54287087", "url": "https://www.ncbi.nlm.nih.gov/gene/3178"},
    {"gene": "NEFH", "chromosome": "22", "location": "29480218-29491390", "url": "https://www.ncbi.nlm.nih.gov/gene/4744"},
    {"gene": "PRPH", "chromosome": "12", "location": "49295147-49298686", "url": "https://www.ncbi.nlm.nih.gov/gene/5630"},
    {"gene": "CHCHD10", "chromosome": "22", "location": "23765834-23767972", "url": "https://www.ncbi.nlm.nih.gov/gene/400916"},
    {"gene": "C19ORF12", "chromosome": "19", "location": "29698886-29715789", "url": "https://www.ncbi.nlm.nih.gov/gene/83636"},
    {"gene": "ERBB4", "chromosome": "2", "location": "211375717-212538802", "url": "https://www.ncbi.nlm.nih.gov/gene/2066"},
    {"gene": "PON1-3", "chromosome": "7", "location": "95297676-95324532", "url": "https://www.ncbi.nlm.nih.gov/gene/5444"},
    {"gene": "DAO", "chromosome": "12", "location": "108880092-108901043", "url": "https://www.ncbi.nlm.nih.gov/gene/1610"},
    {"gene": "DCTN1", "chromosome": "2", "location": "74361155-74391866", "url": "https://www.ncbi.nlm.nih.gov/gene/1639"},
    {"gene": "PFN1", "chromosome": "17", "location": "4945652-4948530", "url": "https://www.ncbi.nlm.nih.gov/gene/5216"},
    {"gene": "SPG11", "chromosome": "15", "location": "44562696-44663662", "url": "https://www.ncbi.nlm.nih.gov/gene/80208"},
    {"gene": "TUBA4A", "chromosome": "2", "location": "219249710-219254740", "url": "https://www.ncbi.nlm.nih.gov/gene/7277"},
    {"gene": "CREST", "chromosome": "20", "location": "62143769-62182514", "url": "https://www.ncbi.nlm.nih.gov/gene/26039"},
    {"gene": "CHRNA3", "chromosome": "15", "location": "78593052-78620996", "url": "https://www.ncbi.nlm.nih.gov/gene/1136"},
    {"gene": "hnRNPA2B1", "chromosome": "7", "location": "26189927-26200746", "url": "https://www.ncbi.nlm.nih.gov/gene/3181"},
    {"gene": "PNPLA6", "chromosome": "19", "location": "7534164-7561767", "url": "https://www.ncbi.nlm.nih.gov/gene/10908"}
]

