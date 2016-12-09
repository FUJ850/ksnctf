def decipher(_chr, _slideNum, _mode):
    TargetChr = _chr[0]
#    print(type(TargetChr))
    if((TargetChr >= 'a' and TargetChr <= 'z') or (TargetChr >= 'A' and TargetChr <= 'Z')):
        if(_mode % 2 == 0):
            if((chr(ord(TargetChr) - _slideNum) < 'a') or (chr(ord(TargetChr) - _slideNum) < 'A')):
                print(chr(ord('z')-ord(TargetChr)-_slideNum), end='')
            else:
                print(chr(ord(TargetChr) - _slideNum), end='')
        else:
            if((chr(ord(TargetChr) + _slideNum) > 'z') or (chr(ord(TargetChr) + _slideNum) > 'Z')):
                print(chr(ord('a')+ord(TargetChr)-_slideNum), end='')
            else:
                print(chr(ord(TargetChr) - _slideNum), end='')

    else:
        print(ord(TargetChr), end='')

if __name__ == "__main__":
    cipher = "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT."
    
    cnt = 0
    for i in cipher:
        print(decipher(i, ord('v')-ord('i'), cnt))
        cnt += 1