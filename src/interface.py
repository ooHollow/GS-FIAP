from typing import List, Dict, Tuple

CORES_STATUS: Dict[str, str] = {
    "Normal": "\033[92mNormal\033[0m",
    "Alerta": "\033[93mAlerta\033[0m",
    "Crítico": "\033[91m\033[1mCRÍTICO\033[0m",
    "Dado corrompido": "\033[90mDado corrompido\033[0m"
}

def exibir_menu_selecao(historico_sensores: Dict[str, Tuple[List[int], List[float]]]) -> str:
    print("\n" + "=" * 60)
    print("      \033[96mINTERFACE DE SELEÇÃO DE GRÁFICOS DE TELEMETRIA\033[0m      ")
    print("=" * 60)

    lista_sensores: List[str] = sorted([s for s in historico_sensores.keys() if s != "Desconhecido"])

    if not lista_sensores:
        print("Nenhum sensor válido disponível.")
        return ""

    for idx, nome in enumerate(lista_sensores, start=1):
        print(f"[{idx}] {nome}")
    print("[0] Sair sem gerar gráfico")
    print("=" * 50)

    try:
        opcao: int = int(input("Digite o número do sensor que deseja analisar: "))
        if opcao == 0:
            print("Execução finalizada pelo usuário.")
        elif 1 <= opcao <= len(lista_sensores):
            return lista_sensores[opcao - 1]
        else:
            print("Opção inválida. Seleção cancelada.")
    except ValueError:
        print("Entrada inválida. Digite apenas números inteiros.")

    return ""