if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

#ordenamos la lista por nota y nombres en caso de empate
records.sort(key=lambda x: (x[1], x[0]))

#encontramos la segunda nota mas baja
second_lower_score = None
for i in range (1, len(records)):
    if records[i][1] != records[i -1][1]:
        second_lower_score = records[i][1]
        break

#imprimimos los nombres de los estudiantes con la 2da nota mas baja
second_lower_students = [record[0] for record in records if record[1] == second_lower_score]
second_lower_students.sort() #ordenamos alfabeticamente en caso de que hallan dos o mas 

for name in second_lower_students:
    print(name)