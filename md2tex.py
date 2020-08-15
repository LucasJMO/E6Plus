import sys
import string
tableStart6 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c |}
\hline
"""
tableStart7 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart8 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c |}
\hline
"""
tableStart9 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart10 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart11 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart12 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableStart13 = r"""\begin{center}
\begin{small}
\begin{tabular}{| c | c | c | c | c | c | c | c | c | c | c | c | c |}
\hline
"""
tableEnd = r"""\hline
\end{tabular}
\end{small}
\end{center}
"""
def processLine(lineNum):
	if inFile[lineNum].isspace():
		return lineNum + 1
	elif inFile[lineNum][0] == "*":
		return processAbility(lineNum)
	elif inFile[lineNum][0] == "#":
		return processTitle(lineNum)
	elif inFile[lineNum].count("|") >= 5:
		return processTable(lineNum)
	else:
		return lineNum + 1
def processAbility(lineNum): # **BOLD**(Su): Description of thing || **BOLD**: Description of thing
	titleDefinition = inFile[lineNum].split(":",1)
	titleDefinition[0] = r"\textbf{" + titleDefinition[0].replace("*","") + "}:"
	inFile[lineNum] = titleDefinition[0] + titleDefinition[1]
	return lineNum + 1
def processTitle(lineNum):
	if inFile[lineNum].count("#") == 1:
		inFile[lineNum] = r"\textbf{\huge{" + inFile[lineNum].replace("#","").strip() + "}}\n"
	else:
		inFile[lineNum] = r"\textbf \large{" + inFile[lineNum].replace("#","").strip() + "}}\n"
	return lineNum + 1
def processTable(lineNum):
	if inFile[lineNum].count("|") == 5: # This accounts for different table widths
		inFile.insert(lineNum,tableStart6)
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
	lineNum += 1
	lineToReplace = lineNum + 1
	del inFile[lineToReplace] # This accounts for the 2nd line in MD tables 
	while lineNum < len(inFile) and not inFile[lineNum].isspace():
		tableRow = inFile[lineNum].split("|")
		tableLine = tableRow[0].strip() + " "
		for cell in tableRow[1:]:
			tableLine += "&" + cell.strip() + " "
		inFile[lineNum] = tableLine + r"\\" + "\n"
		lineNum += 1
	inFile.insert(lineToReplace,"\\hline\n")
	inFile.insert(lineNum+1,tableEnd)
	return lineNum + 1

mdFile = open(sys.argv[1], 'r')
inFile = mdFile.readlines()
mdFile.close()
lineNum = 0
while lineNum < len(inFile):
	lineNum = processLine(lineNum)
inFile.insert(0,"\\documentclass{article}\n\\begin{document}\n")
inFile.append("\n\\end{document}\n")
print("".join(inFile))
#print(tableStart6)