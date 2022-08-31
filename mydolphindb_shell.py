if __name__ == '__main__':
    from mypy import tryx,now,sys,time_maker,log1,flush1
    log1('...');flush1();
    from mydolphindb import mydolphindb
    biz = mydolphindb()

    biz("clearAllCache();go;")

    # my data adaptor
    from myts import biz as ts

    # quick-semicolon-shell
    log1(f'{time_maker(outfmt="%H:%M:%S")} $> ');flush1();
    cmda = []
    for line in sys.stdin:
        cmda.append(line)
        if len(line)>1 and line[-2] in ';':
            cmd = ''.join(cmda)
            cmda = []
            if len(cmd)==0: continue
            if cmd[0] in ['`',';']:
                cmd = cmd[1:-2]
                if cmd: rt = tryx(lambda:eval(cmd))
                else: rt = None
            else:
                rt = tryx(lambda:biz(cmd))
            if rt is not None: print(rt)
            log1(f'{time_maker(outfmt="%H:%M:%S")} $> ');flush1();
