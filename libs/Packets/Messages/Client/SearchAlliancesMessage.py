from Utils.Reader import Reader
from Logic.Player import Player

class SearchAlliancesMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.readString()