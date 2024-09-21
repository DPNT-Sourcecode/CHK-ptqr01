from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_valud(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('AA') == 100
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('B') == 30