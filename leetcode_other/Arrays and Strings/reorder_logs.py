'''
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.

There are two types of logs:

Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:

The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.

https://leetcode.com/problems/reorder-data-in-log-files/

Note: a re-worded version of this question was given in an Amazon OA
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = dict()
        digit_logs = []
        res = []
        ## separate the letter and digit logs into separate lists
        for i in range(len(logs)):
            log = logs[i].split(' ')
            ## if the log is a letter log
            if (log[1].isalpha()):
                ## save the letter log into a dict where the key is a tuple containing
                ## the identifier as the first element, and the string containing the contents as the second element
                letter_logs[(log[0], ' '.join(log[1:]))] = logs[i]
            else:
                digit_logs.append(logs[i])
        ## sort the letter logs by first comparing the string content (comparing the strings containing the content together
        ## i.e ('18a', 'abc def'), ('17a', 'def fgh'), ('16a', 'abc def')
        ## first compare the strings 'abc def' and 'def fgh', if the content is the same i.e ('abc def', 'abc def'), then compare
        ## the identifier
        sorted_letter_logs = sorted(letter_logs.keys(), key = lambda log : (log[1], log[0]))
        for i in range(len(sorted_letter_logs)):
            res.append(letter_logs[sorted_letter_logs[i]])
        res.extend(digit_logs)
        return res