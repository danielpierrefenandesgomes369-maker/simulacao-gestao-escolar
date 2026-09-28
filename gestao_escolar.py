alunos = [
    {"nome" : "João Nicodemus" , "notas" : [8.0,7.0,9.0] , "aulas_assistidas" : 38 , "total_de_aulas" : 40},
    {"nome" : "Noemi Santos" , "notas" : [7.5,8.0,2.0] , "aulas_assistidas" : 37 , "total_de_aulas" : 40},
  {"nome" : "Abdnego Matos" , "notas" : [6.0,8.0,3.0] , "aulas_assistidas" : 34 , "total_de_aulas" : 40},
  {"nome" : "Jezabel Moura" , "notas" : [5.0,3.0,6.0] , "aulas_assistidas" : 25 , "total_de_aulas" : 40},
  {"nome" : "Estevão Silva" , "notas" : [2.0,0.5,9.0] , "aulas_assistidas" : 38 , "total_de_aulas" : 40},
]

aprovados = 0

for aluno in alunos:
    media = round(sum(aluno["notas"]) / len(aluno["notas"]), 2)
    frequencia = round((aluno["aulas_assistidas"]/aluno["total_de_aulas"]), 2)
    if frequencia < 0.75:
        situaçao = "Reprovado por falta"
    elif media >= 7:
        situaçao = "Aprovado"
    elif media >= 4:
        situaçao = "Recuperação"
    else:
       situaçao = "Reprovado por nota"
    print(aluno["nome"], "-Frequência:", frequencia, "-Média:", media, "-Situação:", situaçao)
    if situaçao == "Aprovado":
        aprovados = aprovados + 1
print("Total de aprovados:", aprovados)

