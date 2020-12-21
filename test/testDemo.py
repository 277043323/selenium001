
from automationcodejiang.login.main import test


class Test:
    def setup(self):
        self.main  = test()

    def test(self):
        self.main.Main().deng().couser().action()
