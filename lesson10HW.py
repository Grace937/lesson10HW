v={'apple':'蘋果','banana':'香蕉','water':'水',
   'computer':'電腦','pencil':'鉛筆','book':'書'}
b=['列出字彙表輸入1','英翻中輸入2','中翻英輸入3',
   '測驗學習結果輸入4','離開系統輸入5']
def quiz():
    score=0
    for ff,gg in v.items():
        print(ff)
        ans=input('請輸入中文')
        if ans==gg:
            score=score+1
    print('測驗結束,分數為'+str(score)+'/6')
i=0
for ss in b:
    print(ss)
a=input('選擇功能')
while i<1:
    if a=='1':
        for e,ee in v.items():
            print(e,ee)
        a=input('選擇功能')
    elif a=='2':
        c=input('請輸入單字 ')
        if c in v:
            print(v[c])
        else:
            print('無此單字')
        a=input('選擇功能')
    elif a=='3':
        d=input('請輸入中文 ')
        g=1
        for q,qq in v.items():
            if qq==d:
                g=q
        if g!=1:
            print(g)
        else:
            print('無此單字')
        a=input('選擇功能')
    elif a=='4':
        print('開始測驗')
        quiz()
        a=input('選擇功能')
    elif a=='5':
        print('已離開系統')
        i=i+1
