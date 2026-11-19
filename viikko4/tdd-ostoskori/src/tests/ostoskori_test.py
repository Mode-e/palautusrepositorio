import unittest

from ostoskori import Ostoskori
from tuote import Tuote


class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaaminen_koriin(self):
        tuote = Tuote("maito", 3)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteen_hinta(
        self,
    ):
        tuote = Tuote("maito", 3)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(
        self,
    ):
        tuote1 = Tuote("maito", 3)
        tuote2 = Tuote("juusto", 5)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(
        self,
    ):
        tuote1 = Tuote("maito", 3)
        tuote2 = Tuote("juusto", 5)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_kaksi_tavaraa(
        self,
    ):
        tuote1 = Tuote("maito", 3)
        tuote2 = Tuote("maito", 3)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_on_sama_kuin_tuotteiden_hintojen_summa(
        self,
    ):
        tuote1 = Tuote("maito", 3)
        tuote2 = Tuote("maito", 3)
        self.kori.lisaa_tuote(tuote1)
        self.kori.lisaa_tuote(tuote2)
        self.assertEqual(self.kori.hinta(), 6)

    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorissa_on_yksi_ostos(self):
        tuote = Tuote("maito", 3)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(len(self.kori.ostokset()), 1)
