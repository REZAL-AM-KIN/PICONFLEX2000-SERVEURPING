print("Demarrage de 'loop.py'")
_BOXS=SQL_SELECT("SELECT IP from boxs;")
print(_BOXS)
for i in range(len(_BOXS)):
    _t2=time()
    SQL_EXECUTE(QUERRY_setOnline(_IP,int(REZAL_ping(_BOXS[i][0]))))
sleep(1)
