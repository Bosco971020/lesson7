y=0
a=0
ma=0
mi=0
d=100000000000000000000000000000000000000
x=int(input('你需要輸入幾個成績?'))
score_list=[]
name_list=[]
for i in range(x):         
    name = str(input('輸入新名字:'))
    y=int(input('輸入新成績:'))
    score_list.append(y)
    name_list.append(name)
    if y>a:
        ma=i
        a=y
    if y<d:
        mi=i
        d=y
print('以上的成績平均是',sum(score_list)/x)
print('總成績為',sum(score_list))
print('其中最高分是',name_list[ma],max(score_list),'分為最高分')
print('最低分是',name_list[mi],min(score_list),'分為最低分')