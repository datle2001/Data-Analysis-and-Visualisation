import csv
import sys
import statistics
import matplotlib.pyplot as plt
import matplotlib.pyplot as bar

total_character = 0
total_appearance = 0
appearance = []
first_appearance = {}

def countWomen(reader):
  global total_character
  wmen = 0
  for line in reader:
    if 'female' in line[7].lower():
      wmen+=1
    total_character += 1
  print('There are', wmen, 'women characters, accounting for ' + roundup(wmen/total_character*100) + '% of all the characters.\n')

def countWmenAppearance(reader):
  wmen_app = 0
  global total_appearance
  global appearance
  
  for line in reader:
    try:
      num = int(line[10])
    except ValueError:
      continue
    if 'female' in line[7].lower():
      wmen_app += num
    total_appearance += num
    appearance.append(num) 
  
  appearance.sort()
  print('There are', wmen_app, 'appearances by women characters, accounting for ' + roundup(wmen_app/total_appearance*100) + '% of all the appearances.\n')
    
def countGSM(reader):
  global total_character
  gsm = 0
  
  for line in reader:
    if line[8] != '':
      gsm+=1
  print('There are', gsm, 'GSM characters, accounting for ' + roundup(gsm/total_character*100) + '% of all the characters.\n')

def oldestCharacter(reader):
  oldest = ''
  old = 2021
  global first_appearance
  
  for line in reader:
    try:
      num = int(line[12])
    except ValueError:
      continue
    
    if num<old:
      old = num
      oldest = line[1]
    elif num == old:
      oldest += ', ' + line[1]
      
    if num in first_appearance:
      first_appearance[num]+=1
    else:
      first_appearance.update({num:1})
      
  print('The oldest character(s) is(are) ' + oldest + '.\n')

def mostAppearance(reader):
  most_app = ''
  app = 0
  for line in reader:
    try:
      num = int(line[10])
    except ValueError:
      num = 0
    if num>app:
      app = num
      most_app = line[1]
    elif num == app:
      most_app += ', ' + line[1]
  print('The character with the most appearances is ' + most_app + '.\n')

def roundup(num):
  return str("%.2f" % num)

def calculateApp():
  global appearance
  
  median_app = statistics.median(appearance)
  mode_app = statistics.mode(appearance)
  stde = statistics.stdev(appearance)
  print('The mean of the number of appearances of all characters is ' + roundup(total_appearance/total_character) + '.\n')
  print('The mode of the number of appearances of all characters is ' + roundup(mode_app) + '.\n') 
  print('The median of the number of appearances of all characters is ' + roundup(median_app) + '.\n') 
  print('The standard deviation of the number of appearances of all characters is ' + roundup(stde) + '.\n') 

def plotFirstApp():

  years = []
  nums = []
  
  for year in first_appearance.keys():
    years.append(year)
  years.sort()
  for year in years:
    nums.append( first_appearance[year] )
  
  plt.plot(years, nums)
  plt.title('Number of first appearance by year', fontsize = 20)
  plt.xlabel('Year', fontsize = 16)
  plt.ylabel('Number of first appearance', fontsize = 16)
  plt.show()

def plotAlignment(reader):
  alignment = ['Good', 'Bad', 'Neutral']
  count = [0,0,0]
  
  for line in reader:
    string = line[4].lower()
    if 'good' in string:
      count[0]+=1
    elif 'bad' in string:
      count[1]+=1
    elif 'neutral' in string:
      count[2]+=1
    else:
      continue
  
  bar.bar(alignment, count, color = ['yellow', 'blue', 'grey'] )
  bar.xlabel('Alignment', fontsize =16)
  bar.ylabel('Number of characters', fontsize = 16)
  bar.title('Alignment bar graph', fontsize = 20)
  bar.show()
          
print('Enter a filename:')
filename = input()

try:
  file = open(filename)
except FileNotFoundError:
  print('No file found')
  sys.exit()

reader = csv.reader(file)
next(reader)
countWomen(reader)

file.seek(0)
next(reader)
countWmenAppearance(reader)

file.seek(0)
next(reader)
countGSM(reader)

file.seek(0)
next(reader)
oldestCharacter(reader)

file.seek(0)
next(reader)
mostAppearance(reader)

file.seek(0)
next(reader)
calculateApp()

plotFirstApp()

file.seek(0)
next(reader)
plotAlignment(reader)


  

  

  
