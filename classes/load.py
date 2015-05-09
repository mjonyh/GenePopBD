'''
This class will be used to load the csv input file.
'''
import csv
class Load(object):
  '''
  A description of the class.

  :param fname: name of the input file.
  :type fname: string
  :return : 2D list as data[][]
  '''
  def __init__(self, file_name):
    self.fname = file_name

  def load(self):
    ''' load the file using std open'''
    f = open(self.fname,'r')

    data = []
    for line in f.readlines():
        data.append(line.replace('\n','').split(','))

    f.close()

    return data

  def down(self, result):
    with open("output.csv", "wb") as f:
      writer = csv.writer(f)
      writer.writerows(result)
    print 'csv output'
