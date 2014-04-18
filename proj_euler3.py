import pdb
import sys
from numpy import *

def primes(n):
  # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]

def len_cseq(nr):
  if nr==1:
    return 1
  elif nr%2==0:
    return 1 + len_cseq(nr/2)
  else:
    return 1 + len_cseq(3*nr+1)
    
def Binomial(n,k):
  if n > k:
    return math.factorial(n) / (math.factorial(k)*math.factorial(n-k))
  elif n == k:
    return 1
        
def maxval_tree(dat):
  if len(dat)==1:
    return int(dat[0][0])
  else:
    return int(dat[0][0]) + max(maxval_tree(gentree(dat,'left')),
                             maxval_tree(gentree(dat,'right')))
def gentree(dat,side):
  datnew = []
  if side=='left':
    for i in arange(1,len(dat)):
     datnew.append(dat[i][:-1])
  else:
    for i in arange(1,len(dat)):
     datnew.append(dat[i][1:])
  return datnew

def divisors_of(nr):
  divs = [1,nr]
  for i in arange(2,int((nr+1)/2)+1):
    if nr%i==0:
      divs.append(i)
  return sorted(divs)

def sum_prop_div(nr):
  return sum(divisors_of(nr))-nr
  
def p21():
  '''
  21
  Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
  If d(a) = b and d(b) = a, where a neq b, then a and b are an amicable pair and each of a and b are called amicable numbers.

  For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

  Evaluate the sum of all the amicable numbers under 10000.
  '''    
  amicable = []
  dn = [0]
  max_nr = 10000
  for i in range(1,max_nr):
    dn.append(sum_prop_div(i))
  # properint len(dn)
  for i in range(1,max_nr):
    if i==dn[i]:
      continue
    if dn[i]< max_nr and dn[dn[i]]==i:
      amicable.append(i)
      amicable.append(dn[i])

  print sum(list(set(amicable))) #31626

def p22():
  '''
  Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

  For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 * 53 = 49714.

  What is the total of all the name scores in the file?
  '''
  abc='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  alphadict = {x:e+1 for e,x in enumerate(abc)}
  print alphadict 
  with open('names.txt','rb') as fin:
    names = fin.read().split(',')
    names = sort([x.strip("\"") for x in names])
  print names
  total = 0
  for e,x in enumerate(names):
    total += (e+1)*sum([alphadict[y] for y in x])
  print total

def main():
  # p21()
  p22()
  # pdb.set_trace()
  
if __name__=="__main__":
  main()

