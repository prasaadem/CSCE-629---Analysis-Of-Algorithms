import program

def test_program1():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 1 with expected cost 6'
    matrix = [1,2,3]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 6

def test_program2():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 2 with expected cost 362'
    matrix = [1,11,16,9,3,4,1]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 362

def test_program3():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 3 with expected cost 3376'
    matrix = [8,16,22,6,4,11,8,9]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 3376

def test_program4():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 4 with expected cost 0'
    matrix = [1,1]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 0

def test_program5():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 5 with expected cost 10'
    matrix = [1,3,1,7]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 10

def test_program6():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 6 with expected cost 0'
    matrix = [7,6]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 0

def test_program7():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 7 with expected cost 189'
    matrix = [3,3,3,3,3,3,3,3,3]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 189

def test_program8():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 8 with expected cost 202'
    matrix = [1,9,7,4,6,3,22,1]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 202

def test_program9():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 9 with expected cost 591'
    matrix = [1,6,33,9,3,22,1]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 591

def test_program10():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 10 with expected cost 18'
    matrix = [1,2,3,4]
    print 'Given array of matrix rank is: '
    print matrix
    value = program.matrix_chain_multiplication(matrix)
    print 'Output Cost: ' + str(value)
    assert value == 18