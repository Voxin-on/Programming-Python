inf={'11a':{'boys':17,'girls':13},
     '10a':{'boys':10,'girls':20},
     '9a':{'boys':12,'girls':18},
     '8a':{'boys':20,'girls':10},
     '7a':{'boys':6,'girls':24}}
sort=sorted([[inf[i]['boys']/(inf[i]['boys']+inf[i]['girls'])*100,i] for i in inf])
print('Классы по возрастанию процентов мальчиков:',*[i for _,i in sort])
print('Классы где мальчиков больше чем девочек:',*[i for proc,i in sort if proc>50])