import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_uudella_varastolla_tilavuus_0_jos_ei_anneta(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0.0)

    def test_uudella_varastolla_oikea_alku_saldo(self):
        varasto = Varasto(1, -1)
        self.assertEqual(varasto.saldo, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_yli_tilavuuden_paatyy_tayteen_tilavuuteen(self):
        self.varasto.lisaa_varastoon(8)
        #pitäisi olla vapaata tilaa 2
        self.assertEqual(self.varasto.paljonko_mahtuu(), 2)

        self.varasto.lisaa_varastoon(5)
        
        self.assertEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertEqual(self.varasto.saldo, 10)

    def test_jos_lisayksen_maara_vahemman_kuin_0(self):
        #lisätään saldoon 5
        self.varasto.lisaa_varastoon(5)
        alku_saldo = self.varasto.saldo

        #saldon ei pitäisi muuttua kun lisätään -1
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, alku_saldo)

    def test_otetaan_varastosta_vahemman_kuin_0(self):
        #lisätään saldoon 5
        self.varasto.lisaa_varastoon(5)
        alku_saldo = self.varasto.saldo

        #saldon ei pitäisi muuttua kun otetaan -1
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, alku_saldo)

    def test_otetaan_kaikki_mita_voi(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(self.varasto.ota_varastosta(10), 5)
        self.assertEqual(self.varasto.saldo, 0)



    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tarkista_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(5)

        self.assertEqual(str(self.varasto), "saldo = 5, vielä tilaa 5")

