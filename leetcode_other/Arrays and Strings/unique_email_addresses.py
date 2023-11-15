"""
https://leetcode.com/problems/unique-email-addresses/
"""
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """
        Concepts:
        Parsing
        - there's guaranteed to only be one @ symbol in the email, so we can split
            the email into two parts using split("@")
        - under local name (which is split("@")[0]):
            - remove all periods
            - iterating from 0 ... len(local name), if a "+" is found, only take characters before the "+" sign
            
        """
        emailSet = set()
        for i in range(len(emails)):
            localName, domainName = emails[i].split("@")
            firstPlus = 0
            localName = localName.replace(".", "")
            for j in range(len(localName)):
                if localName[j] == "+":
                    firstPlus = j
                    break
            # remove all periods and take everything up to the first plus sign
            if firstPlus != 0:
                localName = localName[:firstPlus]
            
            emailSet.add(f"{localName}@{domainName}")
        return len(emailSet)
            