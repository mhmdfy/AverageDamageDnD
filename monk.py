from average5e import calculageAverage

def getWayOfHand():
  # Changes by level:
  # 01: AC 14, proficiency 2, Unarmed 1d4
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack, Unarmed 1d6
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: Unarmed 1d8
  # 12: ASI
  # 13: AC 19, proficiency 5
  # 16: ASI
  # 17: AC 20, proficiency 6, Unarmed 1d10

  m01 = calculageAverage(14, 5, [(1, 10)], 3) + calculageAverage(14, 5, [(1, 4)], 3)
  m04 = calculageAverage(15, 6, [(1, 10)], 4) + calculageAverage(15, 6, [(1, 4)], 4)
  m05 = 2 * calculageAverage(16, 7, [(1, 10)], 4) + calculageAverage(16, 7, [(1, 6)], 4)
  m08 = 2 * calculageAverage(17, 8, [(1, 10)], 5) + calculageAverage(17, 8, [(1, 6)], 5)
  m09 = 2 * calculageAverage(18, 9, [(1, 10)], 5) + calculageAverage(18, 9, [(1, 6)], 5)
  m11 = 2 * calculageAverage(18, 9, [(1, 10)], 5) + 2* calculageAverage(18, 9, [(1, 8)], 5)
  m13 = 2 * calculageAverage(19, 10, [(1, 10)], 5) + 2* calculageAverage(19, 10, [(1, 8)], 5)
  m17 = 2 * calculageAverage(20, 11, [(1, 10)], 5) + 2* calculageAverage(20, 11, [(1, 10)], 5)


  return [m01, m01, m01, m04, m05, m05, m05, m08, m09, m09, m11, m11, m13, m13, m13, m13, m17, m17, m17, m17]

def getWayOfMercy():
  # Changes by level:
  # 01: AC 14, proficiency 2, Unarmed 1d4
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra Attack, Unarmed 1d6
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: Unarmed 1d8
  # 12: ASI
  # 13: AC 19, proficiency 5
  # 16: ASI
  # 17: AC 20, proficiency 6, Unarmed 1d10

  m01 = calculageAverage(14, 5, [(1, 10)], 3) + calculageAverage(14, 5, [(1, 4)], 3)
  m04 = calculageAverage(15, 6, [(1, 10)], 4) + calculageAverage(15, 6, [(1, 4)], 4)
  m05 = 2 * calculageAverage(16, 7, [(1, 10)], 4) + calculageAverage(16, 7, [(1, 6)], 4)
  m08 = 2 * calculageAverage(17, 8, [(1, 10)], 5) + calculageAverage(17, 8, [(1, 6)], 5)
  m09 = 2 * calculageAverage(18, 9, [(1, 10)], 5) + calculageAverage(18, 9, [(1, 6)], 5)
  m11 = 2 * calculageAverage(18, 9, [(1, 10)], 5) + calculageAverage(18, 9, [(2, 8)], 8)
  m12 = 2 * calculageAverage(18, 9, [(1, 10)], 5) + calculageAverage(18, 9, [(2, 8)], 9)
  m13 = 2 * calculageAverage(19, 10, [(1, 10)], 5) + calculageAverage(19, 10, [(2, 8)], 9)
  m16 = 2 * calculageAverage(19, 10, [(1, 10)], 5) + calculageAverage(19, 10, [(2, 8)], 10)
  m17 = 2 * calculageAverage(20, 11, [(1, 10)], 5) + calculageAverage(20, 11, [(2, 10)], 10)


  return [m01, m01, m01, m04, m05, m05, m05, m08, m09, m09, m11, m12, m13, m13, m13, m16, m17, m17, m17, m17]