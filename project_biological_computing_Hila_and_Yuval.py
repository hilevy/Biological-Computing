"""Project Biological Computition - Hila Levy (325694461) and Yuval Varsano () .ipynb"""



###################################################################################################################
# First, we built a class named "Compount" to represent any of the 9 compunts we have in the head of each column. #
# The compunt object consists of 4 fields: 2 activators (act1, act2) and 2 depressors (dep1, dep2).               #
###################################################################################################################

class Compount:
    
    # We applied the __init__ method in order to build objects of Compount.
    def __init__(self, act1 = False, act2 = False, dep1 = False, dep2 = False):
        self.act1 = act1
        self.act2 = act2
        self.dep1 = dep1
        self.dep2 = dep2

    # We have created the function "changes" in order to compare the changes between two compounts (how many changes were made, and whether its activator or depressor)
    # Input: 2 compunts (self, comp2)
    # Output: "flag" -1/0/1 that indicates the changes
    # We used "flag" as an indactor of the type of the change:
    # If flag is 0 - there were made less (0) or more (2,3,4) than one changes
    # If flag is 1 - it means one activator changed
    # If flag is (-1) - it means one depressor changed
    def changes(self, comp2):
        changes = 0
        flag = 0
        if self.act1 < comp2.act1:
            changes += 1
            flag = 1
        if self.act2 < comp2.act2:
            changes += 1
            flag = 1
        if self.dep1 < comp2.dep1:
            changes += 1
            flag = -1
        if self.dep2 < comp2.dep2:
            changes += 1
            flag = -1

        if changes == 1:
          return flag   #flag = 1 means activator, flag = -1 means depressor
        else:
          return 0

    # This function was made in order for us to check our code, it is printing the fileds of the compount.
    def __str__(self):
        return str(self.act1) + " " + str(self.act2) + " " + str(self.dep1) + " " + str(self.dep2)


#################################################################################################################################
# Then, we built a class named "RegulationCondition" that represent a row in the table.                                         #
# The RegulationCondition object consists of 2 fields:                                                                          #
# 1. compount array - which is constant for all the RegulationConditions and is an array if the 9 compunts in the table.        #
# 2. activation array - that shows whether that RegulationCondition is On/Off in a specific compount (correspond to the index). #
#################################################################################################################################

class RegulationCondition:
    
    # We applied the __init__ method in order to build objects of RegulationCondition.
    def __init__(self, activationArr):
      self.compountArr = [Compount(False, False, False, False), Compount(True, False, False, False), Compount(True, True, False, False), Compount(False, False, True, False), Compount(True, False, True, False), Compount(True, True, True, False), Compount(False, False, True, True), Compount(True, False, True, True), Compount(True, True, True, True)]
      self.activationArr = activationArr

    # In order to check whether a regulation condition is monotonic or not, we created this function
    # Input: regulation condition (self)
    # Output: True/False
    # The function goes through all the possible transitions (for loop in for loop), and checks whether there exist a transition that is not monotonic.
    def monotonic_regulation_condition_list(self):
      monotonic_flag = True
      for firstIndex in range(len(self.compountArr)):
        for secondIndex in range(len(self.compountArr)):
          firstComp = self.compountArr[firstIndex]
          secondComp = self.compountArr[secondIndex]
          if firstComp.changes(secondComp) == 1:
            if not ((self.activationArr[firstIndex] == self.activationArr[secondIndex]) or (self.activationArr[firstIndex] == 0 and self.activationArr[secondIndex] == 1)):
              #this is not monotonic - we added activator but the activation turned off
              return False
          if firstComp.changes(secondComp) == -1:
            if not ((self.activationArr[firstIndex] == self.activationArr[secondIndex]) or (self.activationArr[firstIndex] == 1 and self.activationArr[secondIndex] == 0)):
              #this is not monotonic - we added depressor but the activation turned on
              return False
      return True

    # This function prints the position list of a regulation condition (a row in the table).
    def __str__(self):
      return str(self.activationArr)


# This function creats all the possible regulation conditions (there are 512).
def creates_all_rc():
  rc_list = []
  for a in range(2):
    for b in range(2):
      for c in range(2):
        for d in range(2):
          for e in range(2):
            for f in range(2):
              for g in range(2):
                for h in range(2):
                  for i in range(2):
                    if not(a==b==c==d==e==f==g==h==i==0 or a==b==c==d==e==f==g==h==i==1):
                      rc = RegulationCondition([a,b,c,d,e,f,g,h,i])
                      rc_list.append(rc)
  return rc_list

def main():
  rc_list = creates_all_rc()
  monotonic_list = []
  for rc in rc_list:
    if rc.monotonic_regulation_condition_list() == True:
      monotonic_list.append(rc)
  print("This is amount of monotonic regulation conditinos: ", len(monotonic_list))
  for i in range(len(monotonic_list)):
    print(monotonic_list[i])

if __name__ == "__main__":
  main()