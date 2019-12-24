import unittest 
  
class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass

    def changes(): 
        pass
  
    # Returns True if the string contains 4 a. 
    def test_strings_a(self): 
        self.assertEqual( 'a'*4, 'aaaa') 
  
    # Returns True if the string is in upper case. 
    def test_upper(self):         
        self.assertEqual('foo'.upper(), 'FOO') 
  
    # Returns TRUE if the string is in uppercase 
    # else returns False. 
    def test_isupper(self):         
        self.assertTrue('FOO'.isupper()) 
        self.assertFalse('Foo'.isupper()) 
  
    # Returns true if the string is stripped and  
    # matches the given output. 
    def test_strip(self):         
        s = 'geeksforgeeks'
        self.assertEqual(s.strip('geek'), 'sforgeeks') 
  
    # Returns true if the string splits and matches 
    # the given output. 
    def test_split(self):         
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world']) 
        with self.assertRaises(TypeError): 
            s.split(2) 
  
if __name__ == '__main__': 
    unittest.main() 
# The above code is a short script to test 5 string methods. unittest.TestCase is used to create test cases by subclassing it. The last block of the code at the bottom allows us to run all the tests just by running the file.


# Basic terms used in the code :

# assertEqual() – This statement is used to check if the result obtained is equal to the expected result.
# assertTrue() / assertFalse() – This statement is used to verify if a given statement is true or false.
# assertRaises() – This statement is used to raise a specific exception.
# Description of tests :

# test_strings_a
# This test is used to test the property of string in which a character say ‘a’ multiplied by a number say ‘x’ gives the output as x times ‘a’. The assertEqual() statement returns true in this case if the result matches the given output.
# test_upper
# This test is used to check if the given string is converted to uppercase or not. The assertEqual() statement returns true if the string returned is in uppercase.
# test_isupper
# This test is used to test the property of string which returns TRUE if the string is in uppercase else returns False. The assertTrue() / assertFalse() statement is used for this verification.
# test_strip
# This test is used to check if all chars passed in the function have been stripped from the string. The assertEqual() statement returns true if the string is stripped and matches the given output.
# test_split
# This test is used to check the split function of the string which splits the string through the argument passed in the function and returns the result as list. The assertEqual() statement returns true in this case if the result matches the given output.
# unittest.main() provides a command-line interface to the test script.On running the above script from the command line, following output is produced :