from __future__ import division
class GC_calculator:
  def read_input(self):
    self.dna_dict = {}
    f = open('rosalind.txt', 'r')
    for line in f :
      if ">" in line :
        name = line.split(">")[1].strip()
        dna = f.next().strip()
        line = f.next()
        while ">" not in line:
          dna += line.strip()
          line = f.next()
        self.dna_dict[name] = dna
    #print self.dna_dict
  def run_stuff(self):
    all_things = []
    for seq in self.dna_dict.keys():
      gc = self.G_count(self.dna_dict[seq])
      cc = self.C_count(self.dna_dict[seq])
      nc = self.Nuc_total_count(self.dna_dict[seq])
      gc_percent = self.GC_percent(gc,cc,nc)
      all_things.append({seq:gc_percent})
    #print all_things
    all_things = sorted(all_things, key = lambda i:i.values()[0])[::-1]
    print all_things
    self.all_things = all_things
  def G_count (self, dna):
    num_g = 0
    for G in dna:
      if G == "G":
        num_g += 1
    #print ("Guanine counter working!")
    return num_g
  def C_count (self, dna):
    num_c = 0
    for C in dna:
      if C == "C" :
        num_c += 1
    #print ("Cytosine counter working! There are {} cystosines" .format(num_c))
    return num_c
  def Nuc_total_count (self, dna):
    dna_length = len(dna)
    #print ("Nucleotide counter working!")
    return dna_length
  def GC_percent (self, num_g, num_c, length):
    #print(num_g, num_c, length)
    gc_percent = ((num_g + num_c)/length)*100
    return gc_percent
  def print_output(self):
    print("The %GC in this DNA sequence is {}" .format(self.gc_percent))
if __name__ == '__main__':
  g = GC_calculator()
  g.read_input()
  g.run_stuff()
