#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/10/20 22:34
# FileName: game_fun.py

"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，
hp的初始值为1000，power的初始值为200。
定义一个fight方法：
my_final_hp = my_hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
"""

import random


def fight(p_enemy_hp, p_enemy_power):
    """

    :param p_enemy_hp: 敌人的血量
    :param p_enemy_power: 敌人的攻击力
    :return:
    """
    # 定义4个变量存放数据
    my_hp = 1000  # 我的血量
    my_power = 1030  # 我的攻击力

    # 打印敌人的血量和攻击力
    print(f"敌人的血量为：{p_enemy_hp}，攻击力为：{p_enemy_power}")

    # 加入循环，让游戏可以进行多轮
    while True:
        my_hp -= p_enemy_power
        p_enemy_hp -= my_power

        # 判断谁的血量小于等于0
        if my_hp <= 0 or p_enemy_hp > 0:
            # 打印我和敌人的剩余血量
            print(f"我的剩余血量为：{my_hp}")
            print(f"敌人的剩余血量为：{p_enemy_hp}")
            print("我输了")
            # 满足条件跳出循环
            break
        elif my_hp > 0 and p_enemy_hp <= 0:
            print(f"我的剩余血量为：{my_hp}")
            print(f"敌人的剩余血量为：{p_enemy_hp}")
            print("我赢了")
            break
        else:
            print(f"我的剩余血量为：{my_hp}")
            print(f"敌人的剩余血量为：{p_enemy_hp}")
            break


if __name__ == "__main__":
    # 利用列表推导式生成hp
    hp = [x for x in range(990, 1010)]
    # print(hp)
    # print(type(hp))
    # 让敌人的hp从hp列表中随机挑选一个值
    # 自动导包：alt+回车
    enemy_hp = random.choice(hp)
    # print(enemy_hp)

    # 敌人的攻击力用randint方法生成随机整数
    enemy_power = random.randint(190, 210)
    # print(enemy_power)

    # 调用函数，传入敌人的hp和power
    fight(enemy_hp, enemy_power)
