import os
import time
os.system('cls')
class Carro():
    def __init__(self, nome, marca, modelo):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
    def Visualizarcarros(self):
        print(f'Nome: {self.nome:<15} Marca: {self.marca:<15} Modelo: {self.modelo:<15}')
Novocarro = [Carro('Siena', 'Fiat', 'Sedan'), Carro('Corola', 'Toyota', 'Sedan'), 
             Carro('HRV', 'Honda', 'SUV'), Carro('Civic', 'Honda', 'Sedan')]
while True:
    print('Escolha uma opção abaixo\n[1] Cadastrar novo carro\n[2] Visualizar carros cadastrados\n[3] Sair')
    escolha = input('Digite: ')
    if escolha == '1':
        os.system('cls')
        CarroNovo = Carro(nome=input('Nome: '), marca=input('Marca: '), modelo=input('Modelo: '))
        Novocarro.append(CarroNovo)
        print('\nCadastrando', end='')
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('\nCarro Cadastrado!')
        time.sleep(2)
        os.system('cls')
    elif escolha == '2':
        os.system('cls')
        print('Imprimindo Registros', end='')
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print('.', end='', flush=True)
        time.sleep(1)
        print()
        for i in Novocarro:
            i.Visualizarcarros()
            time.sleep(0.5)
        print()
    elif escolha == '3':
        print('\nPrograma Encerrado\n')
        break
    else:
        os.system('cls')
        print('Escolha Inválida\n')
