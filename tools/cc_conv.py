import sys
import re

def cc(shfl, ofs):
    
    shc_hx = re.sub(r"[^a-fA-F0-9]", "", shfl)

    cnt = 1
    bt = ''
    en_shc = ''


    for i in shc_hx:
        if(cnt %2 == 0):
            bt = bt + i
            bt = int(bt,16)
            bt = int(bt + ofs)
            bt = int(bt % 256)
            bt = hex(bt)[2:]
            if(len(bt)==1):
                bt = "0" + bt
            bt = "\\x" + bt
            en_shc = en_shc + bt
            bt = ''
        else:
            bt = bt + i
        cnt += 1



    for i in shc_hx:
        if(cnt %2 == 0):
            bt = bt + i
            bt = int(bt,16)
            bt = int(bt + ofs)
            bt = int(bt % 256)
            bt = hex(bt)[2:]
            if(len(bt)==1):
                bt = "0" + bt
            bt = "\\x" + bt
            en_shc = en_shc + bt
            bt = ''
        else:
            bt = bt + i
        cnt += 1

    en_shc = en_shc
    return en_shc


def fmt_txt(string, every):
    lines = []
    lines.append("unsigned char shcd[] = ")
    for i in range(0,len(string), every):
        lines.append("\"" + string[i:i+every] + "\"")
    return '\n'.join(lines)



def main():
    try:
        shfl = open(sys.argv[1], "r").read()
        ofs = int(sys.argv[2]) if len(sys.argv) > 2 else 0
        every = int(sys.argv[3]) if len(sys.argv) > 3 else 60
        
    except:
        print("Valid file Required - %s <shc_file>" %sys.argv[0], "optional <ofs> optional <every>")
        sys.exit()
    
    enc_text = cc(shfl, ofs)
    print(fmt_txt(enc_text, every),';',sep="")

main()
