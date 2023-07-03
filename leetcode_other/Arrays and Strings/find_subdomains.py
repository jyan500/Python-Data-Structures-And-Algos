"""
https://leetcode.com/problems/subdomain-visit-count/
"""
class Solution:        
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = dict()
        result = []
        for i in range(len(cpdomains)):
            count, domain = cpdomains[i].split(" ")
            count = int(count)
            frags = domain.split(".")
            """
            build the subdomain from the fragments
            i.e google.mail.com, frags = [google, mail, com]
            ".".join([google, mail, com]) = google.mail.com
            ".".join([mail, com]) = mail.com
            ".".join([com]) = com
            """
            for i in range(len(frags)):
                subdomain = ".".join(frags[i: ])
                if subdomain in counts:
                    counts[subdomain] += count
                else:
                    counts[subdomain] = count
            
        for subdomain in counts:
            count = counts[subdomain]
            result.append(f"{count} {subdomain}")
        return result
