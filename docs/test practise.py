afang = ''' 
Z0PXH2PCPH;
2ER84GRLVM;
3ZKVWXKC0L;
0EUS6MY3AK;
6PES7C8C1F;
'''
sortiert = []
lines = afang.split()
# das Ziel ist es diese zeilen von nummern zu befreien und in alphabetische reienfolge zu bringen
for line in lines:
    #line = sortiert
    for num in '0123456789':
        line = line.replace(num, '').strip(';')
    sortiert.append(''.join(sorted(line)))

print(sortiert)