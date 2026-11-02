from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    mehua.lisaa_varastoon(50.7)
    mehua.ota_varastosta(3.14)
    huono = Varasto(-100.0)
    huono = Varasto(100.0, -50.7)
    print(f"{huono}\nOlutvarasto: {olutta}\nolutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}\nOlutvarasto: {olutta}\nolutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    saatiin = mehua.ota_varastosta(-32.9)
    print(saatiin)
    a = 0
    if True:
        if True:
            if True:
                a = 1
    aa = 1
    aaa = 1
    aaaa = 1
    aaaaa = 1
    aaaaaa = 1
    aaaaaaa = 1
    aaaaaaaa = 1
    aaaaaaaaa = 1
    aaaaaaaaaa = 1
    aaaaaaaaaaa = 1
    print(
        a,
        aa,
        aaa,
        aaaa,
        aaaaa,
        aaaaaa,
        aaaaaaa,
        aaaaaaaa,
        aaaaaaaaa,
        aaaaaaaaaa,
        aaaaaaaaaaa,
    )

def bad_indentation():
   print("a")

if __name__ == "__main__":
    main()
