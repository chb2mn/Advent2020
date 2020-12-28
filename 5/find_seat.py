def find_seat(s):
    row_id = 0
    col_id = 0
    row = s[:7]
    col = s[7:]
    bin_row = ''
    for c in row:
        bin_row += '1' if c=='B' else '0'
    row_id = int(bin_row, 2)
    bin_col = ''
    for pos in col:
        bin_col += '1' if pos=='R' else '0'
    col_id = int(bin_col, 2)
    return row_id*8 + col_id


with open('input.txt', 'r') as fin:
    sids = []
    for line in fin:
        sid = find_seat(line.strip())
        sids.append(sid)
    print(max(sids))
    for i in range(128*8):
        if (i not in sids) and (i-1 in sids) and (i+1 in sids):
            print(i)

