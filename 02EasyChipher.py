# coding: utf-8

cipher = list("EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT.")

for i in range(len(cipher)):
    if cipher[i] == ' ':
        print(" ", end='')
        pass

    else:
        if cipher[i] >= 'a' and cipher[i] <= 'z':
            if cipher[i] >= chr(ord('n')):
                print(chr(ord(cipher[i])-13), end='')
            else:
                print(chr(ord(cipher[i])+13), end='')

        elif cipher[i] >= 'A' and cipher[i] <= 'Z':
            if cipher[i] >= chr(ord('N')):
                print(chr(ord(cipher[i])-13), end='')
            else:
                print(chr(ord(cipher[i])+13), end='')
