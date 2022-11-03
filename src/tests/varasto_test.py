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

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays(self):
        self.varasto.lisaa_varastoon(-1)
        # Mikään ei muutu
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_lisaa_liikaa(self):
        self.varasto.lisaa_varastoon(11)
        # varasto on nyt täynnä
        self.assertAlmostEqual(self.varasto.saldo, 10)
    
    def test_otetaan_negatiivinen(self):
        otettu = self.varasto.ota_varastosta(-3)
        self.assertAlmostEqual(otettu, 0)
    
    def test_ei_oteta_enempaa_kuin_voi(self):
        self.varasto.lisaa_varastoon(8)
        otettu = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(otettu, 8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)
    
    def test_merkkijonoesitys(self):
        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(
            self.varasto.__str__(),
            "saldo = 6, vielä tilaa 4"
        )
    
    def test_luodaan_varasto_negatiivisella_tilavuudella(self):
        toinen_varasto = Varasto(-1)
        self.assertAlmostEqual(toinen_varasto.tilavuus, 0)
    
    def test_negatiivinen_alku_saldo(self):
        toinen_varasto = Varasto(5, -1)
        self.assertAlmostEqual(toinen_varasto.saldo, 0)