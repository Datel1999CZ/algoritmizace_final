import random

class ChicagoHra:
    def __init__(self, hraci):
        self.hraci = hraci
        self.skore = {hrac: 0 for hrac in hraci}
        self.kola = 7

    def hod_kostkami(self, pocet_kostek):
        return [random.randint(1, 6) for _ in range(pocet_kostek)]

    def vypocitej_skore(self, kostky):
        skore = 0
        for kostka in kostky:
            if kostka == 1:
                skore += 100
            elif kostka == 6:
                skore += 60
            else:
                skore += kostka
        return skore

    def hraj_kolo(self, hrac):
        print(f"\n{hrac} má tah:")
        kostky = self.hod_kostkami(3)
        print(f"Hod 1: {kostky}")

        for hod in range(2, 4):
            ponechat_kostky = input(f"Které kostky ponechat (1-3, oddělené mezerami) nebo 'vse' pro ponechání všech: ")
            if ponechat_kostky.lower() == 'vse':
                break

            ponechane_indexy = [int(x) - 1 for x in ponechat_kostky.split()]
            nove_kostky = self.hod_kostkami(3 - len(ponechane_indexy))
            kostky = [kostky[i] for i in ponechane_indexy] + nove_kostky
            print(f"Hod {hod}: {kostky}")

        skore = self.vypocitej_skore(kostky)
        self.skore[hrac] += skore
        print(f"{hrac} získal {skore} bodů v tomto kole.")

    def hraj_hru(self):
        for kolo in range(1, self.kola + 1):
            print(f"\nZačíná kolo {kolo}!")
            for hrac in self.hraci:
                self.hraj_kolo(hrac)

        print("\nHra skončila! Konečné skóre:")
        for hrac, skore in self.skore.items():
            print(f"{hrac}: {skore} bodů")

        vitez = max(self.skore, key=self.skore.get)
        print(f"\n{vitez} vyhrává hru!")

if __name__ == "__main__":
    hraci = input("Zadejte jména hráčů (oddělená čárkami): ").split(',')
    hra = ChicagoHra([hrac.strip() for hrac in hraci])
    hra.hraj_hru()
