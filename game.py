import random

class Character:
    def __init__(self, name, hp, attack):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0


class Hero(Character):
    def holy_blade(self, enemy):
        dmg = random.randint(self.attack - 3, self.attack + 3)
        enemy.hp -= dmg
        return f"🗡 Holy Blade deals {dmg} damage"

    def frost_dominion(self, enemy):
        dmg = random.randint(self.attack - 6, self.attack - 1)
        enemy.hp -= dmg
        enemy.attack = max(6, enemy.attack - 4)
        return f"❄ Frost Dominion freezes Devil (-ATK), damage {dmg}"

    def inferno_cataclysm(self, enemy):
        dmg = random.randint(self.attack + 10, self.attack + 20)
        recoil = random.randint(5, 12)
        enemy.hp -= dmg
        self.hp -= recoil
        return f"🔥 INFERNO! {dmg} damage dealt (Hero takes {recoil})"


class Devil(Character):
    def attack_enemy(self, enemy):
        dmg = random.randint(self.attack - 4, self.attack + 4)
        enemy.hp -= dmg
        return f"😈 Devil strikes for {dmg} damage"
