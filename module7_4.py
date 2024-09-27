# Использование %

team1_num = 5
team2_num = 6
print('В команде Мастера кода участников: %s !' % (team1_num))
print('Итого сегодня в командах участников: %s и %s !' % (team1_num, team2_num))

# print('В команде Мастера кода участников: %(team1_num)s !' % {'team1_num': '5'})
# print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s !' % {'team1_num': '5', 'team2_num': '6'})


#  Использование format()
score_2 = 42
team1_time = 18015.2
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} с !'.format(team1_time))

# print('Команда Волшебники данных решила задач: {score_2} !'.format(score_2=42))
# print('Волшебники данных решили задачи за {team1_time} с !'.format(team1_time=18015.2))


# Использование f-строк
score_1 = 40
challenge_result = 'Победа команды Волшебники данных!'
tasks_total = 82
time_avg = 350.4
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')
