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

    def test_combined_item_offers(self):
        # Combined offers for A and B
        assert checkout_solution.checkout('AABBB') == 175  #  2 A's for 100 + 2 B's for 45 + 1 B for 30
        assert checkout_solution.checkout('AAAAABBB') == 275  #  5 A's for 200 + 2 B's for 45 + 1 B for 30

        # Combined offers for A, E and B
        assert checkout_solution.checkout('AAAEEBB') == 240  #  3 A's for 130 + 2 E's for 80 + 1 B free + 1 B for 30
        assert checkout_solution.checkout('AAAAEEBB') == 290  #  3 A's for 130 + 1 A for 50 + 2 E's for 80 + 1 B free + 1 B for 30

        # Combined offers for A, E and F
        assert checkout_solution.checkout('AEEFFF') == 150  # 1 A for 50 + 2 E's for 80 + 3 F's for 20
        assert checkout_solution.checkout('AAABBBEEFFF') == 275  #  3 A's for 130 + 2 B's for 45 + 1 B free + 2 E's for 80 + 3 F's for 20

    def test_offer_for_e_and_b(self):
        assert checkout_solution.checkout('EE') == 80  # 2 E's with no B
        assert checkout_solution.checkout('EEB') == 80  # 2 E's gives 1 B for free
        assert checkout_solution.checkout('EEBB') == 110  # 2 E's gives 1 B for free + 1 B charged

    def test_invalid_skus(self):
        assert checkout_solution.checkout('AABR') == -1
        assert checkout_solution.checkout('YYY') == -1
        assert checkout_solution.checkout('123') == -1
