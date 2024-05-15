def vagon(seatnumber):
    if seatnumber < 37:
        if seatnumber % 2 ==0:
            print ("верхнее место в купе")
        else:
            print ("нижнее место в купе")
    else:
        if seatnumber % 2 ==0:
            print ("верхнее место боковое")
        else:
            print ("нижнее место боковое")
seatnumber = int(input("Введите место в первом вагоне"))
vagon(seatnumber)