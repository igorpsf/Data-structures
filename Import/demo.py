import other_script as ot   # Import modult other_script
print(4)
print(ot.num)




import useful_functions as uf

scores = [88, 92, 79, 93, 85]

mean = uf.mean(scores)
curved = uf.add_five(scores)

mean_c = uf.mean(curved)

print("Scores:", scores)
print("Original Mean:", mean, " New Mean:", mean_c)




import math # https://docs.python.org/3/library/math.html

print(math.factorial(4))    # 4 * 3 * 2 * 1 = 24


#import os.path  # https://docs.python.org/3/library/os.path.html
#print("The current directory is %s" % os.path.curdir)   # The current directory is .
from os import path

print("The current directory is %s" % path.curdir)   # The current directory is .
print("abspath = %s" % path.abspath(path.curdir)) # abspath = /Users/ipostnikov/Documents/Git/Data Structures/Import
print("dirname = %s" % path.dirname(path.curdir)) # abspath = /Users/ipostnikov/Documents/Git/Data Structures/Import
print("basename = %s" % path.basename(path.curdir)) # abspath = /Users/ipostnikov/Documents/Git/Data Structures/Import


from random import *




###

# pip install pytz
# http://pytz.sourceforge.net/
from datetime import datetime
import pytz

utc = pytz.utc
ist = pytz.timezone("Asia/Kolkata")

now = datetime.now(tz=utc)
ist_now = now.astimezone(ist)

print(now)
print(ist_now)