from random import choice
from teste import Pessoa

timoteo = Pessoa('Temóteo', 'SENAI', '2 filhos', 'É de Hortolandia', 'Paternal', 'Odeia Python')
lindomar = Pessoa('Lindomar', 'SENAI', 'Arrumou outro emprego recentemente', 'Quer ir para Paulinia', 'Explica mesmo sem saber', 'Beautifulsea')
celso = Pessoa('Celso', 'SENAI', 'Mestre dos hardwares', 'Tem cara de bravo', 'Apoia os projetos doidos', 'É mecanico')
luca = Pessoa('Luca', 'BOSCH', 'Atibaia (entendedores entenderão)', 'Alto', 'Magro', 'Gosta de carros')
clebinho = Pessoa('Clebinho', 'BOSCH', 'Todo mundo gosta', 'Teams tem cara de criança', 'Ensina bem todas as coisas', 'Pediu pra fazer esse jogo')
leo = Pessoa('Léo', 'BOSCH', 'Deve pudim para metade da turma', 'Magro', 'Moreno', 'Ensina JAVA melhor que outras pessoas')

lista = [timoteo, lindomar, celso, luca, clebinho, leo]

x = choice(lista)
x.jogoteste()