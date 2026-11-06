import pygame            

WIDTH,HEIGHT = 1250,750

def UnitOperations(UnitCount,Units,data,FrameRate,EnemyCount,Enemies,EnemyBaseHealth,screen,UnitY):
    for i in range(UnitCount):
        unitSize = (Units[i].UnitX - data["Units"][Units[i].UnitType]["UnitSize"] + Units[i].Range + data["Units"][Units[i].UnitType]["UnitPierce"], UnitY - data["Units"][Units[i].UnitType]["UnitSize"])
        ticks_per_frame = max(1, FrameRate // 12)
        max_post_ticks = len(Units[i].PostAnimations[Units[i].UnitType]) * ticks_per_frame
                            
        if Units[i].UnitHealth <= 0:
            Units[i].UnitX = 0
        if Units[i].UnitCooldown >= 0:
            Units[i].UnitCooldown -= 1
        if (Units[i].UnitCooldown <= 0 and data["Units"][Units[i].UnitType]["UnitPause"] == "True") or (data["Units"][Units[i].UnitType]["UnitPause"] == "False" and Units[i].UnitPostAnimation >= max_post_ticks - 1):
            if (Units[i].UnitX + 120 < WIDTH - Units[i].Range and abs(Units[i].UnitX - FrontmostEnemy(Enemies,EnemyCount)) > Units[i].Range) and Units[i].UnitX > 0:

                Units[i].UnitX += data["Units"][Units[i].UnitType]["UnitSpeed"]*24/FrameRate
                Units[i].UnitAtkAnimation = 0
                max_ticks = len(Units[i].WalkAnimations[Units[i].UnitType]) * (FrameRate / 12)
                Units[i].UnitAnimation = (Units[i].UnitAnimation + 1) % max_ticks
                screen.blit(Units[i].drawWalk(),unitSize)
                

            elif Units[i].UnitX > 0:

                if Units[i].UnitCooldown <= 0:
                    ticks_per_frame = max(1, FrameRate // 12)
                    max_atk_ticks = len(Units[i].AtkAnimations[Units[i].UnitType]) * ticks_per_frame
                    if Units[i].UnitAtkAnimation >= max_atk_ticks - 1:
                        Units[i].UnitCooldown = data["Units"][Units[i].UnitType]["UnitAtkCooldown"]*FrameRate
                        Units[i].UnitAtkAnimation = 0
                        Units[i].UnitPostAnimation = 0
                        screen.blit(Units[i].drawPost(),unitSize)
                                        

                        if data["Units"][Units[i].UnitType]["UnitAttackType"] == "Area":
                            if Units[i].UnitX + 120 >= WIDTH - Units[i].Range:
                                EnemyBaseHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                            for j in range(EnemyCount):
                                if Enemies[j].EnemyX <= Units[i].UnitX + Units[i].Range + data["Units"][Units[i].UnitType]["UnitPierce"] and Enemies[j].EnemyX >= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitBlindspot"]:
                                    Enemies[j].EnemyHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]

                        elif data["Units"][Units[i].UnitType]["UnitAttackType"] == "Single":
                            if Units[i].UnitX + 120 >= WIDTH - Units[i].Range and FrontmostEnemy(Enemies,EnemyCount) > WIDTH - 120:
                                EnemyBaseHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                            for j in range(EnemyCount):
                                if Enemies[j].EnemyX <= Units[i].UnitX + Units[i].Range + data["Units"][Units[i].UnitType]["UnitPierce"] and Enemies[j].EnemyX >= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitBlindspot"]:
                                    if Enemies[j].EnemyX == FrontmostEnemy(Enemies,EnemyCount):
                                        Enemies[j].EnemyHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                                        break

                    else:
                        max_ticks = len(Units[i].AtkAnimations[Units[i].UnitType]) * (FrameRate / 12)
                        Units[i].UnitAtkAnimation = (Units[i].UnitAtkAnimation + 1) % max_ticks
                        screen.blit(Units[i].drawAtk(),unitSize)
                                        
                else:
                    if Units[i].UnitPostAnimation >= max_post_ticks - 1:
                        Units[i].UnitAtkAnimation = 0
                        screen.blit(Units[i].drawStand(),unitSize)
                    else:
                        screen.blit(Units[i].drawPost(),unitSize)
                        Units[i].UnitPostAnimation += 1

        else:
            if Units[i].UnitPostAnimation >= max_post_ticks - 1:
                Units[i].UnitAtkAnimation = 0
                screen.blit(Units[i].drawStand(),unitSize)
            else:
                screen.blit(Units[i].drawPost(),unitSize)
                Units[i].UnitPostAnimation += 1
                                    

def EnemyOperations(EnemyCount,Enemies,data,FrameRate,UnitCount,Units,UnitBaseHealth,Money,screen,EnemyY):
    for i in range(EnemyCount):
        enemySize = (Enemies[i].EnemyX, EnemyY - data["Enemy"][Enemies[i].EnemyType]["EnemySize"])
        if Enemies[i].EnemyHealth <= 0:
            if Enemies[i].EnemyX < WIDTH:
                Money += data["Enemy"][Enemies[i].EnemyType]["EnemyHealth"]
            Enemies[i].EnemyX = WIDTH
        if Enemies[i].EnemyCooldown >= 0:
            Enemies[i].EnemyCooldown -= 1
        if (Enemies[i].EnemyCooldown <= 0 and data["Enemy"][Enemies[i].EnemyType]["EnemyPause"] == "True") or data["Enemy"][Enemies[i].EnemyType]["EnemyPause"] == "False":
            if (Enemies[i].EnemyX + 50 > data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] and abs(Enemies[i].EnemyX - FrontmostUnit(Units,UnitCount)) > data["Enemy"][Enemies[i].EnemyType]["EnemyRange"]) and Enemies[i].EnemyX < WIDTH:

                Enemies[i].EnemyX -= data["Enemy"][Enemies[i].EnemyType]["EnemySpeed"]*24/FrameRate
                Enemies[i].EnemyAtkAnimation = 0
                max_ticks = len(Enemies[i].EnemyWalkAnimations[Enemies[i].EnemyType]) * (FrameRate / 12)
                Enemies[i].EnemyAnimation = (Enemies[i].EnemyAnimation + 1) % max_ticks
                screen.blit(Enemies[i].drawWalk(),enemySize)


            elif Enemies[i].EnemyX < WIDTH:

                if Enemies[i].EnemyCooldown <= 0:
                    ticks_per_frame = max(1, FrameRate // 12)
                    max_atk_ticks = len(Enemies[i].EnemyAtkAnimations[Enemies[i].EnemyType]) * ticks_per_frame
                    if Enemies[i].EnemyAtkAnimation >= max_atk_ticks - 1:
                        Enemies[i].EnemyCooldown = data["Enemy"][Enemies[i].EnemyType]["EnemyAtkCooldown"]*FrameRate
                        Enemies[i].EnemyAtkAnimation = 0
                        screen.blit(Enemies[i].drawStand(),enemySize)


                        if data["Enemy"][Enemies[i].EnemyType]["EnemyAttackType"] == "Area":
                            if Enemies[i].EnemyX + 50 <= data["Enemy"][Enemies[i].EnemyType]["EnemyRange"]:
                                UnitBaseHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                            for j in range(UnitCount):
                                if Units[j].UnitX >= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] - data["Enemy"][Enemies[i].EnemyType]["EnemyPierce"] and Units[j].UnitX <= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyBlindspot"]:
                                    Units[j].UnitHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]

                        elif data["Enemy"][Enemies[i].EnemyType]["EnemyAttackType"] == "Single":
                            if Enemies[i].EnemyX + 50 <= data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] and FrontmostUnit(Units,UnitCount) < 50:
                                UnitBaseHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                            for j in range(UnitCount):
                                if Units[j].UnitX >= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] - data["Enemy"][Enemies[i].EnemyType]["EnemyPierce"] and Units[j].UnitX <= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyBlindspot"]:
                                    if Units[j].UnitX == FrontmostUnit(Units,UnitCount):
                                        Units[j].UnitHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                                        break

                    else:
                        max_ticks = len(Enemies[i].EnemyAtkAnimations[Enemies[i].EnemyType]) * (FrameRate / 12)
                        Enemies[i].EnemyAtkAnimation = (Enemies[i].EnemyAtkAnimation + 1) % max_ticks
                        screen.blit(Enemies[i].drawAtk(),enemySize)

                else:
                    Enemies[i].EnemyAtkAnimation = 0
                    screen.blit(Enemies[i].drawStand(),enemySize)
        else:
            Enemies[i].EnemyAtkAnimation = 0
            screen.blit(Enemies[i].drawStand(),enemySize)
    return Money



def FrontmostUnit(Units,UnitCount):
    FrontmostX = Units[0].UnitX
    for i in range(UnitCount):
        if Units[i].UnitX > FrontmostX:
            FrontmostX = Units[i].UnitX
    return FrontmostX

def FrontmostEnemy(Enemies,EnemyCount):
    FrontmostEnemyX = Enemies[0].EnemyX
    for i in range(EnemyCount):
        if Enemies[i].EnemyX < FrontmostEnemyX:
            FrontmostEnemyX = Enemies[i].EnemyX
    return FrontmostEnemyX