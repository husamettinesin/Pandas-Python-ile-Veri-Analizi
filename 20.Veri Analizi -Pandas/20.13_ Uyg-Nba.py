import pandas as pd

df=pd.read_csv("datasets/nba.csv")

# 1-  ilk 10 kaydı alın
result=df.head(10)
#2- Toplam kaç kayıt vardır ?
result=len(df.index)
#3- Tüm oyuncuların toplma maaş ortalaması alın
result=df["Salary"].mean()  # ortalama fonksiyonu mean()
# 4- En yüksek maaşı en kadardır ?
result =df["Salary"].max()

# 5- En yüksek maaşı alan oyuncu kimdir ?
result= df[df["Salary"]==df["Salary"].max()]["Name"].iloc[0]

#6- Yaşı 20-35 arasında olan oyuncuların isim ve oynadıkları takımları azalan şekilde sıralı olarak getiriniz.
result= df[(df["Age"] >=20) & (df["Age"]<25)][["Name", "Team","Age"]].sort_values("Age",ascending=False)  # true veya false döner 

# 7- "John Holland" isimli oyuncuunun oynadığı takım hangisidir.
result =df[df["Name"]=="John Holland"]["Team"].iloc[0]

# 8- Takımlara göre oyuncuların ortalama maaş bilgisi nedir ?
result=df.groupby("Team").mean()["Salary"]

# 9- Kaç farklı takım mevcut ?
result= len(df.groupby("Team"))
result=df["Team"].nunique()  # tekrarlayanları almaz bu fonksiyom

# 10 - Her takımda kaç oyuncu oynamaktadır ?
result=df["Team"].value_counts()

# 11- İsmi içinde "and" geçen kayıtları bulunuz.
df=df.dropna()
result= df[df["Name"].str.contains("and")]


print(result)

