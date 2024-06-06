class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)
        sorted_cards = sorted(card_count.keys())

        for card in sorted_cards:
            if card_count[card] > 0:
                count = card_count[card]
                for i in range(groupSize):
                    if card_count[card + i] < count:
                        return False
                    card_count[card + i] -= count

        return True