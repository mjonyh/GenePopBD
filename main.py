import sys

from classes.load import Load
from classes.forensic import Forensic

input_file = sys.argv[1]

csv_file = Load(input_file)

data = csv_file.load()

r_locas = ['Locas']
r_homo = ['Homo']
r_hetero = ['Hetero']
r_per_homo = ['Per Homo']
r_per_hetero = ['Per Hetero']

r_poe = ['PoE']
r_tpi = ['TPI']
r_allele = ['Allele']
r_pic = ['PIC']
r_mp = ['MP']
r_pod = ['PoD']

for j in range(1, len(data[0])-1,2):
  allele_l = []
  allele_r = []
  allele_g = []

  for i in range(1,len(data)):
    allele_l.append(data[i][j])
    allele_r.append(data[i][j+1])
    allele_g.append(data[i][j]+','+data[i][j+1])

  'Initiating forensic class'

  forensic = Forensic(allele_l, allele_r, allele_g)

  per_homo_hetero = forensic.per_homo_hetero()

  'Saving locas, homo, hetero in array'

  r_locas.append(data[0][j])
  r_homo.append(per_homo_hetero[1])
  r_per_homo.append(per_homo_hetero[3])
  r_hetero.append(per_homo_hetero[2])
  r_per_hetero.append(per_homo_hetero[4])

  'Saving Power of exclusion and Typical Peternity Index in array'

  pat_stats = forensic.paternity_statistics()

  r_poe.append(pat_stats[0])
  r_tpi.append(pat_stats[1])

  'Saving Allele and PIC in array'

  freq_calc = forensic.freq_calc()
  r_allele.append(freq_calc[1])
  r_pic.append(freq_calc[6])

  'Saving Maching Probability and PoD in array'

  geno_calc = forensic.geno_calc()

  r_mp.append(geno_calc[4])
  r_pod.append(geno_calc[5])

print 'Short description'
print '------------------'
print 'Homo: Total number of homogeneus'
print 'Per Homo: Percentage of homogeneus'
print 'Hetero: Total number of Heterogeneus'
print 'Per Hetero: Percentage of Heterogeneus'
print 'PoE: Power of Exclusion'
print 'TPI: Typical Paternity Index'
print '\n'

for i in range(len(r_locas)):
  print r_locas[i], '    \t', r_homo[i], r_per_homo[i], '\t', r_hetero[i], r_per_hetero[i], '\t', r_poe[i], r_tpi[i], r_pic[i], r_mp[i],r_pod[i]

'Writting output file in csv format'
csv_file.down([r_locas, r_homo, r_per_homo, r_hetero, r_per_hetero, r_poe, r_tpi, r_pic, r_mp,r_pod])
