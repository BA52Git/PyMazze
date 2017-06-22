#!/usr/bin/env python -tt
# Copyright 2017 Benjamin Avery
# Private use only
# http://www.instagram.com/baddogphotography

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# a = [255, 196, 194, 191], [195, 255, 179, 179], [195, 255, 179, 179], [192, 196, 255, 179]]
tempMaze = [[2, 8, 0xE, 6], [0xB, 4, 3, 3], [0xB, 4, 1, 3], [9, 0xC, 4, 1]]

maze = [2,2]

mazeWidth = 4
mazeHeight = 4
mazeChunkWidth = 3
mazeChunkHeight = 3
maze0 = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
maze1 = [[' ','X',' '],[' ','X',' '],[' ',' ',' ']]
maze2 = [[' ',' ',' '],[' ','X',' '],[' ','X',' ']]
maze3 = [[' ','X',' '],[' ','X',' '],[' ','X',' ']]
maze4 = [[' ',' ',' '],['X','X',' '],[' ',' ',' ']]
maze5 = [[' ','X',' '],['X','X',' '],[' ',' ',' ']]
maze6 = [[' ',' ',' '],['X','X',' '],[' ','X',' ']]
maze7 = [[' ','X',' '],['X','X',' '],[' ','X',' ']]
maze8 = [[' ',' ',' '],[' ','X','X'],[' ',' ',' ']]
maze9 = [[' ','X',' '],[' ','X','X'],[' ',' ',' ']]
mazeA = [[' ',' ',' '],[' ','X','X'],[' ','X',' ']]
mazeB = [[' ','X',' '],[' ','X','X'],[' ','X',' ']]
mazeC = [[' ',' ',' '],['X','X','X'],[' ',' ',' ']]
mazeD = [[' ','X',' '],['X','X','X'],[' ',' ',' ']]
mazeE = [[' ',' ',' '],['X','X','X'],[' ','X',' ']]
mazeF = [[' ','X',' '],['X','X','X'],[' ','X',' ']]

# maze0 = [['0','0','0'],['0','0','0'],['0','0','0']]
# maze1 = [['0','X','0'],['0','x','0'],['0','0','0']]
# maze2 = [['0','0','0'],['0','x','0'],['0','X','0']]
# maze3 = [['0','X','0'],['0','x','0'],['0','X','0']]
# maze4 = [['0','0','0'],['X','x','0'],['0','0','0']]
# maze5 = [['0','X','0'],['X','x','0'],['0','0','0']]
# maze6 = [['0','0','0'],['X','x','0'],['0','X','0']]
# maze7 = [['0','X','0'],['X','x','0'],['0','X','0']]
# maze8 = [['0','0','0'],['0','x','X'],['0','0','0']]
# maze9 = [['0','X','0'],['0','x','X'],['0','0','0']]
# mazeA = [['0','0','0'],['0','x','X'],['0','X','0']]
# mazeB = [['0','X','0'],['0','x','X'],['0','X','0']]
# mazeC = [['0','0','0'],['X','x','X'],['0','0','0']]
# mazeD = [['0','X','0'],['X','x','X'],['0','0','0']]
# mazeE = [['0','0','0'],['X','x','X'],['0','X','0']]
# mazeF = [['0','X','0'],['X','x','X'],['0','X','0']]

#Right now this just sends commands to print the predetermined maze.
# In the future, this should take two inputs (length and width), then 
# print a randomly generated maze of that size.
def main():
	global maze
		# for char in range(len(a[iter])):
# 			print(a[char][iter]),
	maze = generateBoundary(maze, mazeWidth,mazeHeight)	
	mazePrint(maze)
	print
		
		
def generateBoundary(boundmaze, boundWidth, boundHeight):
	boundmaze[0][0] = 0xA
	boundmaze[0][boundWidth] = 0x6
	boundmaze[boundWidth][0] = 0x9
	boundmaze[boundWidth][boundHeight] = 0x5
	for boundlines in range(1,boundWidth):
		boundmaze[boundlines][0] = 0xC
		boundmaze[boundlines][boundHeight] = 0xC
	for boundcolumns in range(1,boundcolumns):
		boundmaze[0][boundcolumns] = 0x3
		boundmaze[boundWidth][boundcolumns] = 0x3
		
def mazePrint(printArray):
	for mazeY in range(0, mazeHeight):
		for mazeLine in range(0, mazeChunkWidth):
			for mazeX in range(0,mazeWidth):
				disLine = getMazeChunkLine(tempMaze[mazeY][mazeX],mazeLine)
				for outputElement in disLine:
					print outputElement,
				#				nada = input()
			print
				
				
def getMazeChunkLine(chunkNum, lineNum):
	switcher = {
		0: maze0,
		1: maze1,
		2: maze2,
		3: maze3,
		4: maze4,
		5: maze5,
		6: maze6,
		7: maze7,
		8: maze8,
		9: maze9,
		0xA: mazeA,
		0xB: mazeB,
		0xC: mazeC,
		0xD: mazeD,
		0xE: mazeE,
		0xF: mazeF
	}
	#print(lineNum),
	return switcher.get(chunkNum)[lineNum]
	
				
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
