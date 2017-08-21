import program
import sys

def test_program1():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 1 with expected Maximum flow 14'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('a','c')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 14

def test_program2():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 2 with expected Maximum flow 9'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('a','b')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 9

def test_program3():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 3 with expected Maximum flow 4'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('a','d')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 4

def test_program4():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 4 with expected Maximum flow 7'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('a','e')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 7

def test_program5():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 5 with expected Maximum flow 4'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('a','f')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 4

def test_program6():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 6 with expected Maximum flow 0'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('f','b')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 0

def test_program7():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 7 with expected Maximum flow 0'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('e','a')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 0

def test_program8():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 8 with expected Maximum flow 0'
    program.g = program.Flow()
    map(program.g.addCorners, ['a', 'b', 'c', 'd', 'e', 'f'])
    program.g.addOneEdge('a', 'b', 9)
    program.g.addOneEdge('a', 'c', 8)
    program.g.addOneEdge('b', 'c', 6)
    program.g.addOneEdge('b', 'd', 4)
    program.g.addOneEdge('c', 'e', 5)
    program.g.addOneEdge('c', 'e', 2)
    program.g.addOneEdge('d', 'f', 8)
    program.g.addOneEdge('d', 'f', 2)
    flow = program.g.maximumFlow('d','b')
    print 'Output Maximum Flow: ' + str(flow)
    assert flow == 0

