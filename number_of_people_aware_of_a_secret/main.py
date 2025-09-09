class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        know = [(1, 1)]
        share = []

        know_count = 1
        share_count = 0

        for i in range(2, n+1):
            if know and know[0][0] == i - delay:
                know_count -= know[0][1]
                share_count += know[0][1]
                share.append(know[0])
                know.pop(0)

            if share and share[0][0] == i - forget:
                share_count -= share[0][1]
                share.pop(0)

            if share:
                know_count += share_count
                know.append((i, share_count))

        return (know_count + share_count) % (10 ** 9 + 7)

