'''
Created on Nov 21, 2012

@author: theja
'''
import sys
from numpy import *
import pdb

def helloworld_func():
  print "Hello World"
def mults_of_set_below(divisorset,limit):
  #returns all natural numbers below limit which are multiples of 
  #some element in the divisorset
  temp = divisorset
  for x in divisorset:
    temp = concatenate((arange(x,limit,x),temp))
  temp = unique(temp)
  return temp.sum()  

def prime(nr):
  for i in arange(int(math.sqrt(nr))+1,0,-1):
    if nr%i==0:
     largest_divisor = i
     break
  if largest_divisor == 1:
    return True
  else:
    return False
    
def large_palindrome_using_products(ul,ll):
  maxprod = 0
  for i in arange(ul,ll,-1):
    for j in arange(ul,ll,-1):
      if palindrome(i*j)==True:
      	if i*j > maxprod:
      	  maxprod = i*j
  return maxprod
    
def palindrome(nr):
  seq = []
  while nr != 0:
    seq.append(nr%10)
    nr = nr/10
  for i in arange(0,len(seq)/2):
    if seq[i] != seq[-1-i]:
      return False
  return True
  
def primes(n):
  # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
  """ Returns  a list of primes < n """
  sieve = [True] * n
  for i in xrange(3,int(n**0.5)+1,2):
    if sieve[i]:
      sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
  return [2] + [i for i in xrange(3,n,2) if sieve[i]]  

def find_rowwise_seq(grid,seqlength):
  maxprod = 1
  for i in arange(0,grid.shape[0]):
    for j in arange(0,grid.shape[1]-seqlength+1):
      prod = 1
      for k in arange(0,seqlength):
        prod = prod*grid[i,j+k]
      if prod > maxprod:
      	maxprod = prod
      	idx1 = i
      	idx2 = j
  print str(idx1)+' ' + str(idx2)
  return maxprod

def find_diag_seq(grid,seqlength):
  maxprod = 1
  for i in arange(0,grid.shape[0]-seqlength+1):
    for j in arange(0,grid.shape[1]-seqlength+1):
      prod = 1
      for k in arange(0,seqlength):
        prod = prod*grid[i+k,j+k]
      if prod > maxprod:
      	maxprod = prod
      	idx1 = i
      	idx2 = j
  print str(idx1)+' ' + str(idx2)
  return maxprod

def find_rdiag_seq(grid,seqlength):
  maxprod = 1
  for i in arange(0,grid.shape[0]-seqlength+1):
    for j in arange(seqlength-1,grid.shape[1]):
      prod = 1
      for k in arange(0,seqlength):
        prod = prod*grid[i+k,j-k]
      if prod > maxprod:
      	maxprod = prod
      	idx1 = i
      	idx2 = j
  print str(idx1)+' ' + str(idx2)
  return maxprod
  
def divisors_of_triangle_number_nw(n):
  nr = n*(n+1)/2
  if nr%n==1 and n%2==0: 
    print 'Case: n does not divide nr and is even'
    divs1 = divisors_of(n/2)
    divs2 = divisors_of(n+1)
  #if divids nr and is even: does not happen
  elif nr%n==0 and n%2==1: 
    print 'Case: if n divides nr and is odd'
    divs1 = divisors_of(n)
    divs2 = divisors_of((n+1)/2)
  else: 
    print 'Case: if n does not divide nr and is odd'
    divs1 = divisors_of(n)
    divs1.pop(-1)
    divs2 = divisors_of(n+1)
  divs3 = []
  for i in divs1:
    for j in divs2:
      temp = i*j
      if nr%temp == 0:
      	divs3.append(temp)
      #else:
      	#print str(temp)+' does not divide '+str(nr)
  #print divs1
  #print divs2
  print len(divs3)

def divisors_of(nr):
  divs = [1,nr]
  for i in arange(2,int((nr+1)/2)+1):
    if nr%i==0:
      divs.append(i)
  return sorted(divs)
  
def divisors_of_triangle_number(n):
  #all possible primes
  primedivs = []
  temp = primes(int(math.sqrt(n+1))+1)
  primedivs.extend(temp)
  if prime(n+1):
    primedivs.append(n+1)
  elif prime(n):
    primedivs.append(n)
  #valids prime factors
  divisors = []
  for i in primedivs:
    if n%i==0 or (n+1)%i==0:
      divisors.append(i)
  #print divisors
  
  #powers of prime factors
  power = {}
  for i in divisors:
    d = int(math.log(n+1,i))+1
    for j in arange(1,d):
      if n%(i**j)==0 or (n+1)%(i**j)==0:
      	power[i] = j
  count = 1;
  power[2] = power[2] - 1 #since nr = n*(n+1)/2
  print power

  for i in power.keys():
    count = count*(1+power[i])
  return count
  
def main(argv):
  #Prob 1
#  limit = 1000
#  divisorset = array([3,5])
#  print mults_of_set_below(divisorset,limit)
  
  #Prob 2
#  fm1 = 2
#  fm2 = 1
#  seq = array([fm2,fm1])
#  limit = 4000000
#  while fm1 <= limit:
#    f = fm1 + fm2
#    seq = concatenate((seq,array([f])))
#    fm2 = fm1
#    fm1 = f
#  seq = seq.compress((seq<=limit).flat)
#  print seq.compress((seq%2==0).flat).sum()  

  #Prob 3 #Answer: 6857. Took a long time.
#  nr = 600851475143
#  for i in arange(int(math.sqrt(nr))+1,0,-1):
#    if prime(i)==True:
#      if nr%i==0:
#      	break
#  print i  

  #prob 4: largest palindrome which is a prod of two 3 dig numbers
#  print large_palindrome_using_products(999,99)
  
  #Prob 5 : Hand calc
#  print 2*3*2*5*7*2*3*11*13*2*17*19
  
  #Prob 6: Hand calc
#  n = 100
#  print (n*(n+1)/2)*(n*(n+1)/2) - n*(n+1)*(2*n+1)/6

  #Prob 7: Kth prime number
  #Too Too long buggy solution.
#  limit = 10000*200
#  primes = [2,3,5,7,11,13,17,23,29,31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
#   79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 
#   163, 167, 173, 179, 181, 191, 193, 197, 199]
#  primecand = range(primes[-1],limit)
#  for i in primes:
#    primecand = [x for x in primecand if x not in range(i,limit,i)]
#  #pdb.set_trace()
#  i = primecand[0]
#  primes.append(i)
#  while i < limit and len(primecand)>0:
#    primecand = [x for x in primecand if x not in range(i,limit,i)]
#    if len(primecand)>0:
#      i = primecand[0]
#      primes.append(i)
#      primecand.pop(0)
#  if len(primes) > 10000:
#    print primes[10000]  
#  else:
#    print str(len(primes)) + ': Need to search over a bigger range'
  
  #primelist = primes(106000)
  #print(primelist[10000])
  
  '''  
  #Prob 8
  dig1000 = '73167176531330624919225119674426574742355349194934'+\
'96983520312774506326239578318016984801869478851843'+\
'85861560789112949495459501737958331952853208805511'+\
'12540698747158523863050715693290963295227443043557'+\
'66896648950445244523161731856403098711121722383113'+\
'62229893423380308135336276614282806444486645238749'+\
'30358907296290491560440772390713810515859307960866'+\
'70172427121883998797908792274921901699720888093776'+\
'65727333001053367881220235421809751254540594752243'+\
'52584907711670556013604839586446706324415722155397'+\
'53697817977846174064955149290862569321978468622482'+\
'83972241375657056057490261407972968652414535100474'+\
'82166370484403199890008895243450658541227588666881'+\
'16427171479924442928230863465674813919123162824586'+\
'17866458359124566529476545682848912883142607690042'+\
'24219022671055626321111109370544217506941658960408'+\
'07198403850962455444362981230987879927244284909188'+\
'84580156166097919133875499200524063689912560717606'+\
'05886116467109405077541002256983155200055935729725'+\
'71636269561882670428252483600823257530420752963450'
  seq = [int(x) for x in list(dig1000)]
  nconseq = 5
  maxprod = 1
  for i in arange(0,len(seq)-nconseq):
    prod  = 1
    for j in arange(0,5):
      prod  = prod*seq[i+j]
    if prod > maxprod:
      maxprod = prod
  print maxprod
  '''
  '''
  #Prob 9
  for a in arange(1,500):
    for b in arange(1,500):
      c = math.sqrt(a**2 + b**2)
      if c==around(c):
      	if a + b + c == 1000:
      	  print a,b,c
  '''
  
  #Prob 10
#  print array(primes(2000000)).sum()


  '''
  #Prob 11
  grid = ['08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08',
  '49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00',
  '81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65',
  '52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91',
  '22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80',
  '24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50',
  '32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70',
  '67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21',
  '24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72',
  '21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95',
  '78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92',
  '16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57',
  '86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58',
  '19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40',
  '04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66',
  '88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69',
  '04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36',
  '20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16',
  '20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54',
  '01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48']
  #grid = ['1 2 3 2','4 5 6 7','8 9 1 2','10 10 1 1']
  mat = empty((0,20))
  seqlength = 4
  for x in grid:
    temp = x.split(' ')
    temp = array([int(i) for i in temp])
    print temp
    mat = vstack((mat,temp.transpose()))


  maxprodrow = find_rowwise_seq(mat,seqlength)
  maxprodcol = find_rowwise_seq(mat.transpose(),seqlength)
  maxproddiag = find_diag_seq(mat,seqlength)
  maxprodrdiag = find_rdiag_seq(mat,seqlength)
  print maxprodrow
  print maxprodcol
  print maxproddiag
  print maxprodrdiag
  '''
  
  '''
  #Prob 12
  offset = 12375
  count = empty((0,1))
  for n in arange(offset,offset+1):
    count = vstack((count,divisors_of_triangle_number(n)))
  print count.argmax(0)+offset,count.max(0)
  #print count
  '''
  
  '''
  #Prob 21
  amicable = []
  for i in arange(2,10000):
    print i
    d1 = array(divisors_of(i))
    d1 = d1[:-1]
    j = d1.sum()
    if j==i:
      continue
    else:
      d2 = array(divisors_of(j))
      d2 = d2[:-1]
      if d2.sum()==i:
      	amicable.append([i,j])
  print amicable
  array([x[0] for x in amicable]).sum()
  '''
  
  #Prob22
  with open('data_prob22.txt','rb') as fin:
    dat = fin.read().split(',')
  
  dat = [x.replace('"','') for x in dat]
  dat.sort()
  val = 0L
  for j in arange(0,len(dat)):
    jval = 0
    for i in arange(0,len(dat[j])):
      jval = jval + ord(dat[j][i])-64 
    val = val + (j+1)*jval
  print val
  pdb.set_trace()
if __name__ == "__main__":
  main(sys.argv)
