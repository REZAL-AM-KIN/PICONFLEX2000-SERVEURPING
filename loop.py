print("Demarrage de 'loop.py'")
_BOXS=SQL_SELECT("SELECT IP from boxs;")
print(_BOXS)
for i in range(len(_BOXS)):
    threading.Thread(target=REZAL_pingAndSetState,args=[_BOXS[i][0]]).start()
sleep(1)
