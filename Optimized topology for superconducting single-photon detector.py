from phidl import CrossSection, Device
import phidl.geometry as pg
from phidl import quickplot as qp
import phidl.path as pp
wid = float(0.225)
pit = float(wid + 0.2)
lenn = float(1.15)

D = Device('my device')

#1 crossSection for hairpin function & hairpin (on the right side,straight)
X1 = CrossSection()
X1.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg', ports = ('in1', 'out1'))
X1.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg2', ports = ('in3', 'out4'))
X2 = CrossSection()
X2.add(width = wid, offset = -pit/2, layer = 1, name = 'wg', ports = ('in2', 'out2'))
X2.add(width = wid, offset = pit/2, layer = 1, name = 'wg2',  ports = ('in5', 'out6'))

P1 = pp.straight(length = 0)
P2 = pp.straight(length = 0)
WG1 = P1.extrude(X1)
WG2 = P2.extrude(X2)

D = Device()
wg1 = D << WG1
wg2 = D << WG2
wg2.movex(7.5)

Xtrans = pp.transition(cross_section1 = X1,
                       cross_section2 = X2,
                       width_type = 'sine')
P3 = pp.straight(length = 0.9)
WG_trans = P3.extrude(Xtrans)

Hairpin = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)

#2 crossSection for hairpin2 function & hairpin2 (on the left side,straight)

X12 = CrossSection()
X12.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg2', ports = ('in12', 'out12'))
X12.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg22', ports = ('in32', 'out42'))
X22 = CrossSection()
X22.add(width = wid, offset = -pit/2, layer = 1, name = 'wg2', ports = ('in22', 'out22'))
X22.add(width = wid, offset = pit/2, layer = 1, name = 'wg22',  ports = ('in52', 'out62'))

P12 = pp.straight(length = 0)
P22 = pp.straight(length = 0)
WG12 = P12.extrude(X12)
WG22 = P22.extrude(X22)

wg12 = D << WG12
wg22 = D << WG22
wg22.movex(7.5)

Xtrans2 = pp.transition(cross_section1 = X12,
                       cross_section2 = X22,
                       width_type = 'sine')
P32 = pp.straight(length = 0.9)
WG_trans2 = P32.extrude(Xtrans2)

Hairpin2 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)

#3 crossSection for hairpin3 function  & hairpin3 (30 degrees turn, left side)

X13 = CrossSection()
X13.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg3', ports = ('in13', 'out13'))
X13.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg23', ports = ('in33', 'out43'))
X23 = CrossSection()
X23.add(width = wid, offset = -pit/2, layer = 1, name = 'wg3', ports = ('in23', 'out23'))
X23.add(width = wid, offset = pit/2, layer = 1, name = 'wg23',  ports = ('in53', 'out63'))

P13 = pp.straight(length = 0)
P23 = pp.straight(length = 0)
WG13 = P13.extrude(X13)
WG23 = P23.extrude(X23)

D = Device()
wg13 = D << WG13
wg23 = D << WG23
wg23.movex(7.5)

Xtrans3 = pp.transition(cross_section1 = X13,
                       cross_section2 = X23,
                       width_type = 'sine')
P33 = pp.straight(length = 0.5)
WG_trans3 = P33.extrude(Xtrans3)


Hairpin3 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P43 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans3 = P43.extrude(Xtrans3)

#4 crossSection for hairpin4 & hairpin4 (30 degrees turn, right side)

X14 = CrossSection()
X14.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg4', ports = ('in14', 'out14'))
X14.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg24', ports = ('in34', 'out44'))
X24 = CrossSection()
X24.add(width = wid, offset = -pit/2, layer = 1, name = 'wg4', ports = ('in24', 'out24'))
X24.add(width = wid, offset = pit/2, layer = 1, name = 'wg24',  ports = ('in54', 'out64'))

P14 = pp.straight(length = 0)
P24 = pp.straight(length = 0)
WG14 = P14.extrude(X14)
WG24 = P24.extrude(X24)

D = Device()
wg14 = D << WG14
wg24 = D << WG24
wg24.movex(7.5)

Xtrans4 = pp.transition(cross_section1 = X14,
                       cross_section2 = X24,
                       width_type = 'sine')
P34 = pp.straight(length = 0.5)
WG_trans4 = P34.extrude(Xtrans4)


Hairpin4 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P44 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans4 = P44.extrude(Xtrans4)

#5 crossSection for hairpin5 function  & hairpin5 (30 degrees turn, left side)

X15 = CrossSection()
X15.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg5', ports = ('in15', 'out15'))
X15.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg25', ports = ('in35', 'out45'))
X25 = CrossSection()
X25.add(width = wid, offset = -pit/2, layer = 1, name = 'wg5', ports = ('in25', 'out25'))
X25.add(width = wid, offset = pit/2, layer = 1, name = 'wg25',  ports = ('in55', 'out65'))

P15 = pp.straight(length = 0)
P25 = pp.straight(length = 0)
WG15 = P15.extrude(X15)
WG25 = P25.extrude(X25)

D = Device()
wg15 = D << WG15
wg25 = D << WG25
wg25.movex(7.5)

Xtrans5 = pp.transition(cross_section1 = X15,
                       cross_section2 = X25,
                       width_type = 'sine')
P35 = pp.straight(length = 0.5)
WG_trans5 = P35.extrude(Xtrans5)


Hairpin5 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P45 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans5 = P45.extrude(Xtrans5)
#6 crossSection for hairpin6 function  & hairpin6 (30 degrees turn, right side)
X16 = CrossSection()
X16.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg6', ports = ('in16', 'out16'))
X16.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg26', ports = ('in36', 'out46'))
X26 = CrossSection()
X26.add(width = wid, offset = -pit/2, layer = 1, name = 'wg6', ports = ('in26', 'out26'))
X26.add(width = wid, offset = pit/2, layer = 1, name = 'wg26',  ports = ('in56', 'out66'))

P16 = pp.straight(length = 0)
P26 = pp.straight(length = 0)
WG16 = P16.extrude(X16)
WG26 = P26.extrude(X26)

D = Device()
wg16 = D << WG16
wg26 = D << WG26
wg26.movex(7.5)

Xtrans6 = pp.transition(cross_section1 = X16,
                       cross_section2 = X26,
                       width_type = 'sine')
P36 = pp.straight(length = 0.5)
WG_trans6 = P36.extrude(Xtrans6)


Hairpin6 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P46 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans6 = P46.extrude(Xtrans6)
#7 crossSection for hairpin7 function  & hairpin7 (30 degrees turn, left side)
X17 = CrossSection()
X17.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg7', ports = ('in17', 'out17'))
X17.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg27', ports = ('in37', 'out47'))
X27 = CrossSection()
X27.add(width = wid, offset = -pit/2, layer = 1, name = 'wg7', ports = ('in27', 'out27'))
X27.add(width = wid, offset = pit/2, layer = 1, name = 'wg27',  ports = ('in57', 'out67'))

P17 = pp.straight(length = 0)
P27 = pp.straight(length = 0)
WG17 = P17.extrude(X17)
WG27 = P27.extrude(X27)

D = Device()
wg17 = D << WG17
wg27 = D << WG27
wg27.movex(7.5)

Xtrans7 = pp.transition(cross_section1 = X17,
                       cross_section2 = X27,
                       width_type = 'sine')
P37 = pp.straight(length = 0.5)
WG_trans7 = P37.extrude(Xtrans7)


Hairpin7 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P47 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans7 = P47.extrude(Xtrans7)
#8 crossSection for hairpin8 function  & hairpin8 (30 degrees turn, right side)
X18 = CrossSection()
X18.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg8', ports = ('in18', 'out18'))
X18.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg28', ports = ('in38', 'out48'))
X28 = CrossSection()
X28.add(width = wid, offset = -pit/2, layer = 1, name = 'wg8', ports = ('in28', 'out28'))
X28.add(width = wid, offset = pit/2, layer = 1, name = 'wg28',  ports = ('in58', 'out68'))

P18 = pp.straight(length = 0)
P28 = pp.straight(length = 0)
WG18 = P18.extrude(X18)
WG28 = P28.extrude(X28)

D = Device()
wg18 = D << WG18
wg28 = D << WG28
wg28.movex(7.5)

Xtrans8 = pp.transition(cross_section1 = X18,
                       cross_section2 = X28,
                       width_type = 'sine')
P38 = pp.straight(length = 0.5)
WG_trans8 = P38.extrude(Xtrans8)


Hairpin8 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P48 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans8 = P48.extrude(Xtrans8)
#9 crossSection for hairpin9 function  & hairpin9 (30 degrees turn, left side)
X19 = CrossSection()
X19.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg9', ports = ('in19', 'out19'))
X19.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg29', ports = ('in39', 'out49'))
X29 = CrossSection()
X29.add(width = wid, offset = -pit/2, layer = 1, name = 'wg9', ports = ('in29', 'out29'))
X29.add(width = wid, offset = pit/2, layer = 1, name = 'wg29',  ports = ('in59', 'out69'))

P19 = pp.straight(length = 0)
P29 = pp.straight(length = 0)
WG19 = P19.extrude(X19)
WG29 = P29.extrude(X29)

D = Device()
wg19 = D << WG19
wg29 = D << WG29
wg29.movex(7.5)

Xtrans9 = pp.transition(cross_section1 = X19,
                       cross_section2 = X29,
                       width_type = 'sine')
P39 = pp.straight(length = 0.5)
WG_trans9 = P39.extrude(Xtrans9)


Hairpin9 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P49 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans9 = P49.extrude(Xtrans9)
#10 crossSection for hairpin10 function  & hairpin10 (30 degrees turn, right side)
X110 = CrossSection()
X110.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg10', ports = ('in110', 'out110'))
X110.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg210', ports = ('in310', 'out410'))
X210 = CrossSection()
X210.add(width = wid, offset = -pit/2, layer = 1, name = 'wg10', ports = ('in210', 'out210'))
X210.add(width = wid, offset = pit/2, layer = 1, name = 'wg210',  ports = ('in510', 'out610'))

P110 = pp.straight(length = 0)
P210 = pp.straight(length = 0)
WG110 = P110.extrude(X110)
WG210 = P210.extrude(X210)

D = Device()
wg110 = D << WG110
wg210 = D << WG210
wg210.movex(7.5)

Xtrans10 = pp.transition(cross_section1 = X110,
                       cross_section2 = X210,
                       width_type = 'sine')
P310 = pp.straight(length = 0.5)
WG_trans10 = P310.extrude(Xtrans10)


Hairpin10 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P410 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans10 = P410.extrude(Xtrans10)
#11 crossSection for hairpin11 function  & hairpin11 (30 degrees turn, left side)
X111 = CrossSection()
X111.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg11', ports = ('in111', 'out111'))
X111.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg211', ports = ('in311', 'out411'))
X211 = CrossSection()
X211.add(width = wid, offset = -pit/2, layer = 1, name = 'wg11', ports = ('in211', 'out211'))
X211.add(width = wid, offset = pit/2, layer = 1, name = 'wg211',  ports = ('in511', 'out611'))

P111 = pp.straight(length = 0)
P211 = pp.straight(length = 0)
WG111 = P111.extrude(X111)
WG211 = P211.extrude(X211)

D = Device()
wg111 = D << WG111
wg211 = D << WG211
wg211.movex(7.5)

Xtrans11 = pp.transition(cross_section1 = X111,
                       cross_section2 = X211,
                       width_type = 'sine')
P311 = pp.straight(length = 0.5)
WG_trans11 = P311.extrude(Xtrans11)


Hairpin11 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P411 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans11 = P411.extrude(Xtrans11)
#12 crossSection for hairpin12 function  & hairpin12 (30 degrees turn, right side)
X112 = CrossSection()
X112.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg12', ports = ('in112', 'out112'))
X112.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg212', ports = ('in312', 'out412'))
X212 = CrossSection()
X212.add(width = wid, offset = -pit/2, layer = 1, name = 'wg12', ports = ('in212', 'out212'))
X212.add(width = wid, offset = pit/2, layer = 1, name = 'wg212',  ports = ('in512', 'out612'))

P112 = pp.straight(length = 0)
P212 = pp.straight(length = 0)
WG112 = P112.extrude(X112)
WG212 = P212.extrude(X212)

D = Device()
wg112 = D << WG112
wg212 = D << WG212
wg212.movex(7.5)

Xtrans12 = pp.transition(cross_section1 = X112,
                       cross_section2 = X212,
                       width_type = 'sine')
P312 = pp.straight(length = 0.5)
WG_trans12 = P312.extrude(Xtrans12)


Hairpin12 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P412 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans12 = P412.extrude(Xtrans12)
#13 crossSection for hairpin13 function  & hairpin13 (30 degrees turn, left side)
X113 = CrossSection()
X113.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg13', ports = ('in113', 'out113'))
X113.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg213', ports = ('in313', 'out413'))
X213 = CrossSection()
X213.add(width = wid, offset = -pit/2, layer = 1, name = 'wg13', ports = ('in213', 'out213'))
X213.add(width = wid, offset = pit/2, layer = 1, name = 'wg213',  ports = ('in513', 'out613'))

P113 = pp.straight(length = 0)
P213 = pp.straight(length = 0)
WG113 = P113.extrude(X113)
WG213 = P213.extrude(X213)

D = Device()
wg113 = D << WG113
wg213 = D << WG213
wg213.movex(7.5)

Xtrans13 = pp.transition(cross_section1 = X113,
                       cross_section2 = X213,
                       width_type = 'sine')
P313 = pp.straight(length = 0.5)
WG_trans13 = P313.extrude(Xtrans13)


Hairpin13 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P413 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans13 = P413.extrude(Xtrans13)
#14 crossSection for hairpin14 function  & hairpin14 (30 degrees turn, right side)
X114 = CrossSection()
X114.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg14', ports = ('in114', 'out114'))
X114.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg214', ports = ('in314', 'out414'))
X214 = CrossSection()
X214.add(width = wid, offset = -pit/2, layer = 1, name = 'wg14', ports = ('in214', 'out214'))
X214.add(width = wid, offset = pit/2, layer = 1, name = 'wg214',  ports = ('in514', 'out614'))

P114 = pp.straight(length = 0)
P214 = pp.straight(length = 0)
WG114 = P114.extrude(X114)
WG214 = P214.extrude(X214)

D = Device()
wg114 = D << WG114
wg214 = D << WG214
wg214.movex(7.5)

Xtrans14 = pp.transition(cross_section1 = X114,
                       cross_section2 = X214,
                       width_type = 'sine')
P314 = pp.straight(length = 0.5)
WG_trans14 = P314.extrude(Xtrans14)


Hairpin14 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P414 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans14 = P414.extrude(Xtrans14)
#15 crossSection for hairpin15 function  & hairpin15 (30 degrees turn, left side)
X115 = CrossSection()
X115.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg15', ports = ('in115', 'out115'))
X115.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg215', ports = ('in315', 'out415'))
X215 = CrossSection()
X215.add(width = wid, offset = -pit/2, layer = 1, name = 'wg15', ports = ('in215', 'out215'))
X215.add(width = wid, offset = pit/2, layer = 1, name = 'wg215',  ports = ('in515', 'out615'))

P115 = pp.straight(length = 0)
P215 = pp.straight(length = 0)
WG115 = P115.extrude(X115)
WG215 = P215.extrude(X215)

D = Device()
wg115 = D << WG115
wg215 = D << WG215
wg215.movex(7.5)

Xtrans15 = pp.transition(cross_section1 = X115,
                       cross_section2 = X215,
                       width_type = 'sine')
P315 = pp.straight(length = 0.5)
WG_trans15 = P315.extrude(Xtrans15)


Hairpin15 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P415 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans15 = P415.extrude(Xtrans15)
#16 crossSection for hairpin16 function  & hairpin16 (30 degrees turn, right side)
X116 = CrossSection()
X116.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg16', ports = ('in116', 'out116'))
X116.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg216', ports = ('in316', 'out416'))
X216 = CrossSection()
X216.add(width = wid, offset = -pit/2, layer = 1, name = 'wg16', ports = ('in216', 'out216'))
X216.add(width = wid, offset = pit/2, layer = 1, name = 'wg216',  ports = ('in516', 'out616'))

P116 = pp.straight(length = 0)
P216 = pp.straight(length = 0)
WG116 = P116.extrude(X116)
WG216 = P216.extrude(X216)

D = Device()
wg116 = D << WG116
wg216 = D << WG216
wg216.movex(7.5)

Xtrans16 = pp.transition(cross_section1 = X116,
                       cross_section2 = X216,
                       width_type = 'sine')
P316 = pp.straight(length = 0.5)
WG_trans16 = P316.extrude(Xtrans16)


Hairpin16 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P416 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans16 = P416.extrude(Xtrans16)
#17 crossSection for hairpin17 function  & hairpin17 (30 degrees turn, left side)
X117 = CrossSection()
X117.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg17', ports = ('in117', 'out117'))
X117.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg217', ports = ('in317', 'out417'))
X217 = CrossSection()
X217.add(width = wid, offset = -pit/2, layer = 1, name = 'wg17', ports = ('in217', 'out217'))
X217.add(width = wid, offset = pit/2, layer = 1, name = 'wg217',  ports = ('in517', 'out617'))

P117 = pp.straight(length = 0)
P217 = pp.straight(length = 0)
WG117 = P117.extrude(X117)
WG217 = P217.extrude(X217)

D = Device()
wg117 = D << WG117
wg217 = D << WG217
wg217.movex(7.5)

Xtrans17 = pp.transition(cross_section1 = X117,
                       cross_section2 = X217,
                       width_type = 'sine')
P317 = pp.straight(length = 0.5)
WG_trans17 = P317.extrude(Xtrans17)


Hairpin17 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P417 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans17 = P417.extrude(Xtrans17)
#18 crossSection for hairpin18 function  & hairpin18 (30 degrees turn, right side)
X118 = CrossSection()
X118.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg18', ports = ('in118', 'out118'))
X118.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg218', ports = ('in318', 'out418'))
X218 = CrossSection()
X218.add(width = wid, offset = -pit/2, layer = 1, name = 'wg18', ports = ('in218', 'out218'))
X218.add(width = wid, offset = pit/2, layer = 1, name = 'wg218',  ports = ('in518', 'out618'))

P118 = pp.straight(length = 0)
P218 = pp.straight(length = 0)
WG118 = P118.extrude(X118)
WG218 = P218.extrude(X218)

D = Device()
wg118 = D << WG118
wg218 = D << WG218
wg218.movex(7.5)

Xtrans18 = pp.transition(cross_section1 = X118,
                       cross_section2 = X218,
                       width_type = 'sine')
P318 = pp.straight(length = 0.5)
WG_trans18 = P318.extrude(Xtrans18)


Hairpin18 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P418 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans18 = P418.extrude(Xtrans18)
#19 crossSection for hairpin19 function  & hairpin19 (30 degrees turn, left side)
X119 = CrossSection()
X119.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg19', ports = ('in119', 'out119'))
X119.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg219', ports = ('in319', 'out419'))
X219 = CrossSection()
X219.add(width = wid, offset = -pit/2, layer = 1, name = 'wg19', ports = ('in219', 'out219'))
X219.add(width = wid, offset = pit/2, layer = 1, name = 'wg219',  ports = ('in519', 'out619'))

P119 = pp.straight(length = 0)
P219 = pp.straight(length = 0)
WG119 = P119.extrude(X119)
WG219 = P219.extrude(X219)

D = Device()
wg119 = D << WG119
wg219 = D << WG219
wg219.movex(7.5)

Xtrans19 = pp.transition(cross_section1 = X119,
                       cross_section2 = X219,
                       width_type = 'sine')
P319 = pp.straight(length = 0.5)
WG_trans19 = P319.extrude(Xtrans19)


Hairpin19 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P419 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans19 = P419.extrude(Xtrans19)
#20 crossSection for hairpin20 function  & hairpin20 (30 degrees turn, right side)
X120 = CrossSection()
X120.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg20', ports = ('in120', 'out120'))
X120.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg220', ports = ('in320', 'out420'))
X220 = CrossSection()
X220.add(width = wid, offset = -pit/2, layer = 1, name = 'wg20', ports = ('in220', 'out220'))
X220.add(width = wid, offset = pit/2, layer = 1, name = 'wg220',  ports = ('in520', 'out620'))

P120 = pp.straight(length = 0)
P220 = pp.straight(length = 0)
WG120 = P120.extrude(X120)
WG220 = P220.extrude(X220)

D = Device()
wg120 = D << WG120
wg220 = D << WG220
wg220.movex(7.5)

Xtrans20 = pp.transition(cross_section1 = X120,
                       cross_section2 = X220,
                       width_type = 'sine')
P320 = pp.straight(length = 0.5)
WG_trans20 = P320.extrude(Xtrans20)


Hairpin20 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P420 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans20 = P420.extrude(Xtrans20)
#21 crossSection for hairpin21 function  & hairpin21 (30 degrees turn, left side)
X121 = CrossSection()
X121.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg21', ports = ('in121', 'out121'))
X121.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg221', ports = ('in321', 'out421'))
X221 = CrossSection()
X221.add(width = wid, offset = -pit/2, layer = 1, name = 'wg21', ports = ('in221', 'out221'))
X221.add(width = wid, offset = pit/2, layer = 1, name = 'wg221',  ports = ('in521', 'out621'))

P121 = pp.straight(length = 0)
P221 = pp.straight(length = 0)
WG121 = P121.extrude(X121)
WG221 = P221.extrude(X221)

D = Device()
wg121 = D << WG121
wg221 = D << WG221
wg221.movex(7.5)

Xtrans21 = pp.transition(cross_section1 = X121,
                       cross_section2 = X221,
                       width_type = 'sine')
P321 = pp.straight(length = 0.5)
WG_trans21 = P321.extrude(Xtrans21)


Hairpin21 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P421 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans21 = P421.extrude(Xtrans21)
#22 crossSection for hairpin22 function  & hairpin22 (30 degrees turn, right side)
X122 = CrossSection()
X122.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg22', ports = ('in122', 'out122'))
X122.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg222', ports = ('in322', 'out422'))
X222 = CrossSection()
X222.add(width = wid, offset = -pit/2, layer = 1, name = 'wg22', ports = ('in222', 'out222'))
X222.add(width = wid, offset = pit/2, layer = 1, name = 'wg222',  ports = ('in522', 'out622'))

P122 = pp.straight(length = 0)
P222 = pp.straight(length = 0)
WG122 = P122.extrude(X122)
WG222 = P222.extrude(X222)

D = Device()
wg122 = D << WG122
wg222 = D << WG222
wg222.movex(7.5)

Xtrans22 = pp.transition(cross_section1 = X122,
                       cross_section2 = X222,
                       width_type = 'sine')
P322 = pp.straight(length = 0.5)
WG_trans22 = P322.extrude(Xtrans22)


Hairpin22 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P422 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans22 = P422.extrude(Xtrans22)
#23 crossSection for hairpin23 function  & hairpin23 (30 degrees turn, left side)
X123 = CrossSection()
X123.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg23', ports = ('in123', 'out123'))
X123.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg223', ports = ('in323', 'out423'))
X223 = CrossSection()
X223.add(width = wid, offset = -pit/2, layer = 1, name = 'wg23', ports = ('in223', 'out223'))
X223.add(width = wid, offset = pit/2, layer = 1, name = 'wg223',  ports = ('in523', 'out623'))

P123 = pp.straight(length = 0)
P223 = pp.straight(length = 0)
WG123 = P123.extrude(X123)
WG223 = P223.extrude(X223)

D = Device()
wg123 = D << WG123
wg223 = D << WG223
wg223.movex(7.5)

Xtrans23 = pp.transition(cross_section1 = X123,
                       cross_section2 = X223,
                       width_type = 'sine')
P323 = pp.straight(length = 0.5)
WG_trans23 = P323.extrude(Xtrans23)


Hairpin23 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P423 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans23 = P423.extrude(Xtrans23)
#24 crossSection for hairpin24 function  & hairpin24 (30 degrees turn, right side)
X124 = CrossSection()
X124.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg24', ports = ('in124', 'out124'))
X124.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg224', ports = ('in324', 'out424'))
X224 = CrossSection()
X224.add(width = wid, offset = -pit/2, layer = 1, name = 'wg24', ports = ('in224', 'out224'))
X224.add(width = wid, offset = pit/2, layer = 1, name = 'wg224',  ports = ('in524', 'out624'))

P124 = pp.straight(length = 0)
P224 = pp.straight(length = 0)
WG124 = P124.extrude(X124)
WG224 = P224.extrude(X224)

D = Device()
wg124 = D << WG124
wg224 = D << WG224
wg224.movex(7.5)

Xtrans24 = pp.transition(cross_section1 = X124,
                       cross_section2 = X224,
                       width_type = 'sine')
P324 = pp.straight(length = 0.5)
WG_trans24 = P324.extrude(Xtrans24)


Hairpin24 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P424 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans24 = P424.extrude(Xtrans24)
#25 crossSection for hairpin25 function  & hairpin25 (-30 degrees turn, right side,underneath )
X125 = CrossSection()
X125.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg25', ports = ('in125', 'out125'))
X125.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg225', ports = ('in325', 'out425'))
X225 = CrossSection()
X225.add(width = wid, offset = -pit/2, layer = 1, name = 'wg25', ports = ('in225', 'out225'))
X225.add(width = wid, offset = pit/2, layer = 1, name = 'wg225',  ports = ('in525', 'out625'))

P125 = pp.straight(length = 0)
P225 = pp.straight(length = 0)
WG125 = P125.extrude(X125)
WG225 = P225.extrude(X225)

D = Device()
wg125 = D << WG125
wg225 = D << WG225
wg225.movex(7.5)

Xtrans25 = pp.transition(cross_section1 = X125,
                       cross_section2 = X225,
                       width_type = 'sine')
P325 = pp.straight(length = 0.5)
WG_trans25 = P325.extrude(Xtrans25)


Hairpin25 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P425 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans25 = P425.extrude(Xtrans25)
#26 crossSection for hairpin26 function  & hairpin26 (-30 degrees turn, left side,underneath )
X126 = CrossSection()
X126.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg26', ports = ('in126', 'out126'))
X126.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg226', ports = ('in326', 'out426'))
X226 = CrossSection()
X226.add(width = wid, offset = -pit/2, layer = 1, name = 'wg26', ports = ('in226', 'out226'))
X226.add(width = wid, offset = pit/2, layer = 1, name = 'wg226',  ports = ('in526', 'out626'))

P126 = pp.straight(length = 0)
P226 = pp.straight(length = 0)
WG126 = P126.extrude(X126)
WG226 = P226.extrude(X226)

D = Device()
wg126 = D << WG126
wg226 = D << WG226
wg226.movex(7.5)

Xtrans26 = pp.transition(cross_section1 = X126,
                       cross_section2 = X226,
                       width_type = 'sine')
P326 = pp.straight(length = 0.5)
WG_trans26 = P326.extrude(Xtrans26)


Hairpin26 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P426 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans26 = P426.extrude(Xtrans26)
#27 crossSection for hairpin27 function  & hairpin27 (-30 degrees turn, right side,underneath )
X127 = CrossSection()
X127.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg27', ports = ('in127', 'out127'))
X127.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg227', ports = ('in327', 'out427'))
X227 = CrossSection()
X227.add(width = wid, offset = -pit/2, layer = 1, name = 'wg27', ports = ('in227', 'out227'))
X227.add(width = wid, offset = pit/2, layer = 1, name = 'wg227',  ports = ('in527', 'out627'))

P127 = pp.straight(length = 0)
P227 = pp.straight(length = 0)
WG127 = P127.extrude(X127)
WG227 = P227.extrude(X227)

D = Device()
wg127 = D << WG127
wg227 = D << WG227
wg227.movex(7.5)

Xtrans27 = pp.transition(cross_section1 = X127,
                       cross_section2 = X227,
                       width_type = 'sine')
P327 = pp.straight(length = 0.5)
WG_trans27 = P327.extrude(Xtrans27)


Hairpin27 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P427 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans27 = P427.extrude(Xtrans27)
#28 crossSection for hairpin28 function  & hairpin28 (-30 degrees turn, left side,underneath )
X128 = CrossSection()
X128.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg28', ports = ('in128', 'out128'))
X128.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg228', ports = ('in328', 'out428'))
X228 = CrossSection()
X228.add(width = wid, offset = -pit/2, layer = 1, name = 'wg28', ports = ('in228', 'out228'))
X228.add(width = wid, offset = pit/2, layer = 1, name = 'wg228',  ports = ('in528', 'out628'))

P128 = pp.straight(length = 0)
P228 = pp.straight(length = 0)
WG128 = P128.extrude(X128)
WG228 = P228.extrude(X228)

D = Device()
wg128 = D << WG128
wg228 = D << WG228
wg228.movex(7.5)

Xtrans28 = pp.transition(cross_section1 = X128,
                       cross_section2 = X228,
                       width_type = 'sine')
P328 = pp.straight(length = 0.5)
WG_trans28 = P328.extrude(Xtrans28)


Hairpin28 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P428 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans28 = P428.extrude(Xtrans28)
#29 crossSection for hairpin26 function  & hairpin26 (-30 degrees turn, right side,underneath )
X129 = CrossSection()
X129.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg29', ports = ('in129', 'out129'))
X129.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg229', ports = ('in329', 'out429'))
X229 = CrossSection()
X229.add(width = wid, offset = -pit/2, layer = 1, name = 'wg29', ports = ('in229', 'out229'))
X229.add(width = wid, offset = pit/2, layer = 1, name = 'wg229',  ports = ('in529', 'out629'))

P129 = pp.straight(length = 0)
P229 = pp.straight(length = 0)
WG129 = P129.extrude(X129)
WG229 = P229.extrude(X229)

D = Device()
wg129 = D << WG129
wg229 = D << WG229
wg229.movex(7.5)

Xtrans29 = pp.transition(cross_section1 = X129,
                       cross_section2 = X229,
                       width_type = 'sine')
P329 = pp.straight(length = 0.5)
WG_trans29 = P329.extrude(Xtrans29)


Hairpin29 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P429 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans29 = P429.extrude(Xtrans29)
#30 crossSection for hairpin30 function  & hairpin30 (-30 degrees turn, left side,underneath )
X130 = CrossSection()
X130.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg30', ports = ('in130', 'out130'))
X130.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg230', ports = ('in330', 'out430'))
X230 = CrossSection()
X230.add(width = wid, offset = -pit/2, layer = 1, name = 'wg30', ports = ('in230', 'out230'))
X230.add(width = wid, offset = pit/2, layer = 1, name = 'wg230',  ports = ('in530', 'out630'))

P130 = pp.straight(length = 0)
P230 = pp.straight(length = 0)
WG130 = P130.extrude(X130)
WG230 = P230.extrude(X230)

D = Device()
wg130 = D << WG130
wg230 = D << WG230
wg230.movex(7.5)

Xtrans30 = pp.transition(cross_section1 = X130,
                       cross_section2 = X230,
                       width_type = 'sine')
P330 = pp.straight(length = 0.5)
WG_trans30 = P330.extrude(Xtrans30)


Hairpin30 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P430 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans30 = P430.extrude(Xtrans30)
#31 crossSection for hairpin31 function  & hairpin31 (-30 degrees turn, right side,underneath )
X131 = CrossSection()
X131.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg31', ports = ('in131', 'out131'))
X131.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg231', ports = ('in331', 'out431'))
X231 = CrossSection()
X231.add(width = wid, offset = -pit/2, layer = 1, name = 'wg31', ports = ('in231', 'out231'))
X231.add(width = wid, offset = pit/2, layer = 1, name = 'wg231',  ports = ('in531', 'out631'))

P131 = pp.straight(length = 0)
P231 = pp.straight(length = 0)
WG131 = P131.extrude(X131)
WG231 = P231.extrude(X231)

D = Device()
wg131 = D << WG131
wg231 = D << WG231
wg231.movex(7.5)

Xtrans31 = pp.transition(cross_section1 = X131,
                       cross_section2 = X231,
                       width_type = 'sine')
P331 = pp.straight(length = 0.5)
WG_trans31 = P331.extrude(Xtrans31)


Hairpin31 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P431 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans31 = P431.extrude(Xtrans31)
#32 crossSection for hairpin32 function  & hairpin32 (-30 degrees turn, left side,underneath )
X132 = CrossSection()
X132.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg32', ports = ('in132', 'out132'))
X132.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg232', ports = ('in332', 'out432'))
X232 = CrossSection()
X232.add(width = wid, offset = -pit/2, layer = 1, name = 'wg32', ports = ('in232', 'out232'))
X232.add(width = wid, offset = pit/2, layer = 1, name = 'wg232',  ports = ('in532', 'out632'))

P132 = pp.straight(length = 0)
P232 = pp.straight(length = 0)
WG132 = P132.extrude(X132)
WG232 = P232.extrude(X232)

D = Device()
wg132 = D << WG132
wg232 = D << WG232
wg232.movex(7.5)

Xtrans32 = pp.transition(cross_section1 = X132,
                       cross_section2 = X232,
                       width_type = 'sine')
P332 = pp.straight(length = 0.5)
WG_trans32 = P332.extrude(Xtrans32)


Hairpin32 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P432 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans32 = P432.extrude(Xtrans32)

#33 crossSection for hairpin33 function  & hairpin33 (-30 degrees turn, right side,underneath )
X133 = CrossSection()
X133.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg33', ports = ('in133', 'out133'))
X133.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg233', ports = ('in333', 'out433'))
X233 = CrossSection()
X233.add(width = wid, offset = -pit/2, layer = 1, name = 'wg33', ports = ('in233', 'out233'))
X233.add(width = wid, offset = pit/2, layer = 1, name = 'wg233',  ports = ('in533', 'out633'))

P133 = pp.straight(length = 0)
P233 = pp.straight(length = 0)
WG133 = P133.extrude(X133)
WG233 = P233.extrude(X233)

D = Device()
wg133 = D << WG133
wg233 = D << WG233
wg233.movex(7.5)

Xtrans33 = pp.transition(cross_section1 = X133,
                       cross_section2 = X233,
                       width_type = 'sine')
P333 = pp.straight(length = 0.5)
WG_trans33 = P333.extrude(Xtrans33)


Hairpin33 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P433 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans33 = P433.extrude(Xtrans33)
#34 crossSection for hairpin34 function  & hairpin34 (-30 degrees turn, left side,underneath )
X134 = CrossSection()
X134.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg34', ports = ('in134', 'out134'))
X134.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg234', ports = ('in334', 'out434'))
X234 = CrossSection()
X234.add(width = wid, offset = -pit/2, layer = 1, name = 'wg34', ports = ('in234', 'out234'))
X234.add(width = wid, offset = pit/2, layer = 1, name = 'wg234',  ports = ('in534', 'out634'))

P134 = pp.straight(length = 0)
P234 = pp.straight(length = 0)
WG134 = P134.extrude(X134)
WG234 = P234.extrude(X234)

D = Device()
wg134 = D << WG134
wg234 = D << WG234
wg234.movex(7.5)

Xtrans34 = pp.transition(cross_section1 = X134,
                       cross_section2 = X234,
                       width_type = 'sine')
P334 = pp.straight(length = 0.5)
WG_trans34 = P334.extrude(Xtrans34)


Hairpin34 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P434 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans34 = P434.extrude(Xtrans34)
#35 crossSection for hairpin35 function  & hairpin35 (-30 degrees turn, right side,underneath )
X135 = CrossSection()
X135.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg35', ports = ('in135', 'out135'))
X135.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg235', ports = ('in335', 'out435'))
X235 = CrossSection()
X235.add(width = wid, offset = -pit/2, layer = 1, name = 'wg35', ports = ('in235', 'out235'))
X235.add(width = wid, offset = pit/2, layer = 1, name = 'wg235',  ports = ('in535', 'out635'))

P135 = pp.straight(length = 0)
P235 = pp.straight(length = 0)
WG135 = P135.extrude(X135)
WG235 = P235.extrude(X235)

D = Device()
wg135 = D << WG135
wg235 = D << WG235
wg235.movex(7.5)

Xtrans35 = pp.transition(cross_section1 = X135,
                       cross_section2 = X235,
                       width_type = 'sine')
P335 = pp.straight(length = 0.5)
WG_trans35 = P335.extrude(Xtrans35)


Hairpin35 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P435 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans35 = P435.extrude(Xtrans35)
#36 crossSection for hairpin26 function  & hairpin26 (-30 degrees turn, left side,underneath )
X136 = CrossSection()
X136.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg36', ports = ('in136', 'out136'))
X136.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg236', ports = ('in336', 'out436'))
X236 = CrossSection()
X236.add(width = wid, offset = -pit/2, layer = 1, name = 'wg36', ports = ('in236', 'out236'))
X236.add(width = wid, offset = pit/2, layer = 1, name = 'wg236',  ports = ('in536', 'out636'))

P136 = pp.straight(length = 0)
P236 = pp.straight(length = 0)
WG136 = P136.extrude(X136)
WG236 = P236.extrude(X236)

D = Device()
wg136 = D << WG136
wg236 = D << WG236
wg236.movex(7.5)

Xtrans36 = pp.transition(cross_section1 = X136,
                       cross_section2 = X236,
                       width_type = 'sine')
P336 = pp.straight(length = 0.5)
WG_trans36 = P336.extrude(Xtrans36)


Hairpin36 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P436 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans36 = P436.extrude(Xtrans36)
#37 crossSection for hairpin37 function  & hairpin37 (-30 degrees turn, right side,underneath )
X137 = CrossSection()
X137.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg37', ports = ('in137', 'out137'))
X137.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg237', ports = ('in337', 'out437'))
X237 = CrossSection()
X237.add(width = wid, offset = -pit/2, layer = 1, name = 'wg37', ports = ('in237', 'out237'))
X237.add(width = wid, offset = pit/2, layer = 1, name = 'wg237',  ports = ('in537', 'out637'))

P137 = pp.straight(length = 0)
P237 = pp.straight(length = 0)
WG137 = P137.extrude(X137)
WG237 = P237.extrude(X237)

D = Device()
wg137 = D << WG137
wg237 = D << WG237
wg237.movex(7.5)

Xtrans37 = pp.transition(cross_section1 = X137,
                       cross_section2 = X237,
                       width_type = 'sine')
P337 = pp.straight(length = 0.5)
WG_trans37 = P337.extrude(Xtrans37)


Hairpin37 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P437 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans37 = P437.extrude(Xtrans37)
#38 crossSection for hairpin38 function  & hairpin38 (-30 degrees turn, left side,underneath )
X138 = CrossSection()
X138.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg38', ports = ('in138', 'out138'))
X138.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg238', ports = ('in338', 'out438'))
X238 = CrossSection()
X238.add(width = wid, offset = -pit/2, layer = 1, name = 'wg38', ports = ('in238', 'out238'))
X238.add(width = wid, offset = pit/2, layer = 1, name = 'wg238',  ports = ('in538', 'out638'))

P138 = pp.straight(length = 0)
P238 = pp.straight(length = 0)
WG138 = P138.extrude(X138)
WG238 = P238.extrude(X238)

D = Device()
wg138 = D << WG138
wg238 = D << WG238
wg238.movex(7.5)

Xtrans38 = pp.transition(cross_section1 = X138,
                       cross_section2 = X238,
                       width_type = 'sine')
P338 = pp.straight(length = 0.5)
WG_trans38 = P338.extrude(Xtrans38)


Hairpin38 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P438 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans38 = P438.extrude(Xtrans38)
#39 crossSection for hairpin39 function  & hairpin39 (-30 degrees turn, right side,underneath )
X139 = CrossSection()
X139.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg39', ports = ('in139', 'out139'))
X139.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg239', ports = ('in339', 'out439'))
X239 = CrossSection()
X239.add(width = wid, offset = -pit/2, layer = 1, name = 'wg39', ports = ('in239', 'out239'))
X239.add(width = wid, offset = pit/2, layer = 1, name = 'wg239',  ports = ('in539', 'out639'))

P139 = pp.straight(length = 0)
P239 = pp.straight(length = 0)
WG139 = P139.extrude(X139)
WG239 = P239.extrude(X239)

D = Device()
wg139 = D << WG139
wg239 = D << WG239
wg239.movex(7.5)

Xtrans39 = pp.transition(cross_section1 = X139,
                       cross_section2 = X239,
                       width_type = 'sine')
P339 = pp.straight(length = 0.5)
WG_trans39 = P339.extrude(Xtrans39)


Hairpin39 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P439 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans39 = P439.extrude(Xtrans39)

#40 crossSection for hairpin40 function  & hairpin40 (-30 degrees turn, left side,underneath )
X140 = CrossSection()
X140.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg40', ports = ('in140', 'out140'))
X140.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg240', ports = ('in340', 'out440'))
X240 = CrossSection()
X240.add(width = wid, offset = -pit/2, layer = 1, name = 'wg40', ports = ('in240', 'out240'))
X240.add(width = wid, offset = pit/2, layer = 1, name = 'wg240',  ports = ('in540', 'out640'))

P140 = pp.straight(length = 0)
P240 = pp.straight(length = 0)
WG140 = P140.extrude(X140)
WG240 = P240.extrude(X240)

D = Device()
wg140 = D << WG140
wg240 = D << WG240
wg240.movex(7.5)

Xtrans40 = pp.transition(cross_section1 = X140,
                       cross_section2 = X240,
                       width_type = 'sine')
P340 = pp.straight(length = 0.5)
WG_trans40 = P340.extrude(Xtrans40)


Hairpin40 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P440 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans40 = P440.extrude(Xtrans40)
#41 crossSection for hairpin41 function  & hairpin41 (-30 degrees turn, right side,underneath )
X141 = CrossSection()
X141.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg41', ports = ('in141', 'out141'))
X141.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg241', ports = ('in341', 'out441'))
X241 = CrossSection()
X241.add(width = wid, offset = -pit/2, layer = 1, name = 'wg41', ports = ('in241', 'out241'))
X241.add(width = wid, offset = pit/2, layer = 1, name = 'wg241',  ports = ('in541', 'out641'))

P141 = pp.straight(length = 0)
P241 = pp.straight(length = 0)
WG141 = P141.extrude(X141)
WG241 = P241.extrude(X241)

D = Device()
wg141 = D << WG141
wg241 = D << WG241
wg241.movex(7.5)

Xtrans41 = pp.transition(cross_section1 = X141,
                       cross_section2 = X241,
                       width_type = 'sine')
P341 = pp.straight(length = 0.5)
WG_trans41 = P341.extrude(Xtrans41)


Hairpin41 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P441 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans41 = P441.extrude(Xtrans41)
#42 crossSection for hairpin42 function  & hairpin42 (-30 degrees turn, left side,underneath )
X142 = CrossSection()
X142.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg42', ports = ('in142', 'out142'))
X142.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg242', ports = ('in342', 'out442'))
X242 = CrossSection()
X242.add(width = wid, offset = -pit/2, layer = 1, name = 'wg42', ports = ('in242', 'out242'))
X242.add(width = wid, offset = pit/2, layer = 1, name = 'wg242',  ports = ('in542', 'out642'))

P142 = pp.straight(length = 0)
P242 = pp.straight(length = 0)
WG142 = P142.extrude(X142)
WG242 = P242.extrude(X242)

D = Device()
wg142 = D << WG142
wg242 = D << WG242
wg242.movex(7.5)

Xtrans42 = pp.transition(cross_section1 = X142,
                       cross_section2 = X242,
                       width_type = 'sine')
P342 = pp.straight(length = 0.5)
WG_trans42 = P342.extrude(Xtrans42)


Hairpin42 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P442 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans42 = P442.extrude(Xtrans42)
#43 crossSection for hairpin43 function  & hairpin43 (-30 degrees turn, right side,underneath )
X143 = CrossSection()
X143.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg43', ports = ('in143', 'out143'))
X143.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg243', ports = ('in343', 'out443'))
X243 = CrossSection()
X243.add(width = wid, offset = -pit/2, layer = 1, name = 'wg43', ports = ('in243', 'out243'))
X243.add(width = wid, offset = pit/2, layer = 1, name = 'wg243',  ports = ('in543', 'out643'))

P143 = pp.straight(length = 0)
P243 = pp.straight(length = 0)
WG143 = P143.extrude(X143)
WG243 = P243.extrude(X243)

D = Device()
wg143 = D << WG143
wg243 = D << WG243
wg243.movex(7.5)

Xtrans43 = pp.transition(cross_section1 = X143,
                       cross_section2 = X243,
                       width_type = 'sine')
P343 = pp.straight(length = 0.5)
WG_trans43 = P343.extrude(Xtrans43)


Hairpin43 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P443 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans43 = P443.extrude(Xtrans43)
#44 crossSection for hairpin44 function  & hairpin44 (-30 degrees turn, left side,underneath )
X144 = CrossSection()
X144.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg44', ports = ('in144', 'out144'))
X144.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg244', ports = ('in344', 'out444'))
X244 = CrossSection()
X244.add(width = wid, offset = -pit/2, layer = 1, name = 'wg44', ports = ('in244', 'out244'))
X244.add(width = wid, offset = pit/2, layer = 1, name = 'wg244',  ports = ('in544', 'out644'))

P144 = pp.straight(length = 0)
P244 = pp.straight(length = 0)
WG144 = P144.extrude(X144)
WG244 = P244.extrude(X244)

D = Device()
wg144 = D << WG144
wg244 = D << WG244
wg244.movex(7.5)

Xtrans44 = pp.transition(cross_section1 = X144,
                       cross_section2 = X244,
                       width_type = 'sine')
P344 = pp.straight(length = 0.5)
WG_trans44 = P344.extrude(Xtrans44)


Hairpin44 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P444 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans44 = P444.extrude(Xtrans44)
#45 crossSection for hairpin45 function  & hairpin45 (-30 degrees turn, right side,underneath )
X145 = CrossSection()
X145.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg45', ports = ('in145', 'out145'))
X145.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg245', ports = ('in345', 'out445'))
X245 = CrossSection()
X245.add(width = wid, offset = -pit/2, layer = 1, name = 'wg45', ports = ('in245', 'out245'))
X245.add(width = wid, offset = pit/2, layer = 1, name = 'wg245',  ports = ('in545', 'out645'))

P145 = pp.straight(length = 0)
P245 = pp.straight(length = 0)
WG145 = P145.extrude(X145)
WG245 = P245.extrude(X245)

D = Device()
wg145 = D << WG145
wg245 = D << WG245
wg245.movex(7.5)

Xtrans45 = pp.transition(cross_section1 = X145,
                       cross_section2 = X245,
                       width_type = 'sine')
P345 = pp.straight(length = 0.5)
WG_trans45 = P345.extrude(Xtrans45)


Hairpin45 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P445 = pp.euler(radius = 2, angle = -30, p = 0.1, use_eff = False)
WG_trans45 = P445.extrude(Xtrans45)
#46 crossSection for hairpin46 function  & hairpin46 (-30 degrees turn, left side,underneath )
X146 = CrossSection()
X146.add(width = 0.1, offset = -0.1, layer = 1, name = 'wg46', ports = ('in146', 'out146'))
X146.add(width = 0.1, offset = 0.1, layer = 1, name = 'wg246', ports = ('in346', 'out446'))
X246 = CrossSection()
X246.add(width = wid, offset = -pit/2, layer = 1, name = 'wg46', ports = ('in246', 'out246'))
X246.add(width = wid, offset = pit/2, layer = 1, name = 'wg246',  ports = ('in546', 'out646'))

P146 = pp.straight(length = 0)
P246 = pp.straight(length = 0)
WG146 = P146.extrude(X146)
WG246 = P246.extrude(X246)

D = Device()
wg146 = D << WG146
wg246 = D << WG246
wg246.movex(7.5)

Xtrans46 = pp.transition(cross_section1 = X146,
                       cross_section2 = X246,
                       width_type = 'sine')
P346 = pp.straight(length = 0.5)
WG_trans46 = P346.extrude(Xtrans46)


Hairpin46 = pg.optimal_hairpin(width = wid, pitch = pit, length = lenn,
    turn_ratio = 3, num_pts = 5000, layer = 1)
P446 = pp.euler(radius = 2, angle = 30, p = 0.1, use_eff = False)
WG_trans46 = P446.extrude(Xtrans46)
#create a device with all references
D = Device()
wgt = D << WG_trans
Hairpin1 = D << Hairpin
wgt3 = D << WG_trans3
Hairpin3 = D << Hairpin3
Hairpin4 = D << Hairpin4
wgt4 = D << WG_trans4
wgt2 = D << WG_trans2
Hairpin2 = D << Hairpin2
wgt5 = D << WG_trans5
Hairpin5 = D << Hairpin5
wgt6 = D << WG_trans6
Hairpin6 = D << Hairpin6
wgt7 = D << WG_trans7
Hairpin7 = D << Hairpin7
wgt8 = D << WG_trans8
Hairpin8 = D << Hairpin8
wgt9 = D << WG_trans9
Hairpin9 = D << Hairpin9
wgt10 = D << WG_trans10
Hairpin10 = D << Hairpin10
wgt11 = D << WG_trans11
Hairpin11 = D << Hairpin11
wgt12 = D << WG_trans12
Hairpin12 = D << Hairpin12
wgt13 = D << WG_trans13
Hairpin13 = D << Hairpin13
wgt14 = D << WG_trans14
Hairpin14 = D << Hairpin14
wgt15 = D << WG_trans15
Hairpin15 = D << Hairpin15
wgt16 = D << WG_trans16
Hairpin16 = D << Hairpin16
wgt17 = D << WG_trans17
Hairpin17 = D << Hairpin17
wgt18 = D << WG_trans18
Hairpin18 = D << Hairpin18
wgt19 = D << WG_trans19
Hairpin19 = D << Hairpin19
wgt20 = D << WG_trans20
Hairpin20 = D << Hairpin20
wgt21 = D << WG_trans21
Hairpin21 = D << Hairpin21
wgt22 = D << WG_trans22
Hairpin22 = D << Hairpin22
wgt23 = D << WG_trans23
Hairpin23 = D << Hairpin23
wgt24 = D << WG_trans24
Hairpin24 = D << Hairpin24
wgt25 = D << WG_trans25
Hairpin25 = D << Hairpin25
wgt26 = D << WG_trans26
Hairpin26 = D << Hairpin26
wgt27 = D << WG_trans27
Hairpin27 = D << Hairpin27
wgt28 = D << WG_trans28
Hairpin28 = D << Hairpin28
wgt29 = D << WG_trans29
Hairpin29 = D << Hairpin29
wgt30 = D << WG_trans30
Hairpin30 = D << Hairpin30
wgt31 = D << WG_trans31
Hairpin31 = D << Hairpin31
wgt32 = D << WG_trans32
Hairpin32 = D << Hairpin32
wgt33 = D << WG_trans33
Hairpin33 = D << Hairpin33
wgt34 = D << WG_trans34
Hairpin34 = D << Hairpin34
wgt35 = D << WG_trans35
Hairpin35 = D << Hairpin35
wgt36 = D << WG_trans36
Hairpin36 = D << Hairpin36
wgt37 = D << WG_trans37
Hairpin37 = D << Hairpin37
wgt38 = D << WG_trans38
Hairpin38 = D << Hairpin38
wgt39 = D << WG_trans39
Hairpin39 = D << Hairpin39
wgt40 = D << WG_trans40
Hairpin40 = D << Hairpin40
wgt41 = D << WG_trans41
Hairpin41 = D << Hairpin41
wgt42 = D << WG_trans42
Hairpin42 = D << Hairpin42
wgt43 = D << WG_trans43
Hairpin43 = D << Hairpin43
wgt44 = D << WG_trans44
Hairpin44 = D << Hairpin44
wgt45 = D << WG_trans45
Hairpin45 = D << Hairpin45
wgt46 = D << WG_trans46
Hairpin46 = D << Hairpin46

Hairpin2.rotate(180)
Hairpin4.rotate(30)
Hairpin3.rotate(150)
#Hairpin3.mirror(p1 = [1,1], p2 = [1,3])
#wgt3.mirror(p1 = [1,1], p2 = [1,3])
Hairpin5.rotate(150)
#Hairpin5.mirror(p1 = [1,1], p2 = [1,3])
#wgt5.mirror(p1 = [1,1], p2 = [1,3])
Hairpin6.rotate(30)
Hairpin7.rotate(150)
#Hairpin7.mirror(p1 = [1,1], p2 = [1,3])
#wgt7.mirror(p1 = [1,1], p2 = [1,3])
Hairpin8.rotate(30)
Hairpin9.rotate(150)
#Hairpin9.mirror(p1 = [1,1], p2 = [1,3])
#wgt9.mirror(p1 = [1,1], p2 = [1,3])
Hairpin10.rotate(30)
Hairpin11.rotate(150)
#Hairpin11.mirror(p1 = [1,1], p2 = [1,3])
#wgt11.mirror(p1 = [1,1], p2 = [1,3])
Hairpin12.rotate(30)

Hairpin13.rotate(150)
#Hairpin13.mirror(p1 = [1,1], p2 = [1,3])
#wgt13.mirror(p1 = [1,1], p2 = [1,3])
Hairpin14.rotate(30)
Hairpin15.rotate(150)
#Hairpin15.mirror(p1 = [1,1], p2 = [1,3])
#wgt15.mirror(p1 = [1,1], p2 = [1,3])
Hairpin16.rotate(30)
Hairpin17.rotate(150)
#Hairpin17.mirror(p1 = [1,1], p2 = [1,3])
#wgt17.mirror(p1 = [1,1], p2 = [1,3])
Hairpin18.rotate(30)
Hairpin19.rotate(150)
#Hairpin19.mirror(p1 = [1,1], p2 = [1,3])
#wgt19.mirror(p1 = [1,1], p2 = [1,3])
Hairpin20.rotate(30)

Hairpin21.rotate(150)
#Hairpin21.mirror(p1 = [1,1], p2 = [1,3])
#wgt21.mirror(p1 = [1,1], p2 = [1,3])
Hairpin22.rotate(30)
Hairpin23.rotate(150)
#Hairpin23.mirror(p1 = [1,1], p2 = [1,3])
#wgt23.mirror(p1 = [1,1], p2 = [1,3])
Hairpin24.rotate(30)
Hairpin25.rotate(-30)

#
Hairpin26.rotate(210)
#Hairpin26.mirror(p1 = [1,1], p2 = [1,3])
#wgt26.mirror(p1 = [1,1], p2 = [1,3])
Hairpin27.rotate(-30)
Hairpin28.rotate(210)
#Hairpin28.mirror(p1 = [1,1], p2 = [1,3])
#wgt28.mirror(p1 = [1,1], p2 = [1,3])
Hairpin29.rotate(-30)
Hairpin30.rotate(210)
#Hairpin30.mirror(p1 = [1,1], p2 = [1,3])
#wgt30.mirror(p1 = [1,1], p2 = [1,3])
Hairpin31.rotate(-30)

Hairpin32.rotate(210)
#Hairpin32.mirror(p1 = [1,1], p2 = [1,3])
#wgt32.mirror(p1 = [1,1], p2 = [1,3])
Hairpin33.rotate(-30)
Hairpin34.rotate(210)
#Hairpin34.mirror(p1 = [1,1], p2 = [1,3])
#wgt34.mirror(p1 = [1,1], p2 = [1,3])
Hairpin35.rotate(-30)
Hairpin36.rotate(210)
#Hairpin36.mirror(p1 = [1,1], p2 = [1,3])
#wgt36.mirror(p1 = [1,1], p2 = [1,3])
Hairpin37.rotate(-30)
Hairpin38.rotate(210)
#Hairpin38.mirror(p1 = [1,1], p2 = [1,3])
#wgt38.mirror(p1 = [1,1], p2 = [1,3])
Hairpin39.rotate(-30)
Hairpin40.rotate(210)
#Hairpin40.mirror(p1 = [1,1], p2 = [1,3])
#wgt40.mirror(p1 = [1,1], p2 = [1,3])
Hairpin41.rotate(-30)
Hairpin42.rotate(210)
#Hairpin42.mirror(p1 = [1,1], p2 = [1,3])
#wgt42.mirror(p1 = [1,1], p2 = [1,3])
Hairpin43.rotate(-30)
Hairpin44.rotate(210)
#Hairpin44.mirror(p1 = [1,1], p2 = [1,3])
#wgt44.mirror(p1 = [1,1], p2 = [1,3])
Hairpin45.rotate(-30)
Hairpin46.rotate(210)
#Hairpin46.mirror(p1 = [1,1], p2 = [1,3])
#wgt46.mirror(p1 = [1,1], p2 = [1,3])

#creating polygons
Pol = pg.ramp(length = 17, width1 = 0.1, width2 = 0.1, layer = 1)
pol1 = D.add_ref(Pol)
Pol2 = pg.ramp(length = 16.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol2 = D.add_ref(Pol2)
Pol3 = pg.ramp(length = 16, width1 = 0.1, width2 = 0.1, layer = 1)
pol3 = D.add_ref(Pol3)
Pol4 = pg.ramp(length = 15.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol4 = D.add_ref(Pol4)
Pol5 = pg.ramp(length = 16.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol5 = D.add_ref(Pol5)
Pol6 = pg.ramp(length = 14.6, width1 = 0.1, width2 = 0.1, layer = 1)
pol6 = D.add_ref(Pol6)
Pol7 = pg.ramp(length = 13.9, width1 = 0.1, width2 = 0.1, layer = 1)
pol7 = D.add_ref(Pol7)
Pol8 = pg.ramp(length = 13.2, width1 = 0.1, width2 = 0.1, layer = 1)
pol8 = D.add_ref(Pol8)
Pol9 = pg.ramp(length = 12.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol9 = D.add_ref(Pol9)
Pol10 = pg.ramp(length = 11.8, width1 = 0.1, width2 = 0.1, layer = 1)
pol10 = D.add_ref(Pol10)
Pol11 = pg.ramp(length = 11.1, width1 = 0.1, width2 = 0.1, layer = 1)
pol11 = D.add_ref(Pol11)
Pol12 = pg.ramp(length = 10.4, width1 = 0.1, width2 = 0.1, layer = 1)
pol12 = D.add_ref(Pol12)
Pol13 = pg.ramp(length = 9.7, width1 = 0.1, width2 = 0.1, layer = 1)
pol13 = D.add_ref(Pol13)
Pol14 = pg.ramp(length = 9, width1 = 0.1, width2 = 0.1, layer = 1)
pol14 = D.add_ref(Pol14)
Pol15 = pg.ramp(length = 8.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol15 = D.add_ref(Pol15)
Pol16 = pg.ramp(length = 7.6, width1 = 0.1, width2 = 0.1, layer = 1)
pol16 = D.add_ref(Pol16)
Pol17 = pg.ramp(length = 6.9, width1 = 0.1, width2 = 0.1, layer = 1)
pol17 = D.add_ref(Pol17)
Pol18 = pg.ramp(length = 6.2, width1 = 0.1, width2 = 0.1, layer = 1)
pol18 = D.add_ref(Pol18)
Pol19 = pg.ramp(length = 5.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol19 = D.add_ref(Pol19)
Pol20 = pg.ramp(length = 4.8, width1 = 0.1, width2 = 0.1, layer = 1)
pol20 = D.add_ref(Pol20)
Pol21 = pg.ramp(length = 4.1, width1 = 0.1, width2 = 0.1, layer = 1)
pol21 = D.add_ref(Pol21)
Pol22 = pg.ramp(length = 3.4, width1 = 0.1, width2 = 0.1, layer = 1)
pol22 = D.add_ref(Pol22)
Pol23 = pg.ramp(length = 2.7, width1 = 0.1, width2 = 0.1, layer = 1)
pol23 = D.add_ref(Pol23)
Pol24 = pg.ramp(length = 2, width1 = 0.1, width2 = 0.1, layer = 1)
pol24 = D.add_ref(Pol24)
Pol25 = pg.ramp(length = 1.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol25 = D.add_ref(Pol25)
Pol26 = pg.ramp(length = 16, width1 = 0.1, width2 = 0.1, layer = 1)
pol26 = D.add_ref(Pol26)
Pol27 = pg.ramp(length = 15.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol27 = D.add_ref(Pol27)
Pol28 = pg.ramp(length = 14.6, width1 = 0.1, width2 = 0.1, layer = 1)
pol28 = D.add_ref(Pol28)
Pol29 = pg.ramp(length = 13.9, width1 = 0.1, width2 = 0.1, layer = 1)
pol29 = D.add_ref(Pol29)
Pol30 = pg.ramp(length = 13.2, width1 = 0.1, width2 = 0.1, layer = 1)
pol30 = D.add_ref(Pol30)
Pol31 = pg.ramp(length = 12.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol31 = D.add_ref(Pol31)
Pol32 = pg.ramp(length = 11.8, width1 = 0.1, width2 = 0.1, layer = 1)
pol32 = D.add_ref(Pol32)
Pol33 = pg.ramp(length = 11.1, width1 = 0.1, width2 = 0.1, layer = 1)
pol33 = D.add_ref(Pol33)
Pol34 = pg.ramp(length = 10.4, width1 = 0.1, width2 = 0.1, layer = 1)
pol34 = D.add_ref(Pol34)
Pol35 = pg.ramp(length = 9.7, width1 = 0.1, width2 = 0.1, layer = 1)
pol35 = D.add_ref(Pol35)
Pol36 = pg.ramp(length = 9, width1 = 0.1, width2 = 0.1, layer = 1)
pol36 = D.add_ref(Pol36)
Pol37 = pg.ramp(length = 8.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol37 = D.add_ref(Pol37)
Pol38 = pg.ramp(length = 7.6, width1 = 0.1, width2 = 0.1, layer = 1)
pol38 = D.add_ref(Pol38)
Pol39 = pg.ramp(length = 6.9, width1 = 0.1, width2 = 0.1, layer = 1)
pol39 = D.add_ref(Pol39)
Pol40 = pg.ramp(length = 6.2, width1 = 0.1, width2 = 0.1, layer = 1)
pol40 = D.add_ref(Pol40)
Pol41 = pg.ramp(length = 5.5, width1 = 0.1, width2 = 0.1, layer = 1)
pol41 = D.add_ref(Pol41)
Pol42 = pg.ramp(length = 4.8, width1 = 0.1, width2 = 0.1, layer = 1)
pol42 = D.add_ref(Pol42)
Pol43 = pg.ramp(length = 4.1, width1 = 0.1, width2 = 0.1, layer = 1)
pol43 = D.add_ref(Pol43)
Pol44 = pg.ramp(length = 3.4, width1 = 0.1, width2 = 0.1, layer = 1)
pol44 = D.add_ref(Pol44)
Pol45 = pg.ramp(length = 2.7, width1 = 0.1, width2 = 0.1, layer = 1)
pol45 = D.add_ref(Pol45)
Pol46 = pg.ramp(length = 2, width1 = 0.1, width2 = 0.1, layer = 1)
pol46 = D.add_ref(Pol46)
Pol47 = pg.ramp(length = 1.3, width1 = 0.1, width2 = 0.1, layer = 1)
pol47 = D.add_ref(Pol47)


#connect
wgt.connect('out1', Hairpin1.ports[1])
wgt.connect('out4', Hairpin1.ports[2])
pol1.connect(2, wgt.ports['in5'])
pol2.connect(2, wgt.ports['in2'])
wgt2.connect('in52', pol1.ports[1])
Hairpin2.connect(2, wgt2.ports['out42'])
wgt3.connect('in23', pol2.ports[1])
Hairpin3.connect(1,wgt3.ports['out13'] )
pol3.connect(2, wgt3.ports['in53'])
wgt4.connect('in54', pol3.ports[1])
Hairpin4.connect(2, wgt4.ports['out44'] )
pol4.connect(2, wgt4.ports['in24'])
pol5.connect(2, wgt2.ports['in22'])
wgt5.connect('in25', pol4.ports[1])
pol6.connect(2, wgt5.ports['in55'])
Hairpin5.connect(1, wgt5.ports['out15'] )
wgt6.connect('in56', pol6.ports[1])
pol7.connect(2, wgt6.ports['in26'])
Hairpin6.connect(2, wgt6.ports['out46'] )
wgt7.connect('in27', pol7.ports[1])
pol8.connect(2, wgt7.ports['in57'])
Hairpin7.connect(1, wgt7.ports['out17'] )
wgt8.connect('in58', pol8.ports[1])
pol9.connect(2, wgt8.ports['in28'])
Hairpin8.connect(2, wgt8.ports['out48'] )
wgt9.connect('in29', pol9.ports[1])
pol10.connect(2, wgt9.ports['in59'])
Hairpin9.connect(1, wgt9.ports['out19'] )
wgt10.connect('in510', pol10.ports[1])
pol11.connect(2, wgt10.ports['in210'])
Hairpin10.connect(2, wgt10.ports['out410'] )
wgt11.connect('in211', pol11.ports[1])
pol12.connect(2, wgt11.ports['in511'])
Hairpin11.connect(1, wgt11.ports['out111'] )
wgt12.connect('in512', pol12.ports[1])
pol13.connect(2, wgt12.ports['in212'])
Hairpin12.connect(2, wgt12.ports['out412'] )
wgt13.connect('in213', pol13.ports[1])
pol14.connect(2, wgt13.ports['in513'])
Hairpin13.connect(1, wgt13.ports['out113'] )
wgt14.connect('in514', pol14.ports[1])
pol15.connect(2, wgt14.ports['in214'])
Hairpin14.connect(2, wgt14.ports['out414'] )
wgt15.connect('in215', pol15.ports[1])
pol16.connect(2, wgt15.ports['in515'])
Hairpin15.connect(1, wgt15.ports['out115'] )
wgt16.connect('in516', pol16.ports[1])
pol17.connect(2, wgt16.ports['in216'])
Hairpin16.connect(2, wgt16.ports['out416'] )
wgt17.connect('in217', pol17.ports[1])
pol18.connect(2, wgt17.ports['in517'])
Hairpin17.connect(1, wgt17.ports['out117'] )
wgt18.connect('in518', pol18.ports[1])
pol19.connect(2, wgt18.ports['in218'])
Hairpin18.connect(2, wgt18.ports['out418'] )
wgt19.connect('in219', pol19.ports[1])
pol20.connect(2, wgt19.ports['in519'])
Hairpin19.connect(1, wgt19.ports['out119'] )
wgt20.connect('in520', pol20.ports[1])
pol21.connect(2, wgt20.ports['in220'])
Hairpin20.connect(2, wgt20.ports['out420'] )
wgt21.connect('in221', pol21.ports[1])
pol22.connect(2, wgt21.ports['in521'])
Hairpin21.connect(1, wgt21.ports['out121'] )
wgt22.connect('in522', pol22.ports[1])
pol23.connect(2, wgt22.ports['in222'])
Hairpin22.connect(2, wgt22.ports['out422'] )
wgt23.connect('in223', pol23.ports[1])
pol24.connect(2, wgt23.ports['in523'])
Hairpin23.connect(1, wgt23.ports['out123'] )
wgt24.connect('in524', pol24.ports[1])
pol25.connect(2, wgt24.ports['in224'])
Hairpin24.connect(2, wgt24.ports['out424'] )
wgt25.connect('in225', pol5.ports[1])
pol26.connect(2, wgt25.ports['in525'])
Hairpin25.connect(2, wgt25.ports['out425'] )
wgt26.connect('in526', pol26.ports[1])
pol27.connect(2, wgt26.ports['in226'])
Hairpin26.connect(1, wgt26.ports['out126'] )
wgt27.connect('in227', pol27.ports[1])
pol28.connect(2, wgt27.ports['in527'])
Hairpin27.connect(2, wgt27.ports['out427'] )
wgt28.connect('in528', pol28.ports[1])
pol29.connect(2, wgt28.ports['in228'])
Hairpin28.connect(1, wgt28.ports['out128'] )
wgt29.connect('in229', pol29.ports[1])
pol30.connect(2, wgt29.ports['in529'])
Hairpin29.connect(2, wgt29.ports['out429'] )

wgt30.connect('in530', pol30.ports[1])
pol31.connect(2, wgt30.ports['in230'])
Hairpin30.connect(1, wgt30.ports['out130'] )

wgt31.connect('in231', pol31.ports[1])
pol32.connect(2, wgt31.ports['in531'])
Hairpin31.connect(2, wgt31.ports['out431'] )
##
wgt32.connect('in532', pol32.ports[1])
pol33.connect(2, wgt32.ports['in232'])
Hairpin32.connect(1, wgt32.ports['out132'] )

wgt33.connect('in233', pol33.ports[1])
pol34.connect(2, wgt33.ports['in533'])
Hairpin33.connect(2, wgt33.ports['out433'] )

wgt34.connect('in534', pol34.ports[1])
pol35.connect(2, wgt34.ports['in234'])
Hairpin34.connect(1, wgt34.ports['out134'] )

wgt35.connect('in235', pol35.ports[1])
pol36.connect(2, wgt35.ports['in535'])
Hairpin35.connect(2, wgt35.ports['out435'] )

wgt36.connect('in536', pol36.ports[1])
pol37.connect(2, wgt36.ports['in236'])
Hairpin36.connect(1, wgt36.ports['out136'] )

wgt37.connect('in237', pol37.ports[1])
pol38.connect(2, wgt37.ports['in537'])
Hairpin37.connect(2, wgt37.ports['out437'] )

wgt38.connect('in538', pol38.ports[1])
pol39.connect(2, wgt38.ports['in238'])
Hairpin38.connect(1, wgt38.ports['out138'] )

wgt39.connect('in239', pol39.ports[1])
pol40.connect(2, wgt39.ports['in539'])
Hairpin39.connect(2, wgt39.ports['out439'] )

wgt40.connect('in540', pol40.ports[1])
pol41.connect(2, wgt40.ports['in240'])
Hairpin40.connect(1, wgt40.ports['out140'] )

wgt41.connect('in241', pol41.ports[1])
pol42.connect(2, wgt41.ports['in541'])
Hairpin41.connect(2, wgt41.ports['out441'] )

wgt42.connect('in542', pol42.ports[1])
pol43.connect(2, wgt42.ports['in242'])
Hairpin42.connect(1, wgt42.ports['out142'] )

wgt43.connect('in243', pol43.ports[1])
pol44.connect(2, wgt43.ports['in543'])
Hairpin43.connect(2, wgt43.ports['out443'] )

wgt44.connect('in544', pol44.ports[1])
pol45.connect(2, wgt44.ports['in244'])
Hairpin44.connect(1, wgt44.ports['out144'] )

wgt45.connect('in245', pol45.ports[1])
pol46.connect(2, wgt45.ports['in545'])
Hairpin45.connect(2, wgt45.ports['out445'] )

wgt46.connect('in546', pol46.ports[1])
pol47.connect(2, wgt46.ports['in246'])
Hairpin46.connect(1, wgt46.ports['out146'] )

D.write_gds('myoutput1.gds')
D = pg.import_gds(filename = 'myoutput1.gds', cellname = None, flatten = False)

qp(D)