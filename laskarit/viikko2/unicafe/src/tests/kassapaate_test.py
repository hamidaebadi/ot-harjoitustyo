import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_rahamaara_kassalla_alussa_1000(self):
        raha_euroissa = round(self.kassapaate.kassassa_rahaa/100, 2)
        self.assertEqual(raha_euroissa, 1000)

    def test_edullisten_maara_alussa_nolla(self):
        edullisten_maara = self.kassapaate.edulliset
        self.assertEqual(edullisten_maara, 0)

    #käteisosto testit
    #testataan kassarahan ja myytyjen lounaiden määrä
    #kun maksu riittää
    def test_maukkaiden_maara_alussa_nolla(self):
        maukkaiden_maara = self.kassapaate.maukkaat
        self.assertEqual(maukkaiden_maara, 0)

    def test_syo_edullisesti_kateisella_on_oikein_riitavalla_maksulla(self):
        vaihto_raha = self.kassapaate.syo_edullisesti_kateisella(240)
        uusi_kassa_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(uusi_kassa_saldo, 100000+240)
        self.assertEqual(vaihto_raha, 0)

    def test_syo_maukkaasti_kateisella_on_oikein_riitavalla_maksulla(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(400)
        uusi_kassa_saldo = self.kassapaate.kassassa_rahaa
        self.assertEqual(uusi_kassa_saldo, 100000+400)
        self.assertEqual(vaihtoraha, 0)

    def test_myytydyt_lounaat_kasvaa_riitavalla_maksulla(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        edullisten_maara = self.kassapaate.edulliset
        maukkaiden_maara = self.kassapaate.maukkaat
        self.assertEqual(edullisten_maara, 1)
        self.assertEqual(edullisten_maara, 1)
    #kun maksu ei riitä
    #kassa oleva raha määrä ei muutu
    def test_kassaraha_ei_muutu_kun_ei_riittava_maksu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    #edullisten lounaiden määrä ei kasva, kun ei ole riittävästi maksua
    def test_myydyt_edulliset_ei_muutu_ei_riittava_maksua(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    #maukkaiden lounaiden määrä ei muutu, kun ei ole riittävästi maksua
    def test_myydyt_maukkaat_ei_muutu_kun_ei_riittavasti_maksua(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #Korttiosto toimii sekä edullisten että maukkaiden lounaiden osalta
    def test_syo_edullisesti_kortilla_palauttaa_true(self):
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)

    def test_syo_maukkaasti_kortilla_palauttaa_true(self):
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(vastaus, True)

    def test_edullisesti_kortilla_kasvattaa_lounaiden_maara(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkasti_kortilla_kasvattaa_lounaiden_maara(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    #Kortilla ei ole riittävästi saldoa
    def test_maukkaiden_maara_ei_muutu_ei_saldoa_kortilla(self):
        self.maksukortti.ota_rahaa(800)
        vastaus = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(vastaus, False)
    
    def test_edullisten_maara_ei_muutu_ei_saldoa_kortilla(self):
        self.maksukortti.ota_rahaa(800)
        vastaus = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(vastaus, False)

    def test_kassaraha_ei_muutu_kortilla_ostettua(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_kortti_kassalla_muuttaa_kassarahaa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        kassa_raha = self.kassapaate.kassassa_rahaa
        self.assertEqual(kassa_raha, 101000)
    
    def test_lataaminen_ei_onnistu_negatiivisella_summalla(self):
        vastaus = self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -1000)
        self.assertEqual(vastaus, False)

    
    
