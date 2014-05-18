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
  
  
def main():
  '''
  #Prob 13
  with open('data_prob13.txt','rb') as fin:
    dat  = fin.read().split('\n')
    dat.pop(-1)
    dat = array([int(x.strip()) for x in dat])
  
  print dat.sum()
  '''
  '''
  #Prob 14
  start = 1000000
  maxlennr = 1000
  maxlen = 1
  for i in arange(start,1,-1):
    leni = len_cseq(i)
    if leni > maxlen:
      maxlennr = i
      maxlen = leni
  print maxlennr,maxlen
  pdb.set_trace()
  '''
  #Prob 15
#  print Binomial(40,20)
  '''
  #Prob 16
  temp = 2**1000
  dig = []
  while temp!=0:
    dig.append(temp%10)
    temp = temp/10
  print array(dig).sum()
  '''
  '''
  #Prob 17
  n2w = {}
  vals00t19 = [0,3,3,5,4,4,3,5,5,4,3,
               6,6,8,8,7,7,9,8,8]
  keys00t19 = ['','one','two','three','four','five','six','seven','eight',
              'nine','ten','eleven','twelve','thirteen','fourteen','fifteen',
               'sixteen','seventeen','eighteen','nineteen']
  vals00t90 = [0,0,6,6,5,5,5,7,6,6]
  keys00t90 = ['','ten','twenty','thirty','forty','fifty',
                'sixty','seventy','eighty','ninety']
  ones = {}
  tenths = {}
  onesW = {}
  tenthsW = {}
  for i in arange(0,20):
    ones[i] = vals00t19[i]
    onesW[i] = keys00t19[i]
  for i in arange(0,10,1):
    tenths[i] = vals00t90[i]
    tenthsW[i] = keys00t90[i]    

  count = []
  countW = []
  for i in arange(1,100):
    if i%100 > 19:
      count.append(tenths[(i/10)%10]+ones[i%10])
      countW.append(tenthsW[(i/10)%10]+onesW[i%10])
    else:
      count.append(ones[i%100])
      countW.append(onesW[i%100])
  for i in arange(100,1000):  
    if i%100 > 19:
      count.append(ones[i%10] + tenths[(i/10)%10] + ones[(i/100)%10] \
              + len('hundredand'))
      countW.append(onesW[(i/100)%10] \
              + 'hundredand' + tenthsW[(i/10)%10] + onesW[i%10])
    else:
      count.append(ones[i%100] + ones[(i/100)%10] \
              + len('hundredand'))
      countW.append(onesW[(i/100)%10] \
              + 'hundredand' + onesW[i%100])
  count.append(len('onethousand'))
  countW.append('Onethousand')
  
  count = array(count)
  count2 = array([len(i) for i in countW])
  print count.sum() - 9*3 #to remove and after onehundred, twohundred,...
  '''
  
  
  #Prob 17
#  with open('data_prob17.txt','rb') as fin:
#    dat = fin.read().split('\n')
#    dat.pop(-1)
#    dat = [x.split(' ') for x in dat]
  '''
  dat = [['3'],
    ['7','4'],
    ['2','4','6'],
    ['8','5','9','3']]
    
  print 'Fwd search'
  maxpath = []  
  maxpath.append(int(dat[0][0]));
  idx = 0
  print idx+1,maxpath[0]
  for i in arange(1,len(dat)):
    temp = array([int(x) for x in dat[i]])
    temp = temp[idx:idx+2]
    val,idxadd = temp.max(0),temp.argmax(0)
    idx = idx+idxadd
    maxpath.append(val)
    print idx+1,val
  maxpathF = array(maxpath)
  
  print 'Rev search'
  maxpath = []  
  idx = -1
  for i in arange(len(dat)-1,-1,-1):
    temp = array([int(x) for x in dat[i]])
    if idx==-1:
      val,idx = temp.max(0),temp.argmax(0)
      maxpath.append(val)
    elif idx==0:
      val = temp[0]
      maxpath.append(val)
    else:
      temp = concatenate((temp,array([0])))
      temp = temp[idx-1:idx+1]
      val,idxadd = temp.max(0),temp.argmax(0)
      idx = idx - (1- idxadd)
      maxpath.append(val)
    print idx+1,val
  maxpathR = array(maxpath)
  '''
#  print maxval_tree(dat)
  
  '''
  #Prob 67. Does not work! Too long.
  with open('data_prob67.txt','rb') as fin:
    dat = fin.read().split('\n')
    dat.pop(-1)
    dat = [x.split(' ') for x in dat]
  print maxval_tree(dat)
  '''
  
  '''
  #Prob 18
  wkdaydict = {0:'mon',1:'tue',2:'wed',3:'thur',4:'fri',5:'sat',6:'sun'}
  monthsNL = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  monthsL = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
  startyr = 1900
  endyr = 2000
  lyears = {}
  for i in arange(startyr,endyr+1):
    if (i%4==0 and i%100!=0) or i%400==0:
      lyears[i] = True
    else:
      lyears[i] = False
  day = {}
  wkday = 0
  for k1 in arange(startyr,endyr+1): #each year
    for k2 in arange(1,12+1): #each of the 12 months
      if lyears[k1]==False:
      	for k3 in arange(1,monthsNL[k2]+1):
      	  day[k1*10000+k2*100+k3] = wkdaydict[wkday]
      	  wkday = (wkday+1)%7
      else:
	for k3 in arange(1,monthsL[k2]+1):
      	  day[k1*10000+k2*100+k3] = wkdaydict[wkday]
      	  wkday = (wkday+1)%7
  count = 0
  collecteddays = []
  for i,j in day.items():
    if i%100==1 and j=='sun' and (i/10000)!=1900:
      #print i
      collecteddays.append(i)
      count = count+1
  collecteddays.sort()
  print collecteddays
  print count
  '''  
  '''
  #Prob 20
  nr = math.factorial(100)
  dig = []
  while nr!=0:
    dig.append(nr%10)
    nr =nr/10
  dig = array(dig)
  print dig.sum()
  '''
  

  
  
  pdb.set_trace()
  
if __name__=="__main__":
  main()

