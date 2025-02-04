from Utils.Reader import Reader
from Packets.Messages.Server.Avatar.AvatarStreamMessage import *


class AskForAvatarStreamMessage(Reader):

    def __init__(self, data, device):
        super().__init__(data)
        self.device = device

    def decode(self):
        pass

    def process(self):
        AvatarStreamMessage(self.device).Send()