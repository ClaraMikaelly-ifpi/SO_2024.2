#Criar um programa em qualquer linguagem de programação que implemente três ou
#mais threads e que mostre a execução simultânea delas.

import threading;
import time;

#Função para cada thread executar
def contagem(nome, delay, contagem):
    for i in range(1, contagem + 1):
        time.sleep(delay)
        print(f"{nome} - contagem {i}")


# Criando três threads
thread1 = threading.Thread(target = contagem, args=("Thread 1", 1,5))
thread2 = threading.Thread(target = contagem, args=("Thread 2", 0.5, 7))
thread3 = threading.Thread(target = contagem, args=("Thread 3", 1.5, 3))

#Inicializando as threads
thread1.start()
thread2.start()
thread3.start()

#Aguardando todas as threads terminarem
thread1.join()
thread2.join()
thread3.join()

print("Todas as threads foram concluídas!")