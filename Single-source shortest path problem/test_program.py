import program
import sys

def test_program1():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 1 with expected cost 6'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'x','e')
    print 'Output Cost: ' + str(cost)
    assert cost == 6

def test_program2():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 2 with expected cost 6'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'a','e')
    print 'Output Cost: ' + str(cost)
    assert cost == 6

def test_program3():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 3 with expected cost 6'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'b','e')
    print 'Output Cost: ' + str(cost)
    assert cost == 6

def test_program4():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 4 with expected cost 1'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'b','b')
    print 'Output Cost: ' + str(cost)
    assert cost == 1

def test_program5():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 5 with expected cost 6'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'d','e')
    print 'Output Cost: ' + str(cost)
    assert cost == 6

def test_program6():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 6 with expected cost 2'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'a','a')
    print 'Output Cost: ' + str(cost)
    assert cost == 2

def test_program7():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 7 with expected cost 0'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'x','x')
    print 'Output Cost: ' + str(cost)
    assert cost == 0

def test_program8():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 8 with expected cost 6'
    graph = {'x': {'a': 2, 'b': 1},
            'a': {'x': 3, 'b': 4, 'c':8},
            'b': {'x': 8, 'a': 2, 'd': 2},
            'c': {'a': 2, 'd': 9, 'e': 4},
            'd': {'b': 1, 'c': 1, 'e': 3},
            'e': {'c': 3, 'd': 3}}
    cost = program.shortest_path(graph,'x','x')
    print 'Output Cost: ' + str(cost)
    assert cost == 0