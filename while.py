from os import system as run
while True:
    try:
        import requests
        break
    except:
        run('pip install --force-reinstall requests')
        continue
