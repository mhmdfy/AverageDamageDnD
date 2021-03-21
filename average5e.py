from functools import reduce
import numpy as np
import matplotlib.pyplot as plt

def hitChance(ac, m):
  return (21 + m - ac)/20.0

def missChance(ac, m):
  return 1 - (21 + m - ac)/20.0


def hitChanceMultiDisadvantage(ac, m, t):
  # return pow(hitChance(ac, m), t)
  return pow(21 + m - ac, t)/pow(20, t)

def hitChanceDisadvantage(ac, m):
  # return hitChance(ac, m) * hitChance(ac, m)
  return hitChanceMultiDisadvantage(ac, m, 2)


def hitChanceMultiAdvantage(ac, m, t):
  # return 1 - pow(missChance(ac, m), t)
  return 1 - pow(ac - m - 1, t)/pow(20, t)

def hitChanceAdvantage(ac, m):
  return hitChanceMultiAdvantage(ac, m, 2)

def hitChanceElvenAdvantage(ac, m):
  return hitChanceMultiAdvantage(ac, m, 3)



def d(dice, faces):
  return dice * (sum(range(1, faces + 1)) / float(faces))

def dieWithAcc(acc, die):
  return d(die[0], die[1]) + acc

def dieList(dice):
  return reduce(dieWithAcc, dice, 0)


def calculageAverage(ac, proficiency, dice, bonus):
  # hitChance(14, 5) * (d(1, 10) + d(1, 6)) + 0.05 * (d(1,10) + d(1, 6))
  diceAverage = dieList(dice)
  return hitChance(ac, proficiency) * (diceAverage + bonus) + 0.05 * diceAverage

def calculageAverageMultiDisadvantage(ac, proficiency, dice, bonus, t):
  diceAverage = dieList(dice)
  return hitChanceMultiDisadvantage(ac, proficiency, t) * (diceAverage + bonus) + pow(0.05, t) * diceAverage

def calculageAverageDisadvantage(ac, proficiency, dice, bonus):
  return calculageAverageMultiDisadvantage(ac, proficiency, dice, bonus, 2)

def calculageAverageMultiAdvantage(ac, proficiency, dice, bonus, t):
  diceAverage = dieList(dice)
  return hitChanceMultiAdvantage(ac, proficiency, t) * (diceAverage + bonus) + (1 - pow(0.95, t)) * diceAverage

def calculageAverageAdvantage(ac, proficiency, dice, bonus):
  return calculageAverageMultiAdvantage(ac, proficiency, dice, bonus, 2)

def calculageAverageElvenAdvantage(ac, proficiency, dice, bonus):
  return calculageAverageMultiAdvantage(ac, proficiency, dice, bonus, 3)


def getBaseline():
  # Changes by level:
  # 01: AC 14, proficiency 2, cantrip scale 1
  # 02: mod added to eldrich
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, cantrip scale 2
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: cantrip scale 3
  # 13: AC 19, proficiency 5
  # 17: AC 20, proficiency 6, cantrip scale 4

  dice = [(1, 10), (1, 6)]

  w01 = 1 * calculageAverage(14, 5, dice, 0)
  w02 = 1 * calculageAverage(14, 5, dice, 3)
  w04 = 1 * calculageAverage(15, 6, dice, 4)
  w05 = 2 * calculageAverage(16, 7, dice, 4)
  w08 = 2 * calculageAverage(17, 8, dice, 5)
  w09 = 2 * calculageAverage(18, 9, dice, 5)
  w11 = 3 * calculageAverage(18, 9, dice, 5)
  w13 = 3 * calculageAverage(19, 10, dice, 5)
  w17 = 4 * calculageAverage(20, 11, dice, 5)

  return [w01, w02, w02, w04, w05, w05, w05, w08, w09, w09, w11, w11, w13, w13, w13, w13, w17, w17, w17, w17]

# Takes a list of tuples of (dprlist, lable, color)
def plotTo20(list):
  levels = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
  warlockDPR = np.array(getBaseline())
  

  plt.plot(levels, warlockDPR, color='r', label='baseline')
  for tuple in list:
    otherDPR = np.array(tuple[0])
    plt.plot(levels, otherDPR, color=tuple[2], label=tuple[1])
  plt.title("Average damage per Level")
  plt.xlabel("Levels")
  plt.ylabel("DPR")
  plt.legend()
  plt.show()

def plotTo10(list):
  levels = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
  warlockDPR = np.array(getBaseline()[:10])
  

  plt.plot(levels, warlockDPR, color='r', label='baseline')
  for tuple in list:
    otherDPR = np.array(tuple[0])
    plt.plot(levels, otherDPR[:10], color=tuple[2], label=tuple[1])
  plt.title("Average damage per Level")
  plt.xlabel("Levels")
  plt.ylabel("DPR")
  plt.legend()
  plt.show()
