class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        list_sentence = sentence.split(" ")
        for i in range(len(list_sentence)):
            item = list_sentence[i]
            if item.startswith('$') and item[1:].isdigit():
                price = float(item[1:])
                discounted_price = price * (1 - discount / 100)
                list_sentence[i] = f'${discounted_price:.2f}'
        
        return ' '.join(list_sentence)
                