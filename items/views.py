from django.shortcuts import render

context={'list':[
    {
    'price':'68.00',
    'title':'python编程鼠标垫程序员神器码农 ',
    'shopNick':'龙老大旗舰店',
    'image': 'https://gd2.alicdn.com/imgextra/i2/513779980/O1CN01funE8q2NatEhdCKWw_!!513779980.jpg',
    'count':'58',
    'postal':True,
    'payNum':'500'
    },
    {
    'price':'59.00',
    'title':'秋冬季长袖衬衫男士程序员IT格子',
    'shopNick':'位老板旗舰店',
    'image': 'https://img.alicdn.com/imgextra/i4/29096657/O1CN018Qxxra1z2xAn7EpGj_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'2',
    'postal':False,
    'payNum':'9999'
    },
    {
    'price':'168.00',
    'title':'现货正版 计算机科学中的数学',
    'shopNick':'文王爷旗舰店',
    'image': 'https://img.alicdn.com/imgextra/i1/111354297/O1CN01y2VWCZ1hc4StmmHxe_!!2-saturn_solar.png_220x220.jpg_.webp',
    'count':'20',
    'postal':True,
    'payNum':'50'
    },
    {
    'price':'144.00',
    'title':'程序员面试宝典书',
    'shopNick':'艮少爷自营店',
    'image': 'https://img.alicdn.com/imgextra/i4/32846184/O1CN01vyvbvf1vYJqW6iPfz_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'75',
    'postal':False,
    'payNum':'0'
    },
    {
    'price':'39.60',
    'title':'正版 程序员修炼之道',
    'shopNick':'baby豪自营店',
    'image': 'https://img.alicdn.com/imgextra/i4/111354297/TB2HAnnkuGSBuNjSspbXXciipXa_!!2-saturn_solar.png_220x220.jpg_.webp',
    'count':'30',
    'postal':True,
    'payNum':'155'
    },
    {
    'price':'44.90',
    'title':'Python程序员面试宝典',
    'shopNick':'黑黑自营店',
    'image': 'https://img.alicdn.com/imgextra/i4/178020169/O1CN0103dDNt1D7RTPoUssN_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'26',
    'postal':True,
    'payNum':'98'
    },
    {
    'price':'139.99',
    'title':'套装3本 程序员的数学',
    'shopNick':'lee官方旗舰店',
    'image': 'https://img.alicdn.com/imgextra/i1/50165682/O1CN019NVqnI1rqP0PVEMUX_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'9',
    'postal':False,
    'payNum':'999+'
    },
    {
    'price':'300.09',
    'title':'程序员教程(第5版)',
    'shopNick':'京源畅想图书店',
    'image': 'https://img.alicdn.com/imgextra/i1/29378329/O1CN01HmJICb2BOjOEt7RTH_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'60',
    'postal':True,
    'payNum':'9'
    },
    {
    'price':'56.90',
    'title':'正版 程序员的自我修养',
    'shopNick':'IT官方旗舰店',
    'image': 'https://img.alicdn.com/imgextra/i2/55492740/O1CN018ZpJKK1W6xkW3soo6_!!0-saturn_solar.jpg_220x220.jpg_.webp',
    'count':'76',
    'postal':True,
    'payNum':'9'
    },
    {
    'price':'99.00',
    'title':'Python3编程视频教程零基础',
    'shopNick':'code-hack旗舰店',
    'image': 'https://img.alicdn.com/imgextra/i3/124966102/O1CN01QmdCk71uwlLRhEmWQ_!!0-saturn_solar.jpg_260x260.jpg',
    'count':'529',
    'postal':False,
    'payNum':'999+'
    },]
}

def index(request):
    return render(request,'items/list.html',context)
# Create your views here.
