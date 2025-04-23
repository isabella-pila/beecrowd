cod , quant = map(int,input().split())


def switch_case_match_case(cod):
    match cod:
        case 1:
            return (f"Total: R$ {quant * 4.00}")
        case 2:
            return (f"Total: R$ {quant * 4.50}")
        case 3:
            return (f"Total: R$ {quant * 5.00}")
        case 4:
            return (f"Total: R$ {quant * 2.00}")
        case 5:
            return (f"Total: R$ {quant * 1.50}")


resultado = switch_case_match_case(cod)
print(resultado)
