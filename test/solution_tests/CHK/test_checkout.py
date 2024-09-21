from lib.solutions.CHK import checkout_solution


class TestCheckout():
    def test_single_items_no_offers(self):
        assert checkout_solution.checkout('A') == 50
        assert checkout_solution.checkout('B') == 30
        assert checkout_solution.checkout('C') == 20
        assert checkout_solution.checkout('D') == 15
        assert checkout_solution.checkout('E') == 40
        assert checkout_solution.checkout('F') == 10
        assert checkout_solution.checkout('G') == 20
        assert checkout_solution.checkout('Z') == 21

    def test_multiple_items_no_offers(self):
        assert checkout_solution.checkout('ABCD') == 115
        assert checkout_solution.checkout('ABCDE') == 155
        assert checkout_solution.checkout('ABCDEF') == 165
        assert checkout_solution.checkout('ABCDEFG') == 185
        assert checkout_solution.checkout('XYZ') == 45


    # def test_single_item_offers(self):
    #     # Offers for A
    #     assert checkout_solution.checkout('AAA') == 130  # 3 A's for 130
    #     assert checkout_solution.checkout('AAAAA') == 200  # 5 A's for 200
    #     assert checkout_solution.checkout('AAAAAA') == 250  # 5 A's for 200 + 1 A's for 50

    #     # Offers for B
    #     assert checkout_solution.checkout('BB') == 45  #  2 B's for 45
    #     assert checkout_solution.checkout('BBB') == 75  #  2 B's for 45 + 1B for 30

    #     # Offers for F
    #     assert checkout_solution.checkout('FFF') == 20  # 3 F's for 20
    #     assert checkout_solution.checkout('FFFF') == 30  # 3 F's for 20 + 1 F for 10
    #     assert checkout_solution.checkout('FFFFFF') == 40  # 6 F's for 40 (2 sets of 3 for 20 each)

    #     # Offers for H
    #     assert checkout_solution.checkout('HHHHH') == 45  # 5 H's for 45
    #     assert checkout_solution.checkout('HHHHHHHHHH') == 80  # 10 H's for 80
    #     assert checkout_solution.checkout('HHHHHHHHHHH') == 90  # 10 H's for 80 + 1 H for 10

    # def test_combined_item_offers(self):
    #     # Combined offers for A and B
    #     assert checkout_solution.checkout('AABBB') == 175  #  2 A's for 100 + 2 B's for 45 + 1 B for 30
    #     assert checkout_solution.checkout('AAAAABBB') == 275  #  5 A's for 200 + 2 B's for 45 + 1 B for 30

    #     # Combined offers for A, E and B
    #     assert checkout_solution.checkout('AAAEEBB') == 240  #  3 A's for 130 + 2 E's for 80 + 1 B free + 1 B for 30
    #     assert checkout_solution.checkout('AAAAEEBB') == 290  #  3 A's for 130 + 1 A for 50 + 2 E's for 80 + 1 B free + 1 B for 30

    #     # Combined offers for A, E and F
    #     assert checkout_solution.checkout('AEEFFF') == 150  # 1 A for 50 + 2 E's for 80 + 3 F's for 20
    #     assert checkout_solution.checkout('AAABBBEEFFF') == 275  #  3 A's for 130 + 2 B's for 45 + 1 B free + 2 E's for 80 + 3 F's for 20

    #     # Combined offers with H
    #     assert checkout_solution.checkout('HHHHHAAAAA') == 245  # 5 H's for 45 + 5 A's for 200
    #     assert checkout_solution.checkout('HHHHHHHHHHFFFFF') == 120  #  10 H's for 80 + 5 F's for 40

    # def test_offer_for_e_and_b(self):
    #     assert checkout_solution.checkout('EE') == 80  # 2 E's with no B
    #     assert checkout_solution.checkout('EEB') == 80  # 2 E's gives 1 B for free
    #     assert checkout_solution.checkout('EEBB') == 110  # 2 E's gives 1 B for free + 1 B charged

    # def test_offer_for_r_and_q(self):
    #     assert checkout_solution.checkout('RRR') == 150  # 3 R's with no Q
    #     assert checkout_solution.checkout('RRRQ') == 150  # 3 R's give 1 Q for free
    #     assert checkout_solution.checkout('RRRRQQQ') == 260  # 3 R's give 1 Q for free, 3 Q's for 80 + 1 R for 50

    # def test_offer_for_n_and_m(self):
    #     assert checkout_solution.checkout('NNNM') == 120  # 3 N's give 1 M for free, no charge for M
    #     assert checkout_solution.checkout('NNNNM') == 160  # 3 N's give 1 M for free, no charge for M + 1 N
    #     assert checkout_solution.checkout('NNNNNNMM') == 240  # 6 N's give 2 M's for free, no charge for M

    # def test_invalid_skus(self):
    #     assert checkout_solution.checkout('123') == -1
    #     assert checkout_solution.checkout('-!@') == -1

    # def test_empty_basket(self):
    #     assert checkout_solution.checkout('') == 0

    # def test_basket_with_all_skus(self):
    #     assert checkout_solution.checkout('ABCDEFGHIJKLOMNPQRSTUVWXYZ') == 965



