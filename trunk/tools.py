# coding: iso-8859-1
def getValueStringFromValues(values, minValue, maxValue):
    """ return string representation from tuple/list """
    valueStr = ""
    inValueRange = False
    lastValue = -100
    for i in xrange(minValue, maxValue + 1):
        if values[i-minValue]:
            if not inValueRange:
                inValueRange = True
                lastValue = i
                valueStr += str(i)
        else:
            if inValueRange:
                inValueRange = False
                if i-1 != lastValue:
                    valueStr += "-"
                    valueStr += str(i-1)
                valueStr += ","
    if inValueRange:
        if i != lastValue:
            valueStr += "-"
            valueStr += str(i)
    else:
        valueStr = valueStr[:-1] #strip last comma
    if valueStr == "%s-%s" % (minValue, maxValue):
        valueStr = "*"
    elif valueStr == "":
        valueStr = "?"
    return valueStr
