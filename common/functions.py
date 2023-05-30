def priceToCopperPiece(self, strValue):
    value = 0
    if (strValue.strip() == '-'):
        return value
    elif strValue.find('sp'):
        value = int(strValue.split()[0])*10
    elif strValue.find('gp'):
        value = int(strValue.split()[0])*100
    else:
        value = int(strValue()[0])
    return value
