# This is a horrible hacky mess, you have been warned
import sys
import string
import math
tableStart2 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| l | l |}
\hline
"""
tableStart3 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| l | l | l |}
\hline
"""
tableStart4 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| l | l | l | l |}
\hline
"""
tableStart5 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| l | l | l | l | l |}
\hline
"""
tableStart6 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c |}
\hline
"""
tableStart7 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart9 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart10 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart11 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart12 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart13 = r"""\begin{center}
\begin{adjustwidth}{-4cm}{}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableEnd = r"""\hline
\end{tabular}
\end{small}
\end{adjustwidth}
\end{center}
"""
baseClasses = ["Assassin.md"
			  ,"Barbarian.md"
			  ,"Bard.md"
			  ,"Cleric.md"
			  ,"Diploconvoker.md"
			  ,"DreadNecromancer.md"
			  ,"Druid.md"
			  ,"HorizonWalker.md"
			  ,"Jester.md"
			  ,"Knight.md"
			  ,"Marshall.md"
			  ,"Monk.md"
			  ,"Paladin.md"
			  ,"Pyrokineticist.md"
			  ,"Pyromancer.md"
			  ,"Ranger.md"
			  ,"Rogue.md"
			  ,"Shadowdancer.md"
			  ,"Soldier.md"
			  ,"SongweaverBard.md"
			  ,"Sorcerer.md"
			  ,"ThiefAcrobat.md"
			  ,"Wizard.md"
			  ]
prestigeClasses = ["ArcaneArcher.md"
				  ,"ArcaneTrickster.md"
				  ,"Blackguard.md"
				  ,"Defender.md"
				  ,"DragonDisciple.md"
				  ,"Duelist.md"
				  ,"EldritchKnight.md"
				  ,"Fighter.md"
				  ,"Hierophant.md"
				  ,"Loremaster.md"
				  ,"MysticTheurge.md"
				  ,"Thaumaturgist.md"
				  ]
psionicBaseClasses = ["Elocater.md"
					 ,"Psion.md"
					 ,"PsionUncarnate.md"
					 ,"PsychicWarrior.md"
					 ,"Soulknife.md"
					 ,"Wilder.md"
					 ]
psionicPrestigeClasses = ["Cerebremancer.md"
						 ,"Metamind.md"
						 ,"PsionicFist.md"
						 ,"Slayer.md"
						 ,"Thrallherd.md"
						 ,"WarMind.md"
						 ]
def escapePercent(lineNum):
	inFile[lineNum] = inFile[lineNum].replace("%","\%")
def splitCell(cell): #Some long table cells make the tables run off the page
	midPoint = math.ceil(len(cell)/2)
	offset = 0
	while True: # This is technically bad, but any long cell is going to have spaces
		if cell[midPoint + offset] == " ":
			return r"\makecell{" + cell[:midPoint+offset] + r"\\" + cell[midPoint+offset:] + "}"
		if cell[midPoint - offset] == " ":
			return r"\makecell{" + cell[:midPoint-offset] + r"\\" + cell[midPoint-offset:] + "}"
		offset += 1
def processLine(lineNum):
	print(inFile[lineNum])
	if inFile[lineNum].isspace():
		return lineNum + 1
	elif inFile[lineNum][0] == "*":
		if inFile[lineNum][1] == "*":
			return processAbility(lineNum)
		return lineNum + 1
	elif inFile[lineNum][0] == "#":
		return processTitle(lineNum)
	elif inFile[lineNum].count("|") >= 1:
		return processTable(lineNum)
	else:
		return lineNum + 1
def processAbility(lineNum): # **BOLD**(Su): Description of thing || **BOLD**: Description of thing
	titleDefinition = inFile[lineNum].split(":",1)
	titleDefinition[0] = r"\textbf{" + titleDefinition[0].replace("*","") + "}:"
	if len(titleDefinition) == 1:
		inFile[lineNum] = titleDefinition[0] + "\n"
	elif len(titleDefinition) == 2:
		inFile[lineNum] = titleDefinition[0] + titleDefinition[1]
	return lineNum + 1
def processTitle(lineNum):
	if inFile[lineNum].count("#") == 1:
		inFile[lineNum] = r"\textbf{\huge{" + inFile[lineNum].replace("#","").strip() + "}}\n"
	else:
		inFile[lineNum] = r"\textbf{\large{" + inFile[lineNum].replace("#","").strip() + "}}\n"
	return lineNum + 1
def processTable(lineNum):
	if inFile[lineNum].count("|") == 5: # This accounts for different table widths
		inFile.insert(lineNum,tableStart6)
	elif inFile[lineNum].count("|") == 1:
		inFile.insert(lineNum,tableStart2)
	elif inFile[lineNum].count("|") == 2:
		inFile.insert(lineNum,tableStart3)
	elif inFile[lineNum].count("|") == 3:
		inFile.insert(lineNum,tableStart4)
	elif inFile[lineNum].count("|") == 4:
		inFile.insert(lineNum,tableStart5)
	elif inFile[lineNum].count("|") == 6:
		inFile.insert(lineNum,tableStart7)
	elif inFile[lineNum].count("|") == 7:
		inFile.insert(lineNum,tableStart8)
	elif inFile[lineNum].count("|") == 8:
		inFile.insert(lineNum,tableStart9)
	elif inFile[lineNum].count("|") == 9:
		inFile.insert(lineNum,tableStart10)
	elif inFile[lineNum].count("|") == 10:
		inFile.insert(lineNum,tableStart11)
	elif inFile[lineNum].count("|") == 11:
		inFile.insert(lineNum,tableStart12)
	elif inFile[lineNum].count("|") == 12:
		inFile.insert(lineNum,tableStart13)
	else:
		print("Inappropriate Table Width")
		exit(1)
	lineNum += 1
	lineToReplace = lineNum + 1
	del inFile[lineToReplace] # This accounts for the 2nd line in MD tables 
	while lineNum < len(inFile) and not inFile[lineNum].isspace():
		tableRow = inFile[lineNum].split("|")
		tableLine = tableRow[0].strip() + " "
		for cell in tableRow[1:]:
			line = cell.strip()
			if len(line) >= 60:
				tableLine += "&" + splitCell(line) + " "
			else:
				tableLine += "&" + line + " "
		inFile[lineNum] = tableLine + r"\\" + "\n"
		lineNum += 1
	inFile.insert(lineToReplace,"\\hline\n")
	inFile.insert(lineNum+1,tableEnd)
	return lineNum + 1

for file in baseClasses:
	print(file)
	mdFile = open("classes/"+file, 'r')
	inFile = mdFile.readlines()
	mdFile.close()
	lineNum = 0
	while lineNum < len(inFile):
		escapePercent(lineNum)
		lineNum = processLine(lineNum)
#	inFile.insert(0,"\\documentclass{article}\n\\begin{document}\n")
#	inFile.append("\n\\end{document}\n")
	texFile = open("latex/classes/"+file.split(".")[0]+".tex","w")
	texFile.write("".join(inFile))
	texFile.close()
for file in prestigeClasses:
	print(file)
	mdFile = open("prestige_classes/"+file, 'r')
	inFile = mdFile.readlines()
	mdFile.close()
	lineNum = 0
	while lineNum < len(inFile):
		escapePercent(lineNum)
		lineNum = processLine(lineNum)
#	inFile.insert(0,"\\documentclass{article}\n\\begin{document}\n")
#	inFile.append("\n\\end{document}\n")
	texFile = open("latex/prestige_classes/"+file.split(".")[0]+".tex","w")
	texFile.write("".join(inFile))
	texFile.close()
for file in psionicBaseClasses:
	print(file)
	mdFile = open("classes/Psionic/"+file, 'r')
	inFile = mdFile.readlines()
	mdFile.close()
	lineNum = 0
	while lineNum < len(inFile):
		escapePercent(lineNum)
		lineNum = processLine(lineNum)
#	inFile.insert(0,"\\documentclass{article}\n\\begin{document}\n")
#	inFile.append("\n\\end{document}\n")
	texFile = open("latex/classes/Psionic/"+file.split(".")[0]+".tex","w")
	texFile.write("".join(inFile))
	texFile.close()
for file in psionicPrestigeClasses:
	print(file)
	mdFile = open("prestige_classes/Psionic/"+file, 'r')
	inFile = mdFile.readlines()
	mdFile.close()
	lineNum = 0
	while lineNum < len(inFile):
		escapePercent(lineNum)
		lineNum = processLine(lineNum)
#	inFile.insert(0,"\\documentclass{article}\n\\begin{document}\n")
#	inFile.append("\n\\end{document}\n")
	texFile = open("latex/prestige_classes/Psionic/"+file.split(".")[0]+".tex","w")
	texFile.write("".join(inFile))
	texFile.close()
#print(tableStart6)