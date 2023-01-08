import efinance as ef

df = ef.stock.get_realtime_quotes()
#print(df)
dict={}
for index,row in df.iterrows():
    code=row['股票代码']
    name=row['股票名称']
    dict[code]=name


print(dict)