import pytest
import allure

from HomeWork.P_20201027.core.calc import Calc


@allure.feature("calc.py模块测试用例")
class TestCalc:
    def setup_class(self):
        self.calc = Calc()

    def setup(self):
        pass

    @allure.story("整数相乘")
    @pytest.mark.parametrize("a, b, c", [
        [1, 2, 2],
        [-1, -1, 1],
        [1, -1, -1],
    ])
    def test_mul_int(self, a, b, c):
        assert self.calc.mul(a, b) == c

    @allure.story("浮点数相乘")
    @pytest.mark.parametrize("a, b, c", [
        [1.2, 2, 2.4],
        [3, 3.6, 10.8],
        [2.5, 3.4, 8.5],
        [3.25, 3.7, 12.025],
        [6.5, 6.37, 41.405],
        [3.14, 2.18, 6.8452],
        [6.336, 6.28, 39.79008]
    ])
    def test_mul_float(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # 正常值例子
    @allure.story("两个正整数相除")
    @pytest.mark.parametrize("a, b, c", [
        [2, 2, 1],
        [4, 3, 1.333333333333333],
        [3, 6, 0.5]
    ])
    def test_div_int(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 正常值例子
    @allure.story("带有小数位相除")
    @pytest.mark.parametrize("a, b, c", [
        [2.3, 2, 1.15],
        [4, 3.2, 1.25],
        [6.5, 3.2, 2.03125]
    ])
    def test_div_float(self, a, b, c):
        assert self.calc.div(a, b) == c

    # 异常值例子
    @allure.story("除数等于0")
    @pytest.mark.parametrize("a, b", [
        [2, 0],
        [0.2, 0],
        [0, 0]
    ])
    def test_div_by_zero(self, a, b):
        with pytest.raises(Exception):
            assert self.calc.div(a, b)

    # 流程示例
    def test_process(self):
        r1 = self.calc.mul(1, 2)
        r2 = self.calc.div(2, 1)
        assert r1 == 2
        assert r2 == 2