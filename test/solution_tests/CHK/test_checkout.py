from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_checkout_valud(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('AA') == 100
        assert checkout_solution.checkout('AAA') == 130
        assert checkout_solution.checkout('AAAA') == 180
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('BB') == 45
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('AAABBBCCCDDD') == 310

    def test_checkout_invalid(self):
        assert checkout_solution.checkout('E') == -1
        assert checkout_solution.checkout('AABR') == -1
