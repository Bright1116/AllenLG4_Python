#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/10/24 22:32
# FileName: task_02.py

"""
作业2
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，

1、see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“师弟是我的！”，如果传入“丁春秋”，打印“叛徒！我杀了你”

2、fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。

* 定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
* 加入模块化改造
希望各位同学在此基础上可以添加自己的“freestyle”哦
"""


class TongLao:
    def __init__(self, blood_volume, force_value):
        self.blood_volume = blood_volume  # 血量
        self.force_value = force_value  # 武力值

    def see_people(self, name):
        if name == "WYZ":
            print("师弟！！！！")
        elif name == "李秋水":
            print("师弟是我的！")
        elif name == "丁春秋":
            print("叛徒！我杀了你")
        else:
            print("对不起，您选择的角色暂不支持识别！")

    def fight_zms(self, hp, power):
        """

        :param hp: 敌人的血量
        :param power: 敌人的武力值
        :return:
        """
        self.force_value *= 10
        self.blood_volume /= 2
        self.blood_volume -= power
        hp -= self.force_value
        print(f"我的血量{self.blood_volume}，武力值{self.force_value}")
        print(f"敌人的血量{hp}，武力值{power}")
        if self.blood_volume > hp:
            print("我赢了！")
        elif self.blood_volume == hp:
            print("平局！")
        else:
            print("我输了！")


class XuZhu(TongLao):
    def see_people(self, name):
        if name == "虚竹":
            print("虚竹宅心仁厚不想打架")
        else:
            print("对不起，您选择的角色暂不支持识别！")

    @staticmethod
    def read():
        print("罪过罪过!")


if __name__ == '__main__':
    TongLao(1000, 30).fight_zms(600, 70)
    XuZhu(1000, 30).see_people("虚竹")
