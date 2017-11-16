# Sentence Reversal
# Problem
# Given a string of words, reverse all the words. For example:
#
# Given:
#
# 'This is the best'
#
# Return:
#
# 'best the is This'
#
# As part of this exercise you should remove all leading and trailing whitespace. So that inputs such as:
#
# '  space here'  and 'space here      '
#
# both become:
#
# 'here space'

def rev_word(s):

    s= s.strip()
    arr_words = s.split()
    answer = ""

    if len(arr_words) == 1:
        return arr_words[0]

    for num in range(len(arr_words)-1,-1,-1):
        answer += arr_words[num] + " "

    answer = answer.strip()

    return answer

"""
RUN THIS CELL TO TEST YOUR SOLUTION
"""

from nose.tools import assert_equal

class ReversalTest(object):

    def test(self,sol):
        assert_equal(sol('    space before'),'before space')
        assert_equal(sol('space after     '),'after space')
        assert_equal(sol('   Hello John    how are you   '),'you are how John Hello')
        assert_equal(sol('1'),'1')
        print ("ALL TEST CASES PASSED")

# Run and test
t = ReversalTest()
t.test(rev_word)
