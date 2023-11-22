import subprocess

command = 'python main.py'
a = int(input('Введите кол-во потоков: '))
for i in range(a):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    print(f'Поток {i} запущен')
