print(' = = = = = = = = = = GRACKNUX CALCULATOR = = = = = = = = = = ')
print('amaliyat ra entekhab koniid')
print('{1} mashin hesab')
print('{2} hendese')
print('{3} bakhsh paziri')
print('{4} adade aval')
print('{5} ertebat ba man')
first = int(input("adade noe moadele ra vare konid >>>"))

if first == 1 :
    output = float(input('>>>'))
    print('javab >>>',output)
if first == 2 :
    print("noe mohasebe ra entehab konid")
    print("{1} mohit")
    print("{2} masahat")
    first3 = int (input(">>>"))
    if first3 == 1 :
        print("{1} moraba")
        print("{2} mostatil")
        print("{3} dayere")
        print("{4} mosalas (hame ye mosalas ha) ")
        print("{5} motezavi al azla")
        print("{6} beyzi (be zodi ...)")
        mo = int(input(">>>"))
        if mo == 1 :
            mmoraba = float(input("andazeh ye zel :"))
            print(mmoraba*4)
        if mo == 2 :
            mmostatil1 = float(input("tol :"))
            mmostatil2 = float(input("arz :"))
            print(mmostatil1 + mmostatil1 +mmostatil2 +mmostatil2)
        if mo == 3 :
            pe = 3.1415
            mdayere = float(input("ghor ra vare konid >>>"))
            print(mdayere*pe)
        if mo == 4 :
            momo1 = float(input("zel 1:"))
            momo2 = float(input("zel 2:"))
            momo3 = float(input("zel 3:"))
            print(momo1+momo2+momo3)
        if mo == 5:
            momote1 = float(input("majmoe do zel motevali >>>"))
            print(momote1*2)
#======================================================================
    if first3 == 2 :
        print("{1} moraba")
        print("{2} mostatil")
        print("{3} dayere")
        print("{4} mosalas (tamami mosalas ha)")
        print("{5} motezavi al azla")
        print("{6} kore")
        masahat = int(input(">>>"))
        if masahat == 1:
            mamoraba = float(input("zel >>>"))
            print(mamoraba*mamoraba)
        if masahat == 2:
            mamostatil1 = float(input("tol >>>"))
            mamostatil2 = float(input("arz >>>"))
            print(mamostatil1*mamostatil2)
        if masahat == 3:
            shdr = float(input("shoa >>>"))
            print(shdr*shdr*3.1415)
        if masahat == 4:
            qmosalas = float(input("ghaede >>>"))
            emosalas = float(input("ertefa >>>"))
            print(qmosalas*emosalas/2)
        if masahat == 5 :
            mamote1 = float(input("qaede >>>"))
            mamote1 = float(input("ertefa >>>"))
            print(mamote1*mamote2)
        if masahat == 6 :
            makore1 = float(input("shoa ra vared konid >>>"))
            makore2 = makore1**2
            print(makore2*3.1415*4)
#======================================================================
if first == 3 :
    print('{1} test bakhsh paziri')
    tba = int(input('>>>'))
    if tba == 1 :
        tba1 = int(input('adade aval >>>'))
        tba2 = int(input('adade dovom >>>'))
        if tba1 % tba2 == 0:
            print('bakhsh pazir')
        else :
            print('bakhsh pazir nist')
#======================================================================
if first == 4:
    print('{1} test avval bodan')
    aval1 = int(input('>>>'))
    adadaval1 = []
    if aval1 == 1:
        aval2 = int(input('adad ra vared konid '))
        print('dar hale pardazesh ...')
        for avfor1 in range(2,aval2):
            if aval2 % avfor1 == 0:
                adadaval1.append(1)
            else:
                adadaval1.append(2)
        if 1 in adadaval1:
            print('aval nist')
        else :
            print('aval ast')
#======================================================================
if first == 5:
    print('Email: moh.rajabi05@gmail.com')
    print('website: rajabii.ir')
    print('twitter: twitter.com/moh_rajabi05')
