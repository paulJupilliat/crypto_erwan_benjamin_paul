FRENQUENCE_FRANCAIS = {
    'A': 7.636,
    'B': 0.901,
    'C': 3.260,
    'D': 3.669,
    'E': 14.715,
    'F': 1.066,
    'G': 0.866,
    'H': 0.737,
    'I': 7.529,
    'J': 0.613,
    'K': 0.074,
    'L': 5.456,
    'M': 2.968,
    'N': 7.095,
    'O': 5.796,
    'P': 2.521,
    'Q': 1.362,
    'R': 6.693,
    'S': 7.948,
    'T': 7.244,
    'U': 6.311,
    'V': 1.838,
    'W': 0.049,
    'X': 0.427,
    'Y': 0.128,
    'Z': 0.326
}

def tableau_frequence(texte):
    res = {}
    for lettre in [ord(char.upper()) for char in texte]:
        if lettre >= 65 and lettre <= 90:
            if lettre not in res.keys():
                res[lettre] = 0
            res[lettre] += 1
    return res

def Ic(texte):
    ic = 0
    tableau_freq = tableau_frequence(texte)
    for lettre in tableau_freq.keys():
        ic += (tableau_freq[lettre] * (tableau_freq[lettre]-1))
    return ic/(len(texte) * (len(texte) -1))

def inverse_matrice_mod_26(matrice:list[int,int,int,int]):
    res = []
    det = matrice[0] * matrice[3] - matrice[1] * matrice[2]
    coeff_d = matrice[3] * det
    while coeff_d < 0:
        coeff_d += 26
    while coeff_d >= 26:
        coeff_d -= 26
    res.append(coeff_d)
    coeff_c = (- matrice[2]) * det
    res.append(coeff_c)
    coeff_b = (- matrice[1]) * det
    res.append(coeff_b)
    coeff_a = matrice[0] * det
    res.append(coeff_a)

def decode_HILL(texte):
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    if a*d-c*b!=0:
                        inverse = inverse_matrice_mod_26([a,b,c,d])

print(1)
print(Ic("Huyzu Izxk u'hoovihvy eht h wzopvo. Vk hkkdph. Tzu Ahc phojdhvy pvudvy ivuly. Vk ezdtth du eozgzuw tzdevo, t'httvy whut tzu kvy, t'heedxhuy tdo tzu ezkzrqzu. Vk eovy du ozphu, vk k'zdiovy, vk kdy; phvt vk u'x thvtvtthvy jd'du vpmozlkvz rzugdt, vk mdyhvy h yzdy vutyhuy tdo du pzy wzuy vk vluzohvy kh tvluvgvrhyvzu. Vk hmhuwzuuh tzu ozphu tdo tzu kvy. Vk hkkh h tzu khihmz; vk pzdvkkh du lhuy jd'vk ehtth tdo tzu gozuy, tdo tzu rzd."))
print("mono")
print(2)
print(Ic("Dwi gsftn seebvzx ezjg jzzo. Zp ldvzx npvlh. Tt jlzcqo jsy dvjmdbvj, wnzpke wi ilme. Qg wetavzx owpo. Yy jmlme qiumdbdege ujexlqo uy qipssfzb. Lr nimzpwwi, gpfa gfycl ll'yy ogrw, atpj wzcmu uf'ci ksnade, twcn gvznjeh bc'pe fzcmusy, vje pzqi, jsyvv kvzqn tsfxn. Uy niirp Didex-Ximkmy, ci tplxjkmd xgrmybdw wtoirplqo lr npvceyl llm ainjetb."))
print("poly")
print(3)
print(Ic("Sop u'dffrmtfe oz qvigpjcm, bh nnaqhd iw hcbvrl dvercy, h d'youcxlmdc zpzirn, ay eg xpzzht, qy eg xohirgxpb, ymsu lstlhf bh zhkhakc, z'lbnnecvz, layoanfe bh bidv g'dlky. Oy x'txdwiyoh, gnvxnnt w'txwlkhr g'bh uuhr oju, nyor v'nnaqhd dwvz akl ojr, erdpzhyomennv innr vn nmim tqvfe om'xl yof qv x'cmksxluzf."))
print("poly")
print(4)
print(Ic("Zc krgfkr u'le ufzxk le rzi drikzrc jli c'fscfex tyrjjzj ul mrjzjkrj. Zc flmizk jfe wizxf dlirc, zc gizk ul crzk wifzu, zc slk le xireu sfc. Zc j'rgrzjrzk. Zc j'rjjzk jli jfe tfjp, zc gizk le aflierc hl'zc gritflilk u'le rzi uzjkirzk. Zc rccldr le tzxrizccf hl'zc wldr aljhl'rl sflk hlfzhl'zc kiflmrk jfe griwld ziizkrek. Zc kfljjr."))
print("mono")
print(5)
print(Ic("Os dom sb kbrog : wf bok bykg-ewzbof ywm lwoxo r'wf zglmgf, hwol wf mbfug, hwol wf ygv-mkgm, hwol wf egmossgf dol bw ugwm rw pgwk. Rwmkgfe eibfmb rw Sbfndbff, Zbkzbkb wf dbrkoubs r'Bkbugf, Lmoei-Kbfrbss wf bok r' Borb."))
print("mono")

