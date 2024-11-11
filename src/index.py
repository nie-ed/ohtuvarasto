from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    #Luonnin jälkeen:
    print(f"Mehuvarasto: {mehua}, Olutvarasto: {olutta}")
    #Mehu setterit:, Lisätään 50.7
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}, Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    #Virhetilanteita: Varasto(-100.0)
    print(Varasto(-100.0))

    #Varasto(100.0, -50.7)
    print(Varasto(100.0, -50.7))

    print(f"Olutvarasto: {olutta}, olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

   #mehua.lisaa_varastoon(-666.0)
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
