import unittest

from utilities.lcm import least_common_multiple


class TestLCM(unittest.TestCase):
    def setUp(self):
        self.small_number_1 = 4
        self.small_number_2 = 6
        self.large_number_1 = 1111111111111111111111111111119472389472389812209381902549018238910248121298371859122609131298371829398712981725981274982474623455287328934782374293847892343223423423423908899878000000012391203462352376656782365782346283746238746238761267516275126514526115624516256127616786871263781264387182764128764904819204
        self.large_number_2 = 2378492839472983472389472389472389812209381902549018238910248121298371859122609131298371829398712981725981274982474623455287328934782374293847892343223423423423908899878000000012391203462352376656782365782346283746238746238761267516275126514526115624516256127616786871263781264387182764128764904819209
        pass

    def test_lcm_works_with_small_numbers(self):
        self.assertEqual(least_common_multiple(
            self.small_number_1, self.small_number_2), 12)

    def test_lcm_works_with_large_numbers(self):
        expectedResult = 2642769821636648302654969321655875920943788350306189113419054975939127279050281997899110019534886602435597539002175314416236165327862432310159392334485885555632151322794030885873853391938677141658392700365850875720907839316849593549602746493558448371847253808920002920223493584020604706446188664177517504946490201029089769979122460402533405446933383348621282768685423443023435884467912269439839280951509286030442342135503118832613010416672054112627697545491783621134736684278939999866662305559007500527531612955251398592262679962688134991052384628507202601611073274262819218213763618806986626631309328451289636
        self.assertEqual(least_common_multiple(
            self.large_number_1, self.large_number_2), expectedResult)
