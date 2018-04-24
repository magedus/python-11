# -*- coding: UTF-8 -*-
# random goods
import random

Wa_Zhi     = ['WZ'] * 10
Xie_Zi     = ['XZ'] * 20
Tuo_Xie    = ['TX'] * 30
Xiang_Lian = ['XL'] * 40

All_Goods=Wa_Zhi + Xie_Zi + Tuo_Xie + Xiang_Lian
randomgoods=random.sample(All_Goods,1)
print(randomgoods)