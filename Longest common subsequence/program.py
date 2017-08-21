# Python 2.7.13
# OS: Macintosh
# Author: Aditya Emani - 524002563
# Course: CSCE 629 - Analysis of Algorithms - Fall 2016

# Longest Common subsequence

import sys

def longest_common_subsequence(string1, string2):
  rows = len(string1) + 1
  cols = len(string2) + 1
  position = [[0 for x in xrange(cols)] for y in xrange(rows)]
  path = [[(0, 0) for x in xrange(cols)] for y in xrange(rows)]

  for i in xrange(1, rows):
    for j in xrange(1, cols):
      if string1[i - 1] == string2[j - 1]:
        position[i][j] = position[i - 1][j - 1] + 1
        path[i][j] = (i - 1, j - 1)
      else:
        if position[i - 1][j] >= position[i][j - 1]:
          position[i][j] = position[i - 1][j]
          path[i][j] = (i - 1, j)
        else:
          position[i][j] = position[i][j - 1]
          path[i][j] = (i, j - 1)
  
  length = position[rows - 1][cols - 1]
  string = ''
  row = rows - 1
  col = cols - 1

  while row > 0 or col > 0:
    prev_row, prev_col = path[row][col]
    if position[row][col] != position[prev_row][prev_col]:
      string += string1[row - 1]
    row = prev_row
    col = prev_col
  string = string[::-1]
  return length, string


def main():
  string1 = "ABABCZ"
  string2 = "ABCAZZ"
  length, string= longest_common_subsequence(string1, string2)
  print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)

main()