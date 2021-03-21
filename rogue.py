from average5e import calculageAverage, calculageAverageAdvantage, hitChanceAdvantage, d


def getSwashbucklerRapier():
  # Changes by level:
  # 01: AC 14, proficiency 2, 1d6
  # 03: 2d6
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, 3d6
  # 07: 4d6
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4, 5d6
  # 11: 6d6
  # 13: AC 19, proficiency 5, 7d6
  # 15: 8d6
  # 17: AC 20, proficiency 6, 9d9
  # 19: 10d6

  r01 = calculageAverageAdvantage(14, 5, [(1, 8), (1, 6)], 3)
  r03 = calculageAverageAdvantage(14, 5, [(1, 8), (2, 6)], 3)
  r04 = calculageAverageAdvantage(15, 6, [(1, 8), (2, 6)], 4)
  r05 = calculageAverageAdvantage(16, 7, [(1, 8), (3, 6)], 4)
  r07 = calculageAverageAdvantage(16, 7, [(1, 8), (4, 6)], 4)
  r08 = calculageAverageAdvantage(17, 8, [(1, 8), (4, 6)], 5)
  r09 = calculageAverageAdvantage(18, 9, [(1, 8), (5, 6)], 5)
  r11 = calculageAverageAdvantage(18, 9, [(1, 8), (6, 6)], 5)
  r13 = calculageAverageAdvantage(19, 10, [(1, 8), (7, 6)], 5)
  r15 = calculageAverageAdvantage(19, 10, [(1, 8), (8, 6)], 5)
  r17 = calculageAverageAdvantage(20, 11, [(1, 8), (9, 6)], 5)
  r19 = calculageAverageAdvantage(20, 11, [(1, 8), (10, 6)], 5)

  return [r01, r01, r03, r04, r05, r05, r07, r08, r09, r09, r11, r11, r13, r13, r15, r15, r17, r17, r19, r19]

def calculateSneakAttackTWF(ac, prof, mod, sa):
  return calculageAverage(ac, prof, [(1, 6)], mod) + calculageAverage(ac, prof, [(1, 6)], 0) + hitChanceAdvantage(ac, prof) * d(sa, 6) + 0.098 * d(sa, 6)


def getSwashbucklerTWF():
  r01 = calculateSneakAttackTWF(14, 5, 3, 1)
  r03 = calculateSneakAttackTWF(14, 5, 3, 2)
  r04 = calculateSneakAttackTWF(15, 6, 4, 2)
  r05 = calculateSneakAttackTWF(16, 7, 4, 3)
  r07 = calculateSneakAttackTWF(16, 7, 4, 4)
  r08 = calculateSneakAttackTWF(17, 8, 5, 4)
  r09 = calculateSneakAttackTWF(18, 9, 5, 5)
  r11 = calculateSneakAttackTWF(18, 9, 5, 6)
  r13 = calculateSneakAttackTWF(19, 10, 5, 7)
  r15 = calculateSneakAttackTWF(19, 10, 5, 8)
  r17 = calculateSneakAttackTWF(20, 11, 5, 9)
  r19 = calculateSneakAttackTWF(20, 11, 5, 10)

  return [r01, r01, r03, r04, r05, r05, r07, r08, r09, r09, r11, r11, r13, r13, r15, r15, r17, r17, r19, r19]
