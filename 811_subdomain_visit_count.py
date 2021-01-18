from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        if not cpdomains:
            return []
        result = []
        visit_map = dict()

        for visit_log in cpdomains:
            hits, address = visit_log.split(' ')
            subdomains = address.split('.')
            hits = int(hits)
            for sd_idx in range(len(subdomains) - 1, -1, -1):
                subdomain = '.'.join(subdomains[sd_idx:])
                if subdomain not in visit_map:
                    visit_map[subdomain] = 0
                visit_map[subdomain] += hits

        for key, value in visit_map.items():
            result.append(str(value) + " " + key)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]))
