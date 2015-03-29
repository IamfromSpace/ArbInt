import random

hexChars = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']


def testFromString():
    s = ''
    words = []
    for i in range(random.randint(1,10)):
        w = '0'
        s += w
        for j in range(7):
            rChar = hexChars[random.randint(0,(1<<4)-1)]
            s += rChar
            w += rChar
        words.append(w)

    s = "\t\t ArbInt a = ArbInt('0x" + s + "') from ArbIntProvider;"
    for i in range(len(words)):
        s += "\n\t\tAsserts.that(a.toNumList()["+str(i)+"])Equals(0x"+ words[len(words) - 1 - i] + ");"

    return s

def testToString():
    s = getRandomHexNumber(1,80)
    return "\t\ta = ArbInt('" + s + "') from ArbIntProvider;\n\t\tAsserts.that(a.toString())Equals('" + s + "');"

def testOp(op,aMin=1,aMax=80,bMin=1,bMax=80,aSigned=True, bSigned=True):
    a = getRandomHexNumber(aMin, aMax,aSigned)
    b = getRandomHexNumber(bMin, bMax,bSigned)
    cNum = op.pyOp(int(a,16), int(b,16))
    if cNum >= 0:
        c = "0x" + "{0:x}".format(cNum).upper()
    else:
        c = "-0x" + "{0:x}".format(abs(cNum)).upper()
        
    return "\t\ta = ArbInt('" + a + "') from ArbIntProvider;\n\t\tb = ArbInt('" + b + "') from ArbIntProvider;\n\t\tAsserts.that(a."+ op.wakeMethod + "(b).toString())Equals('" + c + "');"

def testOp2(op,aMin=1,aMax=80,bMin=1,bMax=80,aSigned=True, bSigned=True):
    a = getRandomHexNumber(aMin, aMax,aSigned)
    b = getRandomHexNumber(bMin, bMax,bSigned)
    cNum = op.pyOp(int(a,16), int(b,16))
    if cNum >= 0:
        c = "0x" + "{0:x}".format(cNum).upper()
    else:
        c = "-0x" + "{0:x}".format(abs(cNum)).upper()
        
    return "\t\ta = ArbInt('" + a + "') from ArbIntProvider;\n\t\tAsserts.that(a."+ op.wakeMethod + "("+ b +").toString())Equals('" + c + "');"

def testOp3(op,aMin=1,aMax=80,bMin=1,bMax=80,aSigned=True, bSigned=True):
    a = getRandomHexNumber(aMin, aMax,aSigned)
    cNum = op.pyOp(int(a,16))
    if cNum >= 0:
        c = "0x" + "{0:x}".format(cNum).upper()
    else:
        c = "-0x" + "{0:x}".format(abs(cNum)).upper()
        
    return "\t\ta = ArbInt('" + a + "') from ArbIntProvider;\n\t\tAsserts.that(a."+ op.wakeMethod + "().toString())Equals('" + c + "');"



def getRandomHexNumber(a,b,signed=True):
    if signed and random.randint(0,1):
        sign = '-'
    else:
        sign = ''
    s = ''
    for i in range(random.randint(a,b)):
        start = 0
        if i == 0:
            start = 1
        s += hexChars[random.randint(start,(1<<4)-1)]
    s = sign + "0x" + s
    return s

class Operation:
    def __init__(self, pyOp, wakeMethod):
        self.pyOp = pyOp
        self.wakeMethod = wakeMethod

bitNotOp = Operation(lambda a: ~a, "bitNot")
bitOrOp = Operation(lambda a, b: a | b, "bitOr")
bitAndOp = Operation(lambda a, b: a & b, "bitAnd")
bitXorOp = Operation(lambda a, b: a ^ b, "bitXor")
addOp = Operation(lambda a, b: a + b, "add")
shiftRight = Operation(lambda a,b: a >> b, "shiftRight")
shiftRight = Operation(lambda a,b: a << b, "shiftLeft")
