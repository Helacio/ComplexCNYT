import complejos as lib

passed = 0
failed = 0

c1 = (3,-8)
c2 = (4,6)

resp = lib.suma(c1, c2)
if resp[0] == 7 and resp[1] == -2:
    passed += 1
else:
    failed += 1


resp1 = lib.mult(c1, c2)
if resp1[0] == 60 and resp1[1] == -14:
    passed +=1
else:
    failed += 1


resp2 = lib.resta(c1, c2)
if resp2[0] == -1 and resp2[1] == -14:
    passed +=1
else:
    failed += 1


resp3 = lib.div(c1, c2)
if resp3[0] == 12.375 and resp3[1] == 3.625:
    passed +=1
else:
    failed += 1


resp4 = lib.modulo(c1)
if resp4 == 8.54400374531753:
    passed += 1
else:
    failed += 1


resp5 = lib.conjugado(c1)
if resp5[0] == 3 and resp5[1] == 8:
    passed += 1
else:
    failed += 1


resp6 = lib.reprePolarCart(c1)
if resp6[0] == -0.4365001014258406 and resp6[1] == -2.9680747398701453:
    passed += 1
else:
    failed += 1


resp7 = lib.fase(c1)
if resp7 == -1.2120256565243244:
    passed += 1
else:
    failed += 1
    
print("Passed:" + str(passed) + " " + "Failed:" + str(failed) )
