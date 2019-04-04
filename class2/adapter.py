#!/usr/bin/env python3

class Player:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(f'{self.name} attack')

    def defense(self):
        print(f'{self.name} defense')


class PlayerTranslator(Player):
    def __init__(self, player, name):
        super().__init__(name)
        self.player = player

    def attack(self):
        self.player.gong_ji()

    def defense(self):
        self.player.fang_shou()


class ChinesePlayer:
    def __init__(self, name):
        self.name = name

    def gong_ji(self):
        print(f'{self.name} 攻擊')

    def fang_shou(self):
        print(f'{self.name} 防守')


if __name__ == '__main__':
    Jeff = Player('Jeff')
    CJ = Player('CJ')
    shiang = PlayerTranslator(ChinesePlayer('香香'))

    Jeff.attack()
    CJ.attack()
    shiang.attack()

    Jeff.defense()
    CJ.defense()
    shiang.defense()
