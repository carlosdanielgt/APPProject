from strategy import Strategy
from ast import List


class ClientTypeDiscount(Strategy):
    def do_algorithm(self, data: List):
        return sorted(data)
