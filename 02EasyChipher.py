# coding: utf-8

cipher = list("EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.")

for i in range(len(cipher)):
    if cipher[i].isalnum() == False:
        print(cipher[i], end='')

    else:
        upper_flag = 0

        if cipher[i].isupper():
            upper_flag = 1
        else:
            upper_flag = 0

        if cipher[i] >= chr(ord('n') - 32 * upper_flag):
            print(chr(ord(cipher[i])-13), end='')
        else:
            print(chr(ord(cipher[i])+13), end='')
