print("Demarrage de 'loop.py'")
_BOXS=SQL_SELECT("SELECT IP from boxs;")
print(_BOXS)
for i in range(len(_BOXS)):
    _t2=time()
    _IP=_BOXS[i][0]
    SQL_EXECUTE(QUERRY_setOnline(_IP,int(REZAL_ping(_IP))))
    if time()-_t2<1:
        sleep(0.1)
sleep(1)