from Utils.Reader import Reader
from Logic.Player import Player
from Packets.Messages.Server.NpcDataMessage import *


class AttackNpcMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        self.readInt()

    def process(self):
        NpcDataMessage(self.device).Send()