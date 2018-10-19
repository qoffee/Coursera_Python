"""
Ваша цель напечатать на экран лесенку используя символы пробела " " и решетки "#". 
Например, для входного параметра (количества ступенек) 4 лесенка должна выглядеть следующим образом:
   #
  ##
 ###
####
"""

import sys
num_steps = int(sys.argv[1])
a = 0
while num_steps - a:
    print(" " * (num_steps - a + 1) + "#" * (a + 1))
    a += 1
