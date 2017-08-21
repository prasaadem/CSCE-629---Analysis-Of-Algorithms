import program

def test_program1():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 1 with expected length 0 and string ""'
    string1 = "ABABABABAB"
    string2 = ""
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length) 
    assert length == 0
    assert string == ""

def test_program2():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 2 with expected length 10 and string ABABABABAB'
    string1 = "ABABABABAB"
    string2 = "ABABABABAB"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 10
    assert string == "ABABABABAB"

def test_program3():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 3 with expected length 0 and string ""'
    string1 = ""
    string2 = "ABABABABAB"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 0
    assert string == ""

def test_program4():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 4 with expected length 1 and string "A"'
    string1 = "Aaaaa"
    string2 = "AAAAA"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 1
    assert string == "A"

def test_program5():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 5 with expected length 5 and string "IIIII"'
    string1 = "AZcABGHIIIIIIIIIIIII"
    string2 = "IIIJKHILLLI"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 5
    assert string == "IIIII"

def test_program6():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 6 with expected length 5 and string "QsTlI"'
    string1 = "PQRsTlKI"
    string2 = "QsTlI"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length) 
    assert length == 5
    assert string == "QsTlI"

def test_program7():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 7 with expected length 3 and string "OoL"'
    string1 = "OOOOOO0oPPRLK"
    string2 = "OoL"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length) 
    assert length == 3
    assert string == "OoL"

def test_program8():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 8 with expected length 3 and string "143"'
    string1 = "1469326"
    string2 = "1336437"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length) 
    assert length == 3
    assert string == "143"

def test_program9():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 9 with expected length 4 and string "4j30"'
    string1 = "l425gjsjruusn888930"
    string2 = "4ujewqlo30"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 4
    assert string == "4j30"

def test_program10():
    print '\n--------------------------------------------------------------------------\n'
    print '\nTest Program 10 with expected length 4 and string "TAMU"'
    string1 = "ggeTqqmlAhhhdmmMiiiii938333U"
    string2 = "TAMU"
    length, string= program.longest_common_subsequence(string1, string2)
    print 'The longest common subsequence of ' + string1 + ' and ' +string2+ ' is: '+ string +' ,and its length is: ' + str(length)
    assert length == 4
    assert string == "TAMU"