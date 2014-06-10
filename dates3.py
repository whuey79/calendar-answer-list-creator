# Will Huey
# Calendar answer list builder

import datetime
from sys import exit
from Tkinter import Tk
  
def getValidInt(text, min, max):
  check = 'n'
  while check == 'n':
    val = raw_input("Enter the " + str(text) + " (" + str(min) + "," + str(max) + ")" + " : ")
    if len(val) > 0:
      if int(val) >= min and int(val) <= max:
        check = 'y'
    
    if check == 'n':
      print ("Input is invalid.  Please try again.")

  return int(val)
  
def getValidIntYear(text, min, max):
  check = 'n'
  while check == 'n':
    val = raw_input("Enter the " + str(text) + " : ")
    if len(val) > 0:
    
      if int(val) < 100:
        val = '20' + val;
    

      if int(val) >= min and int(val) <= max:
        check = 'y'
    
    if check == 'n':
      print ("Input is invalid.  Please try again.")

  print "Year set: " + val
  return int(val)

  
def getdt(year):
  """ Builds date header """

  
  check = 'n'
  
  while check == 'n':
    mon = getValidInt('MONTH',1,12)
    date = getValidInt('DAY',1,31)
    
    dt = datetime.date( year, mon, date );
    str = dt.strftime('%A') + ', ' + dt.strftime('%m') + '/' + dt.strftime('%d')
    print " "
    print "Date entered: " + str
    check = raw_input("Is this correct - Yes(Default)/No ?").lower()
    print " "
  
  return str

def getHourMod(timeslot):
  """ func to sort by first 2 digits if valid, otherwise first char """
  
  hour = timeslot.split(':')
  try:
    hour = int(hour[0])%12
    # this uses mod to account for 12am coming before 1am
  except:  
    hour = hour[0]
  return hour

def getHour(timeslot):
  """ func to sort by first 2 digits if valid, otherwise first char """
  
  hour = timeslot.split(':')
  try:
    hour = int(hour[0])
  except:  
    hour = hour[0]
  return hour
    
def buildCalTimes():
  """ Builds dates """

  check = 'n';
  aslot = [];
  pslot = [];
  ampm = '';
    
  while check == 'n':
    ampm = 'AM'
    slot = 'y';
    aslot[:] = []
    pslot[:] = []

    while len(slot) > 0:
      slot = raw_input("AM:  Enter timeslot ie. 100, 6, 1230 - (Press enter to pass): ")
    
      if len(slot) > 2:
        aslot.append(slot[:-2] + ':' + slot[-2:] + ' ' + ampm)
      elif len(slot) > 0 and len(slot) <= 2 :
        aslot.append(slot + ':00' + ' ' + ampm)
    
    aslot = sorted(aslot,key=getHourMod)    
    print " "
    
    ampm = 'PM'
    slot = 'y'
    
    while len(slot) > 0:
      slot = raw_input("PM:  Enter timeslot ie. 100, 6, 1230 - (Press enter to pass): ")
    
      if len(slot) > 2:
        pslot.append(slot[:-2] + ':' + slot[-2:] + ' ' + ampm)
      elif len(slot) > 0 and len(slot) <= 2 :
        pslot.append(slot + ':00' + ' ' + ampm)   
    
    pslot = sorted(pslot,key=getHourMod)

    lslot = aslot + pslot

    print "Times entered: ", lslot

    print " "
    check = raw_input("Is this correct - Yes(Default)/No ?").lower()
    print " "
    
  return lslot  
  
def main():
  aList = []
  check = 'y'
  clipOut = ""

  print ""  
  print "***************************"
  print "*  Calendar List Builder  *"
  print "*  Updated:  09/13/2013   *"
  print "***************************"

#  year = getValidIntYear('CALENDAR YEAR (ie. 2013-2015,13)', 2013 , 2015)
  dat = datetime.datetime.now()
  year = int( dat.strftime('%Y') )
  print "Today: ", dat.strftime('%A, %m/%d/%Y')
 
  while check == 'y':
    print ""
    print "[ Group Header ]"

    dt = getdt(year)
    #print dt
    header = dt + ", Eastern Time"
    #print "Group header:  ", header

    print "[ Time Slots ]"
    openTimes = buildCalTimes()

    aList.append(header)
    
    for each in openTimes:
      aList.append(dt + ', ' + each)

    check = raw_input("Is there another date to add - Yes/No(Default) ?")
    if check == 'y':
      aList.append("")

  print ""
  print "[ Return List ]"  
  print ""
  
  for each in aList:
   print each

  clipOut = '\n'.join(aList)

  print ""

  # Clipboard stuff

  r = Tk() 
  r.withdraw()
  r.clipboard_clear()
  r.clipboard_append(clipOut) 
  
  print "List copied to clipboard.  Press enter to quit."
  check = raw_input("")
  r.destroy()
 
  exit(0)
  
if __name__ == '__main__':
  main()
