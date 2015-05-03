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

for j in range(1, len(data[0])-1,2):
  allele_l = []
  allele_r = []

  for i in range(1,len(data)):
    allele_l.append(data[i][j])
    allele_r.append(data[i][j+1])

  forensic = Forensic(allele_l, allele_r)

  per_homo_hetero = forensic.per_homo_hetero()

  r_locas.append(data[0][j])
  r_homo.append(per_homo_hetero[1])
  r_per_homo.append(per_homo_hetero[3])
  r_hetero.append(per_homo_hetero[2])
  r_per_hetero.append(per_homo_hetero[4])
  
  '''
  print '\n'
  print 'Locus: ', data[0][j]
  print '--------------------------'
  print '\n \t Summary'
  print '\t --------------------------'
  print '\t Total = ', per_homo_hetero[0]
  print '\t Homos = ', per_homo_hetero[1], '\t Percent = ', per_homo_hetero[3] 
  print '\t Heteros = ', per_homo_hetero[2], '\t Percent = ', per_homo_hetero[4]
  '''

  pat_stats = forensic.paternity_statistics()

  r_poe.append(pat_stats[0])
  r_tpi.append(pat_stats[1])
  '''

  print '\n \t Paternity Statistics'
  print '\t --------------------------'
  print '\t Power of exclusion = ', pat_stats[0]
  print '\t Typical paternity index = ', pat_stats[1]
  '''

  freq_calc = forensic.freq_calc()
  r_allele.append(freq_calc[1])
  '''
  
  print '\n \t Frequency Calculations'
  print '\t --------------------------'
  print '\t Total allele = ', freq_calc[0]
  print '\t Table for frequency '
  print '\t --------------------------'
  print '\n \t Allele \t Frequency \t Percent'
  '''
  '''
  for k in range(len(freq_calc[1])):
    print '\t',freq_calc[1][k], '\t', freq_calc[2][k], '\t', freq_calc[3][k]
  '''
'''
new_allele = [[1,2,3,4],[11,22,33,44]]
print new_allele
new_allele[0].pop(2)
print new_allele
'''
'''
for i in range(2, len(r_allele)):
  for k in range(len(r_allele[i])):
    for j in range(len(r_allele[i-1])):
      if r_allele[i-1][j] == r_allele[i][k]:
        r_allele[i].pop()
        print j, row
      
  print r_allele[i]
'''

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
  print r_locas[i], '    \t', r_homo[i], r_per_homo[i], '\t', r_hetero[i], r_per_hetero[i], '\t', r_poe[i], r_tpi[i]
