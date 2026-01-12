def Weight_Calculator(lst):
    
    d = {'A':89.09,'G':75.07,'I':131.17,'V':117.15,'F':165.19,'Y':181.19,'N':132.12,'C':121.16,'Q':146.15,'D':133.10,'R':174.20,'H':155.16,'L':131.17,'M':149.21,'P':115.13,'W':204.23,'S':105.09,'T':119.12,'E':147.13,'K':146.19}
    w = 0

    for l in lst:
        seq = l['sequence']
        for s in seq:
            w += d[s]

        wh = float((len(seq)-1)) * 18.015
        mw = w - wh
        l['mw'] = mw

    return lst
