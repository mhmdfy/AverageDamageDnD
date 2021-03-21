from average5e import calculageAverage, d

def getSwordFighter():
  # Changes by level:
  # 01: AC 14, proficiency 2
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack
  # 06: ASI
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: Extra Attack
  # 13: AC 19, proficiency 5
  # 17: AC 20, proficiency 6, Extra Attack

  f01 = 1 * calculageAverage(14, 5, [(1, 8)], 5)
  f04 = 1 * calculageAverage(15, 6, [(1, 8)], 6)
  f05 = 2 * calculageAverage(16, 7, [(1, 8)], 6)
  f06 = 2 * calculageAverage(16, 8, [(1, 8)], 7)
  f08 = 2 * calculageAverage(17, 8, [(1, 8)], 7)
  f09 = 2 * calculageAverage(18, 9, [(1, 8)], 7)
  f11 = 3 * calculageAverage(18, 9, [(1, 8)], 7)
  f13 = 3 * calculageAverage(19, 10, [(1, 8)], 7)
  f17 = 4 * calculageAverage(20, 11, [(1, 8)], 7)

  f13a = 3 * calculageAverage(19, 11, [(1, 8)], 8)
  print('fighter: ' + str(f13a))

  return [f01, f01, f01, f04, f05, f06, f06, f08, f09, f09, f11, f11, f13, f13, f13, f13, f17, f17, f17, f17]


def getCrossbowFighter():
  # Changes by level:
  # 01: AC 14, Archery, proficiency 2
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack
  # 06: ASI
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: Extra Attack
  # 13: AC 19, proficiency 5
  # 17: AC 20, proficiency 6, Extra Attack

  f01 = 2 * calculageAverage(14, 7, [(1, 6)], 3)
  f03 = 2 * (calculageAverage(14, 7, [(1, 6)], 3) + 0.05 * d(1, 6))
  f04 = 2 * (calculageAverage(15, 2, [(1, 6)], 13) + 0.05 * d(1, 6))
  f05 = 3 * (calculageAverage(16, 3, [(1, 6)], 13) + 0.05 * d(1, 6))
  f06 = 3 * (calculageAverage(16, 4, [(1, 6)], 14) + 0.05 * d(1, 6))
  f08 = 3 * (calculageAverage(17, 5, [(1, 6)], 15) + 0.05 * d(1, 6))
  f09 = 3 * (calculageAverage(18, 6, [(1, 6)], 15) + 0.05 * d(1, 6))
  f11 = 4 * (calculageAverage(18, 6, [(1, 6)], 15) + 0.05 * d(1, 6))
  f13 = 4 * (calculageAverage(19, 7, [(1, 6)], 15) + 0.05 * d(1, 6))
  f15 = 4 * (calculageAverage(19, 7, [(1, 6)], 15) + 0.1 * d(1, 6))
  f17 = 5 * (calculageAverage(20, 8, [(1, 6)], 15) + 0.1 * d(1, 6))

  return [f01, f01, f03, f04, f05, f06, f06, f08, f09, f09, f11, f11, f13, f13, f15, f15, f17, f17, f17, f17]

def getGWMFighter():
  # Changes by level:
  # 01: AC 14, Archery, proficiency 2
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack
  # 06: ASI
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: Extra Attack
  # 13: AC 19, proficiency 5
  # 17: AC 20, proficiency 6, Extra Attack

  f01 = 1 * calculageAverage(14, 5, [(2, 6)], 3)
  f03 = 1 * (calculageAverage(14, 5, [(2, 6)], 3) + 0.05 * d(2, 6))
  f04 = 1 * (calculageAverage(15, 0, [(2, 6)], 13) + 0.05 * d(2, 6))
  f05 = 2 * (calculageAverage(16, 1, [(2, 6)], 13) + 0.05 * d(2, 6))
  f06 = 2 * (calculageAverage(16, 2, [(2, 6)], 14) + 0.05 * d(2, 6))
  f08 = 2 * (calculageAverage(17, 3, [(2, 6)], 15) + 0.05 * d(2, 6))
  f09 = 2 * (calculageAverage(18, 4, [(2, 6)], 15) + 0.05 * d(2, 6))
  f11 = 3 * (calculageAverage(18, 4, [(2, 6)], 15) + 0.05 * d(2, 6))
  f13 = 3 * (calculageAverage(19, 5, [(2, 6)], 15) + 0.05 * d(2, 6))
  f15 = 3 * (calculageAverage(19, 5, [(2, 6)], 15) + 0.1 * d(2, 6))
  f17 = 4 * (calculageAverage(20, 6, [(2, 6)], 15) + 0.1 * d(2, 6))

  return [f01, f01, f03, f04, f05, f06, f06, f08, f09, f09, f11, f11, f13, f13, f15, f15, f17, f17, f17, f17]