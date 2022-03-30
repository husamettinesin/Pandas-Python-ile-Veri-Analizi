
import pandas as pd

df=pd.read_csv("datasets/youtune-ing.csv")

# 1- İlk 1o kaydı getirin
result=df.head(10)

# 2-  İkinci 5 kaydı getiriniz.
result=df[5:10].head(5)  # ilk önce ilk 5 ile 20 arasındaki kaydı getir. Sonra ilk 5 dedik

# 3- Dataset de bulunan  kolon isimleri ve sayısını bulunuz.
result=df.columns
result=len(df.columns)

# 4- Aşağıda bılınan bazı kolonları silin ve kalan kolonları listeleyiniz.
 #  (thumbnail_link, coments_disabled,tatings_disabled)
df=df.drop(["thumbnail_link","comments_disabled","ratings_disabled","video_error_or_removed","description","trending_date"],axis=1,inplace=True)

# 5- Beğenme (like) ve beğenmeme(dislike) sayılarının ortlamasını bulunuz.
result=df["likes"].mean()
result=df["dislikes"].mean()

# 6- İlk 50 videonun like ve dislike kolonlarını getiriniz.
result=df.head(50)[["Title","likes","dislikes"]]

# 7 En çok görüntülen video hangisidir ?
result=df[df["views"].max()==df["views"]]["title"].iloc[0]

# 8- En düşük görüntülenen video hangisidir ?
result=df[df["views"].min()==df["views"]]["title"].iloc[0]

# 9- en fazla görüntülenen ilk 10 video hangisidir ?
result=df.sort_values("views", ascending=False).head(10)[["title","views"]]

# 10- Kategoriye göre beğeni ortalmasını sıralı şekilde getiriniz.
result=df.groupby("category_id").mean().sort_values("likes")["likes"]

# 11 - Kategoriye göre yorum sayılarını yukarıdan aşağıya sıralayınız.
result=df.groupby("category_id").sum().sort_values("comment_count",ascending=False)["comment_count"]

# 12- Her kategoride kaç video vardır ?
result=df["category_id"].value_counts()

# 13- Her videonun title uzunluğu bilgisini yeni bir kolonda gösteriniz.
df["title_len"]=df["title"].apply(len)
result=df



print(result)