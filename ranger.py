from average5e import calculageAverage, calculageAverageAdvantage, calculageAverageElvenAdvantage, calculageAverageMultiAdvantage

def getSwarmRangerHuntersMark():
  # Changes by level:
  # 01: AC 14, proficiency 2,
  # 02: Archery
  # 03: swarm (1d6)
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra attack
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4
  # 11: swarm (1d8)
  # 13: AC 19, proficiency 5
  # 17: AC 20, proficiency 6
  # 20: Foe Slayer

  r01 = calculageAverage(14, 5, [(1, 8), (1, 6)], 3)
  r02 = calculageAverage(14, 7, [(1, 8), (1, 6)], 3)
  r03 = calculageAverage(14, 7, [(1, 8), (2, 6)], 3)
  r04 = calculageAverage(15, 2, [(1, 8), (2, 6)], 13)
  r05 = 2 * calculageAverage(16, 3, [(1, 8), (1, 6)], 13) + calculageAverageAdvantage(16, 3, [(1, 6)], 0)
  r08 = 2 * calculageAverage(17, 4, [(1, 8), (1, 6)], 14) + calculageAverageAdvantage(17, 4, [(1, 6)], 0)
  r09 = 2 * calculageAverage(18, 5, [(1, 8), (1, 6)], 14) + calculageAverageAdvantage(18, 5, [(1, 6)], 0)
  r11 = 2 * calculageAverage(18, 5, [(1, 8), (1, 6)], 14) + calculageAverageAdvantage(18, 5, [(1, 8)], 0)
  r12 = 2 * calculageAverage(18, 6, [(1, 8), (1, 6)], 15) + calculageAverageAdvantage(18, 6, [(1, 8)], 0)
  r13 = 2 * calculageAverage(19, 7, [(1, 8), (1, 6)], 15) + calculageAverageAdvantage(19, 7, [(1, 8)], 0)
  r17 = 2 * calculageAverage(20, 8, [(1, 8), (1, 6)], 15) + calculageAverageAdvantage(20, 8, [(1, 8)], 0)
  r20 = 2 * calculageAverage(20, 8, [(1, 8), (1, 6)], 15) + calculageAverageAdvantage(20, 13, [(1, 8)], 5)

  return [r01, r02, r03, r04, r05, r05, r05, r08, r09, r09, r11, r11, r13, r13, r13, r13, r17, r17, r17, r20]

def getSwarmRangerCrossbow():
  # Changes by level:
  # 01: AC 14, proficiency 2, favored (1d4)
  # 02: Archery
  # 03: swarm (1d6)
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra attack
  # 06: favored 1d6

  # 07: Summon Beast
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4

  # 11: swarm (1d8), Conjure Animals (2 wolves)
  # 12 : ASI
  # 13: AC 19, proficiency 5

  # 15: Guardian Nature
  # 17: AC 20, proficiency 6

  # 19: Conjure Animals (4 wolves)

  r01 = 2 * calculageAverage(14, 5, [(1, 6)], 3) + calculageAverageAdvantage(14, 5, [(1, 4)], 0)
  r02 = 2 * calculageAverage(14, 7, [(1, 6)], 3) + calculageAverageAdvantage(14, 7, [(1, 4)], 0)
  r03 = 2 * calculageAverage(14, 7, [(1, 6)], 3) + calculageAverageAdvantage(14, 7, [(1, 4), (1, 6)], 0)
  r04 = 2 * calculageAverage(15, 2, [(1, 6)], 13) + calculageAverageAdvantage(15, 2, [(1, 4), (1, 6)], 0)
  r05 = 3 * calculageAverage(16, 3, [(1, 6)], 13) + calculageAverageElvenAdvantage(16, 3, [(1, 4), (1, 6)], 0)
  r06 = 3 * calculageAverage(16, 3, [(1, 6)], 13) + calculageAverageElvenAdvantage(16, 3, [(2, 6)], 0)

  r07 = 3 * calculageAverage(16, 3, [(1, 6)], 13) + calculageAverageElvenAdvantage(16, 3, [(1, 6)], 0) + calculageAverage(16, 6, [(1, 8)], 6)
  r08 = 3 * calculageAverage(17, 4, [(1, 6)], 14) + calculageAverageElvenAdvantage(17, 4, [(1, 6)], 0) + calculageAverage(17, 6, [(1, 8)], 6)
  r09 = 3 * calculageAverage(18, 5, [(1, 6)], 14) + calculageAverageElvenAdvantage(18, 5, [(1, 6)], 0) + calculageAverage(18, 7, [(1, 8)], 7)

  r11 = 3 * calculageAverage(18, 5, [(1, 6)], 14) + calculageAverageElvenAdvantage(18, 5, [(1, 8)], 0) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r12 = 3 * calculageAverage(18, 6, [(1, 6)], 15) + calculageAverageElvenAdvantage(18, 6, [(1, 8)], 0) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r13 = 3 * calculageAverage(19, 7, [(1, 6)], 15) + calculageAverageElvenAdvantage(19, 7, [(1, 8)], 0) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)

  r15 = 3 * calculageAverageAdvantage(19, 7, [(1, 6)], 15) + calculageAverageMultiAdvantage(19, 7, [(1, 8)], 0, 6)
  r17 = 3 * calculageAverageAdvantage(20, 8, [(1, 6)], 15) + calculageAverageMultiAdvantage(20, 8, [(1, 8)], 0, 6)

  r19 = 3 * calculageAverage(20, 8, [(1, 6)], 15) + calculageAverageElvenAdvantage(20, 8, [(1, 8)], 0) + 4 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)


  return [r01, r02, r03, r04, r05, r06, r07, r08, r09, r09, r11, r12, r13, r13, r15, r15, r17, r17, r19, r19]


def getHorizonRangerStr():
  # Changes by level:
  # 01: AC 14, proficiency 2, Favored (1d4)
  # 02: Hunter's Mark
  # 03: Planar (1d8)
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra attack
  # 06: favored 1d6

  # 07: Summon Beast
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4

  # 11: Planar (2d8), Conjure Animals (2 wolves), Distance Strike
  # 12 : ASI
  # 13: AC 19, proficiency 5

  # 15: Guardian Nature
  # 17: AC 20, proficiency 6

  # 19: Conjure Animals (4 wolves)

  r01 = calculageAverage(14, 5, [(1, 12), (1, 4)], 3)
  r02 = calculageAverage(14, 5, [(1, 12), (1, 6)], 3)
  r03 = calculageAverage(14, 5, [(1, 12), (1, 4), (1, 8)], 3)
  r04 = calculageAverage(15, 0, [(1, 12), (1, 4), (1, 8)], 13)
  r05 = 2 * calculageAverage(16, 1, [(1, 12)], 13) + calculageAverageAdvantage(16, 1, [(1, 4), (1, 8)], 0)
  r06 = 2 * calculageAverage(16, 1, [(1, 12)], 13) + calculageAverageAdvantage(16, 1, [(1, 6), (1, 8)], 0)

  r07 = 2 * calculageAverage(16, 1, [(1, 12)], 13) + calculageAverageAdvantage(16, 1, [(1, 8)], 0) + calculageAverage(16, 6, [(1, 8)], 6)
  r08 = 2 * calculageAverage(17, 2, [(1, 12)], 14) + calculageAverageAdvantage(17, 2, [(1, 8)], 0) + calculageAverage(17, 6, [(1, 8)], 6)
  r09 = 2 * calculageAverage(18, 3, [(1, 12)], 14) + calculageAverageAdvantage(18, 3, [(1, 8)], 0) + calculageAverage(18, 7, [(1, 8)], 7)

  r11 = 3 * calculageAverage(18, 3, [(1, 12)], 14) + calculageAverageMultiAdvantage(18, 5, [(2, 8)], 0, 3) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r12 = 3 * calculageAverage(18, 4, [(1, 12)], 15) + calculageAverageMultiAdvantage(18, 6, [(2, 8)], 0, 3) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r13 = 3 * calculageAverage(19, 5, [(1, 12)], 15) + calculageAverageMultiAdvantage(19, 7, [(2, 8)], 0, 3) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)

  r15 = 3 * calculageAverageAdvantage(19, 5, [(1, 12), (1, 6)], 15) + calculageAverageMultiAdvantage(19, 7, [(2, 8)], 0, 6)
  r17 = 3 * calculageAverageAdvantage(20, 6, [(1, 12), (1, 6)], 15) + calculageAverageMultiAdvantage(20, 8, [(2, 8)], 0, 6)

  r19 = 3 * calculageAverage(20, 6, [(1, 12)], 15) + calculageAverageMultiAdvantage(20, 8, [(2, 8)], 0, 3) + 4 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)


  return [r01, r02, r03, r04, r05, r06, r07, r08, r09, r09, r11, r12, r13, r13, r15, r15, r17, r17, r19, r19]

def getBeastRanger():
  # Changes by level:
  # 01: AC 14, proficiency 2, Favored (1d4)
  # 02: Archery
  # 03: Pimal Companion 1d8 + 1d6 + 2 + PB (wisdom to hit)
  # 04: AC 15, ASI
  # 05: AC 16, proficiency 3, Extra attack
  # 06: favored 1d6

  # 07: Summon Beast
  # 08: AC 17, ASI
  # 09: AC 18, proficiency 4

  # 11: Beast Extra Attack, Conjure Animals (2 wolves)
  # 12 : ASI
  # 13: AC 19, proficiency 5

  # 15: Guardian Nature, Share Spells
  # 16: ASI
  # 17: AC 20, proficiency 6

  # 19: ASI, Conjure Animals (4 wolves)

  r01 = calculageAverage(14, 5, [(1, 8), (1, 4)], 3)
  r02 = calculageAverage(14, 7, [(1, 8), (1, 6)], 3)
  r03 = calculageAverage(14, 7, [(1, 8), (1, 4)], 3) + calculageAverage(14, 5, [(1, 8), (1, 6)], 4)
  r04 = calculageAverage(15, 2, [(1, 8), (1, 4)], 13) + calculageAverage(15, 5, [(1, 8), (1, 6)], 4)

  r05 = 2 * calculageAverage(16, 3, [(1, 8)], 13) + calculageAverageAdvantage(16, 3, [(1, 4)], 0) + calculageAverage(16, 6, [(1, 8), (1, 6)], 5)
  r06 = 2 * calculageAverage(16, 3, [(1, 8)], 13) + calculageAverageAdvantage(16, 3, [(1, 6)], 0) + calculageAverage(16, 6, [(1, 8), (1, 6)], 5)

  r07 = 2 * calculageAverage(16, 3, [(1, 8)], 13) + calculageAverage(16, 6, [(1, 8), (1, 6)], 5) + calculageAverage(16, 6, [(1, 8)], 6)
  r08 = 2 * calculageAverage(17, 4, [(1, 8)], 14) + calculageAverage(17, 6, [(1, 8), (1, 6)], 5) + calculageAverage(17, 6, [(1, 8)], 6)
  r09 = 2 * calculageAverage(18, 5, [(1, 8)], 14) + calculageAverage(18, 7, [(1, 8), (1, 6)], 6) + calculageAverage(18, 7, [(1, 8)], 7)

  # no spells
  # r07 = 2 * calculageAverage(16, 3, [(1, 8)], 13) + calculageAverageAdvantage(16, 3, [(1, 6)], 0) + calculageAverage(16, 6, [(1, 8)], 6)
  # r08 = 2 * calculageAverage(17, 4, [(1, 8)], 14) + calculageAverageAdvantage(17, 4, [(1, 6)], 0) + calculageAverage(17, 6, [(1, 8)], 6)
  # r09 = 2 * calculageAverage(18, 5, [(1, 8)], 14) + calculageAverageAdvantage(18, 5, [(1, 6)], 0) + calculageAverage(18, 7, [(1, 8)], 7)

  r11 = 2 * calculageAverage(18, 5, [(1, 8)], 14) + 2 * calculageAverage(18, 7, [(1, 8), (1, 6)], 6) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r12 = 2 * calculageAverage(18, 6, [(1, 8)], 15) + 2 * calculageAverage(18, 7, [(1, 8), (1, 6)], 6) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)
  r13 = 2 * calculageAverage(19, 7, [(1, 8)], 15) + 2 * calculageAverage(19, 8, [(1, 8), (1, 6)], 7) + 2 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)

  r15 = 2 * calculageAverageAdvantage(19, 7, [(1, 8)], 15) + 2 * calculageAverageAdvantage(19, 8, [(1, 8), (1, 6)], 7)
  r16 = 2 * calculageAverageAdvantage(19, 7, [(1, 8)], 15) + 2 * calculageAverageAdvantage(19, 9, [(1, 8), (1, 6)], 8)
  r17 = 2 * calculageAverageAdvantage(20, 8, [(1, 8)], 15) + 2 * calculageAverageAdvantage(20, 10, [(1, 8), (1, 6)], 9)

  r19 = 2 * calculageAverage(20, 8, [(1, 8)], 15) + 2 * calculageAverage(20, 11, [(1, 8), (1, 6)], 10) + 4 * calculageAverageAdvantage(18, 6, [(2, 6)], 3)


  return [r01, r02, r03, r04, r05, r06, r07, r08, r09, r09, r11, r12, r13, r13, r15, r16, r17, r17, r19, r19]