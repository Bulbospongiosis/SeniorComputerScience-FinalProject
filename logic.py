import pygame            

WIDTH,HEIGHT = 1250,750

def UnitOperations(UnitCount,Units,data,FrameRate,EnemyCount,Enemies,WalkAnimations,AtkAnimations,EnemyBaseHealth):

    for i in range(UnitCount):
        if Units[i].UnitHealth <= 0:
            Units[i].UnitX = 0
        if Units[i].UnitCooldown >= 0:
            Units[i].UnitCooldown -= 1
        if (Units[i].UnitCooldown <= 0 and data["Units"][Units[i].UnitType]["UnitPause"] == "True") or data["Units"][Units[i].UnitType]["UnitPause"] == "False":
            if (Units[i].UnitX + 120 < WIDTH - data["Units"][Units[i].UnitType]["UnitRange"] and abs(Units[i].UnitX - FrontmostEnemy(Enemies,EnemyCount)) > data["Units"][Units[i].UnitType]["UnitRange"]) and Units[i].UnitX > 0:

                Units[i].UnitX += data["Units"][Units[i].UnitType]["UnitSpeed"]*24/FrameRate
                Units[i].UnitAtkAnimation = 0
                Units[i].UnitAnimation += 1 if Units[i].UnitAnimation < len(WalkAnimations[Units[i].UnitType])*FrameRate/12 else -Units[i].UnitAnimation

            elif Units[i].UnitX > 0:

                if Units[i].UnitCooldown <= 0:
                    if Units[i].UnitAtkAnimation >= (len(AtkAnimations[Units[i].UnitType])-1)*FrameRate/12:
                        Units[i].UnitCooldown = data["Units"][Units[i].UnitType]["UnitAtkCooldown"]*FrameRate
                        Units[i].UnitAtkAnimation = 0

                        if data["Units"][Units[i].UnitType]["UnitAttackType"] == "Area":
                            if Units[i].UnitX + 120 >= WIDTH - data["Units"][Units[i].UnitType]["UnitRange"]:
                                EnemyBaseHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                            for j in range(EnemyCount):
                                if Enemies[j].EnemyX <= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitRange"] + data["Units"][Units[i].UnitType]["UnitPierce"] and Enemies[j].EnemyX >= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitBlindspot"]:
                                    Enemies[j].EnemyHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]

                        elif data["Units"][Units[i].UnitType]["UnitAttackType"] == "Single":
                            if Units[i].UnitX + 120 >= WIDTH - data["Units"][Units[i].UnitType]["UnitRange"] and FrontmostEnemy(Enemies,EnemyCount) > WIDTH - 120:
                                EnemyBaseHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                            for j in range(EnemyCount):
                                if Enemies[j].EnemyX <= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitRange"] + data["Units"][Units[i].UnitType]["UnitPierce"] and Enemies[j].EnemyX >= Units[i].UnitX + data["Units"][Units[i].UnitType]["UnitBlindspot"]:
                                    if Enemies[j].EnemyX == FrontmostEnemy(Enemies,EnemyCount):
                                        Enemies[j].EnemyHealth -= data["Units"][Units[i].UnitType]["UnitDamage"]
                                        break

                    else:
                        Units[i].UnitAtkAnimation += 1
                else:
                    Units[i].UnitCooldown -= 1
                    Units[i].UnitAtkAnimation = 0

def EnemyOperations(EnemyCount,Enemies,data,FrameRate,UnitCount,Units,EnemyWalkAnimations,EnemyAtkAnimations,UnitBaseHealth):   

    for i in range(EnemyCount):
        if Enemies[i].EnemyHealth <= 0:
            Enemies[i].EnemyX = WIDTH
        if Enemies[i].EnemyCooldown >= 0:
            Enemies[i].EnemyCooldown -= 1
        if (Enemies[i].EnemyCooldown <= 0 and data["Enemy"][Enemies[i].EnemyType]["EnemyPause"] == "True") or data["Enemy"][Enemies[i].EnemyType]["EnemyPause"] == "False":
            if (Enemies[i].EnemyX + 50 > data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] and abs(Enemies[i].EnemyX - FrontmostUnit(Units,UnitCount)) > data["Enemy"][Enemies[i].EnemyType]["EnemyRange"]) and Enemies[i].EnemyX < WIDTH:
                Enemies[i].EnemyX -= data["Enemy"][Enemies[i].EnemyType]["EnemySpeed"]*24/FrameRate
                Enemies[i].EnemyAnimation += 1 if Enemies[i].EnemyAnimation < len(EnemyWalkAnimations[Enemies[i].EnemyType])*FrameRate/12 else -Enemies[i].EnemyAnimation

            elif Enemies[i].EnemyX < WIDTH:

                if Enemies[i].EnemyCooldown <= 0:
                        if Enemies[i].EnemyAtkAnimation >= (len(EnemyAtkAnimations[Enemies[i].EnemyType])-1)*FrameRate/12:
                            Enemies[i].EnemyCooldown = data["Enemy"][Enemies[i].EnemyType]["EnemyAtkCooldown"]*FrameRate
                            Enemies[i].EnemyAtkAnimation = 0
                            if data["Enemy"][Enemies[i].EnemyType]["EnemyAttackType"] == "Area":
                                if Enemies[i].EnemyX + 50 <= data["Enemy"][Enemies[i].EnemyType]["EnemyRange"]:
                                    UnitBaseHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                                    print("attack")
                                for j in range(UnitCount):
                                    if Units[j].UnitX >= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] - data["Enemy"][Enemies[i].EnemyType]["EnemyPierce"] and Units[j].UnitX <= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyBlindspot"]:
                                        Units[j].UnitHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                            elif data["Enemy"][Enemies[i].EnemyType]["EnemyAttackType"] == "Single":
                                if Enemies[i].EnemyX + 50 <= data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] and FrontmostUnit(Units,UnitCount) < 50:
                                    UnitBaseHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                                for j in range(UnitCount):
                                    if Units[j].UnitX >= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyRange"] - data["Enemy"][Enemies[i].EnemyType]["EnemyPierce"] and Units[j].UnitX <= Enemies[i].EnemyX - data["Enemy"][Enemies[i].EnemyType]["EnemyBlindspot"]:
                                        if Units[j].UnitX == FrontmostUnit(Units, UnitCount):
                                            Units[j].UnitHealth -= data["Enemy"][Enemies[i].EnemyType]["EnemyDamage"]
                                            break
                        else:
                            Enemies[i].EnemyAtkAnimation += 1
                else:
                    Enemies[i].EnemyCooldown -= 1
                    Enemies[i].EnemyAtkAnimation = 0



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