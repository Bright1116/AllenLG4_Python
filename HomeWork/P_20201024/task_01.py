#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Author  : Allen Bright
# Time    : 2020/10/24 22:27
# FileName: task_01.py

"""
作业1
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个。
"""


# 1、封装一个狗类
class Dog:
    def __init__(self, name, kind, place):
        """

        :param name: 狗的名字
        :param kind: 狗的品种
        :param place: 原产地
        """
        self.name = name
        self.kind = kind
        self.place = place

    # 吃 - 方法
    def eat(self, weight):
        print(f"{self.name}，原产地：{self.place}，属于{self.kind}，它吃了{weight}斤的狗粮！")

    # 睡觉 - 方法
    def sleep(self):
        print(f"{self.name}，喜欢睡觉！")


# 2、封装一个水果类
class BuyFruit:
    def __init__(self, name, discount):
        """

        :param name: 水果名
        :param discount: 折扣
        """
        self.name = name
        self.discount = discount

    # 购买水果
    def buy(self):
        print(f"{self.name}, 今日打{self.discount}折。")


# 3、学生类，计算分数
class Student:
    def __init__(self, name, age, gender, **score):
        """

        :param name: 姓名
        :param age: 年龄
        :param gender: 性别
        :param score: 每门课的成绩，字典形式
        """
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score

    def total_score(self):
        TotalScore = 0
        # 计算总分
        try:
            for i in self.score.values():
                TotalScore += i
        except Exception:
            return "计算总分异常！"
        return TotalScore

    def average_score(self):
        # 计算平均分
        try:
            AverageScore = self.total_score() / len(self.score.keys())
        except Exception:
            return "计算平均分异常！"
        return AverageScore

    def person_information(self):
        Inf = f"我的名字叫{self.name}，年龄：{self.age},性别：{self.gender}。"
        return Inf


# 4、定义一个用例类，执行用例
class Case:
    user = "allen"
    passwd = "888888"

    def __init__(self, name, user, passwd, expected):
        self.case_name = name
        self.case_user = user
        self.case_passwd = passwd
        self.case_expected = expected
        self.case_actual = None

    def run_case(self):
        print(f"运行测试用例：{self.case_name}")
        if self.user == self.case_user and self.passwd == self.case_passwd:
            self.case_actual = "登陆成功"
            return self.case_actual
        else:
            self.case_actual = "登陆失败"
            return self.case_actual

    def case_is_passed(self):
        if self.run_case() == self.case_expected:
            print('用例通过')
        else:
            print("用例失败")


# 5、定义一个笔类
class Bi:
    def __init__(self, name, function):
        self.name = name
        self.function = function

    def writing(self):
        print(f"{self.name}，可以用来{self.function}。")


if __name__ == '__main__':
    # 狗类
    Dog("哈士奇", "西伯利亚雪橇犬", "俄罗斯西伯利亚地区").eat(3)

    # 买水果
    BuyFruit("哈密瓜", 8).buy()

    # 学生信息
    student = [{"stu_name": "Bright", "stu_age": 18, "stu_gender": "男",
                "stu_score": {"English": 90, "math": 120, "Chinese": 135}}]
    for stu in student:
        Stu_1 = Student(stu["stu_name"], stu["stu_age"], stu["stu_gender"], **(stu["stu_score"]))
        print(f"个人信息：{Stu_1.person_information()}总分：{Stu_1.total_score()}")

    # 执行用例
    Case("正常登陆", "allen", "888888", "登陆成功").case_is_passed()

    # 水彩笔写字
    Bi("水彩笔", "画画").writing()


