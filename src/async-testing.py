import time

async def _mi_2_second():
    print("Inicio de la ejecucion 1")
    await time.sleep(2)
    print("Fin ejecucion 1")

async def _mi_43_second():
    print("aaa")
    time.sleep(1)
    print("fin")



_mi_2_second()
_mi_43_second()