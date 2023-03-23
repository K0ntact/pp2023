import subprocess

while True:
    cmd = input('shell> ')
    if cmd == 'exit':
        break
    try:
        output = subprocess.check_output(cmd, shell=True)
        print(output.decode('utf-8'))
    except Exception as e:
        print(e)
