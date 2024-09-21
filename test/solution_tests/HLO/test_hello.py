from lib.solutions.HLO import hello_solution


class TestHello():
    def test_hello_world(self):
        assert hello_solution.hello('any_name') == 'Hello, World!'

    def test_hello_friend(self):
        assert hello_solution.hello('John') == 'Hello, John!'

