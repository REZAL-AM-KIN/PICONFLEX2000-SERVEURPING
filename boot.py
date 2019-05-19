print("Demarrage 'boot.py'")
exec(open('/home/pi/SERVEURPING/config.py').read())
exec(open('/home/pi/SERVEURPING/setting.py').read())
exec(open('/home/pi/SERVEURPING/importation.py').read())
exec(open('/home/pi/SERVEURPING/setup.py').read())
exec(open('/home/pi/SERVEURPING/init.py').read())
while True:
    exec(open('/home/pi/SERVEURPING/loop.py').read())