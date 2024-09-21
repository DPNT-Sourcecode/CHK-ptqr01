from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_items_no_offers(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('E') == 40
        assert checkout_solution.checkout('F') == 10

    def test_multiple_items_no_offers(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('ABCDE') == 155
        assert checkout_solution.checkout('ABCDEF') == 165

    def test_single_item_offers(self):
        # Offers for A
        assert checkout_solution.checkout('AAA') == 130  # 3 A's for 130
        assert checkout_solution.checkout('AAAAA') == 200  # 5 A's for 200
        assert checkout_solution.checkout('AAAAAA') == 250  # 5 A's for 200 + 1 A's for 50

        # Offers for B
        assert checkout_solution.checkout('BB') == 45  #  2 B's for 45
        assert checkout_solution.checkout('BBB') == 75  #  2 B's for 45 + 1B for 30

        # Offers for F
        assert checkout_solution.checkout('FFF') == 20  # 3 F's for 20
        assert checkout_solution.checkout('FFFF') == 30  # 3 F's for 20 + 1 F for 10
        assert checkout_solution.checkout('FFFFFF') == 40  # 6 F's for 40 (2 sets of 3 for 20 each)

        # Multi-item tests with offers applied
    #     assert checkout_solution.checkout('AA') == 100
    #     
        
    #     
        
        
        
    #     assert checkout_solution.checkout('AAABBBCCCDDD') == 310

    # def test_checkout_with_e(self):
    #     assert checkout_solution.checkout('E') == 40
    #     assert checkout_solution.checkout('EE') == 80
    #     assert checkout_solution.checkout('EEB') == 80  # 2 E's give 1 B free, so no charge for B
    #     assert checkout_solution.checkout('EEBB') == 110  # 2 E's give 1 B free, so charge for 1 B

    # def test_checkout_with_f(self):
    #     assert checkout_solution.checkout('F') == 10
    #     assert checkout_solution.checkout('FF') == 20
    #     

    # def test_checkout_invalid(self):
    #     assert checkout_solution.checkout('AABR') == -1




