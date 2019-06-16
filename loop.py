print("Demarrage de 'loop.py'")
_BOXS=SQL_SELECT("SELECT IP from boxs;")
print(_BOXS)
for i in range(len(_BOXS)):
    REZAL_pingAndSetState(_BOXS[i][0])
sleep(1)
