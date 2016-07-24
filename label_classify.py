
# tansform data 
import pandas as pd
alldata = pd.read_excel('./input_test.xlsx',header = None)
alldata.to_csv('./input_test.csv', header = None, index = None, encoding = 'utf-8')

# 取所有不重复的病症为一个list,作为结果的列名，allsymb
# creat a list(allsymb) as colname in the result
with open('./input_test.csv','r') as all:
    allsymbols = []
    for line in all:
        eachone = line.split(',')
        for i in eachone:
            if len(str(i)) > 1:
                allsymbols.append(i.strip('\n'))
    allsymbol = set(allsymbols)
    allsymb = list( allsymbol )

# 定义一个dict，每个key－value对应一行数据，key[0]对应不同symbol，其他value为1表示有此病症，0则没有
# creat a dict, every key－value stand for a patient, key[0] is the colname(different symbols)
with open('./input_test.csv','r') as all:
    final = {}
    final[0] = allsymb
    key=0
    for line in all:
        key = key +1
        values = line.split(',')
        everylist = [0] * len(allsymb)
        for value in values:
            if len(str(value)) > 1:
                location = allsymb.index(value.strip())
                everylist[location] = 1
                final[key] = everylist

# write dict to csv
with open( 'output_test.tsv', 'w' ) as f:
    for key, values in sorted( final.items() ):
        f.write( str(key) + '\t' )
        for value in values :
            f.write( str(value) + '\t' )
        f.write('\n')