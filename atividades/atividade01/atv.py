import time

def executarTarefa (tempoDeExecucao):
    print ("Inicializando a Tarefa . . .")

    for i in range(tempoDeExecucao):
        time.sleep(1)
        print(f"Barra de Progressão: {i + 1}/{tempoDeExecucao}")

    print("Tarefa Encerrada")
    print("Saindo . . .")


def main():
    tarefaEmExecussao = executarTarefa(4)

main()