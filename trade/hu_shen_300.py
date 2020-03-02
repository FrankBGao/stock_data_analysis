data = """
code	name	eng name	exchange	weight
600000	浦发银行	Shanghai Pudong Development Bank Co Ltd	上海证券交易所	1.21
600008	首创股份	Beijing Capital Co Ltd	上海证券交易所	0.11
600009	上海机场	Shanghai International Airport Co Ltd	上海证券交易所	0.42
600010	包钢股份	Inner Mongolia Baotou Steel Union Co Ltd	上海证券交易所	0.26
600011	华能国际	Huaneng Power International Inc	上海证券交易所	0.25
600015	华夏银行	Hua Xia Bank Co Ltd	上海证券交易所	0.5
600016	民生银行	China Minsheng Banking Corp Ltd	上海证券交易所	1.67
600018	上港集团	Shanghai International Port (Group) Co Ltd	上海证券交易所	0.19
600019	宝钢股份	Baoshan Iron &Steel Co Ltd	上海证券交易所	0.66
600021	上海电力	Shanghai Electric Power Co Ltd	上海证券交易所	0.08
600023	浙能电力	Zhejiang Zheneng Electric Power Co., Ltd.	上海证券交易所	0.2
600028	中国石化	China Petroleum & Chemical Corporation	上海证券交易所	0.6
600029	南方航空	China Southern Airlines Co Ltd	上海证券交易所	0.32
600030	中信证券	CITIC Securities Co Ltd	上海证券交易所	1.29
600031	三一重工	Sany Heavy Industry Co Ltd	上海证券交易所	0.32
600036	招商银行	China Merchants Bank Co Ltd	上海证券交易所	2.65
600038	中直股份	AVIC Helicopter Co.,Ltd.	上海证券交易所	0.1
600048	保利地产	Poly Real Estate Group Co Ltd	上海证券交易所	0.85
600050	中国联通	China United Network Communications Co Ltd	上海证券交易所	0.46
600061	国投资本	SDIC Capital Co., Ltd	上海证券交易所	0.1
600066	宇通客车	Zhengzhou Yutong Bus Co Ltd	上海证券交易所	0.26
600068	葛洲坝	China Gezhouba Group Co Ltd	上海证券交易所	0.21
600074	ST保千里	Jiangsu Protruly Vision Technology Group Co., Ltd.	上海证券交易所	0.02
600085	同仁堂	Beijing Tongrentang Co Ltd	上海证券交易所	0.17
600089	特变电工	TBEA Co Ltd	上海证券交易所	0.29
600100	同方股份	Tsinghua Tongfang Co Ltd	上海证券交易所	0.16
600104	上汽集团	SAIC Motor Co Ltd	上海证券交易所	1.05
600109	国金证券	Sinolink Securities Co. Ltd.	上海证券交易所	0.16
600111	北方稀土	China Northern Rare Earth (Group) High-Tech Co.,Ltd	上海证券交易所	0.25
600115	东方航空	China Eastern Airlines Corp Ltd	上海证券交易所	0.25
600118	中国卫星	China Spacesat Co Ltd	上海证券交易所	0.12
600153	建发股份	Xiamen C&D Inc	上海证券交易所	0.14
600157	永泰能源	Wintime Energy Co Ltd	上海证券交易所	0.18
600170	上海建工	Shanghai Construction Co Ltd	上海证券交易所	0.15
600177	雅戈尔	Youngor Group Co Ltd	上海证券交易所	0.19
600188	兖州煤业	Yanzhou Coal Mining Co Ltd	上海证券交易所	0.05
600196	复星医药	Shanghai Fosun Pharmaceutical (Group) Co Ltd	上海证券交易所	0.39
600208	新湖中宝	Xinhu Zhongbao Co Ltd	上海证券交易所	0.18
600219	南山铝业	Shandong Nanshan Aluminium Co., Ltd.	上海证券交易所	0.16
600221	海航控股	Hainan Airlines Holding Co., Ltd.	上海证券交易所	0.33
600233	圆通速递	YTO Express Group Co.,Ltd.	上海证券交易所	0.05
600271	航天信息	Aisino Co.,Ltd	上海证券交易所	0.25
600276	恒瑞医药	Jiangsu Hengrui Medicine Co Ltd	上海证券交易所	1.3
600297	广汇汽车	China Grand Automotive Services Co., Ltd.	上海证券交易所	0.16
600309	万华化学	Wanhua Chemical Group Co., Ltd.	上海证券交易所	0.44
600332	白云山	GUANGZHOU BAIYUNSHAN PHARMACEUTICAL HOLDINGS COMPANY LIMITED	上海证券交易所	0.15
600340	华夏幸福	China Fortune Land Development Co., Ltd.	上海证券交易所	0.34
600352	浙江龙盛	Zhejiang Longsheng Group Co Ltd	上海证券交易所	0.22
600362	江西铜业	Jiangxi Copper Co Ltd	上海证券交易所	0.16
600369	西南证券	Southwest Securities Co Ltd	上海证券交易所	0.11
600372	中航电子	CHINA AVIONICS SYSTEMS CO.,LTD.	上海证券交易所	0.07
600373	中文传媒	Chinese Universe Publishing And Media Co Ltd	上海证券交易所	0.08
600376	首开股份	Beijing Capital Development Co.,Ltd.	上海证券交易所	0.1
600383	金地集团	Gemdale Corporation	上海证券交易所	0.23
600390	五矿资本	Minmetals Capital Company Limited	上海证券交易所	0.03
600406	国电南瑞	NARI Technology Co., Ltd.	上海证券交易所	0.25
600415	小商品城	Zhejiang China Commodities City Group Co Ltd	上海证券交易所	0.13
600436	片仔癀	Zhangzhou Pientzehuang Pharmaceutical Co Ltd	上海证券交易所	0.22
600482	中国动力	China Shipbuilding Industry Group Power Co.,Ltd	上海证券交易所	0.19
600485	信威集团	Beijing Xinwei Telecom Technology Group Co., Ltd.	上海证券交易所	0.23
600489	中金黄金	Zhongjin Gold Co Ltd	上海证券交易所	0.14
600498	烽火通信	Fiberhome Telecommunication Technologies Co Ltd	上海证券交易所	0.14
600518	康美药业	Kangmei Pharmaceutical Co Ltd	上海证券交易所	0.59
600519	贵州茅台	Kweichow Moutai Co Ltd	上海证券交易所	3.03
600522	中天科技	Jiangsu Zhongtian Technologies Co Ltd	上海证券交易所	0.23
600535	天士力	TASLY PHARMACEUTICAL GROUP CO.,LTD	上海证券交易所	0.26
600547	山东黄金	Shandong Gold-Mining Co Ltd	上海证券交易所	0.19
600549	厦门钨业	Xiamen Tungsten Co Ltd	上海证券交易所	0.1
600570	恒生电子	Hundsun Technologies Inc.	上海证券交易所	0.26
600583	海油工程	Offshore Oil Engineering Co Ltd	上海证券交易所	0.12
600585	海螺水泥	Anhui Conch Cement Co Ltd	上海证券交易所	0.57
600588	用友网络	Yonyou Network Technology Co., Ltd.	上海证券交易所	0.25
600606	绿地控股	Greenland Holdings Corporation Limited	上海证券交易所	0.24
600637	东方明珠	Shanghai Oriental Pearl Media Co., Ltd.	上海证券交易所	0.19
600649	城投控股	Shanghai Chengtou Holding Co., Ltd.	上海证券交易所	0.09
600660	福耀玻璃	Fuyao Glass Industry Group Co.,Ltd	上海证券交易所	0.31
600663	陆家嘴	Shanghai Lujiazui Finance and Trade Zone Development Co Ltd	上海证券交易所	0.12
600674	川投能源	Sichuan Chuantou Energy Co Ltd	上海证券交易所	0.18
600682	南京新百	Nanjing Xinjiekou Department Store Co Ltd	上海证券交易所	0.13
600685	中船防务	CSSC OFFSHORE & MARINE ENGINEERING (GROUP) COMPANY LIMITED	上海证券交易所	0.07
600688	上海石化	Sinopec Shanghai Petrochemical Co Ltd	上海证券交易所	0.08
600690	青岛海尔	Qingdao Haier Co Ltd	上海证券交易所	0.47
600703	三安光电	Sanan Optoelectronics Co.,Ltd	上海证券交易所	0.5
600704	物产中大	Zhejiang Material Industrial Zhongda Yuantong Group Co Ltd	上海证券交易所	0.1
600705	中航资本	AVIC CAPITAL CO.,LTD.	上海证券交易所	0.21
600739	辽宁成大	Liaoning Cheng Da Co Ltd	上海证券交易所	0.2
600741	华域汽车	HUAYU Automotive Systems Company Limited	上海证券交易所	0.34
600795	国电电力	GD Power Development Co Ltd	上海证券交易所	0.31
600804	鹏博士	DR. PENG TELECOM&MEDIA GROUP CO., LTD.	上海证券交易所	0.19
600816	安信信托	Anxin Trust Co., Ltd	上海证券交易所	0.19
600820	隧道股份	Shanghai Tunnel Engineering Co Ltd	上海证券交易所	0.12
600827	百联股份	Shanghai Bailian Group Co.,Ltd.	上海证券交易所	0.08
600837	海通证券	Haitong Securities Company Limited	上海证券交易所	0.82
600871	石化油服	Sinopec Oilfield Service Corporation	上海证券交易所	0.03
600886	国投电力	SDIC Power Holdings Co.,Ltd.	上海证券交易所	0.26
600887	伊利股份	Inner Mongolia Yili Industrial Group Co Ltd	上海证券交易所	1.53
600893	航发动力	AVIC AVIATION ENGINE CORPORATION PLC.	上海证券交易所	0.22
600895	张江高科	Shanghai Zhangjiang Hi-tech Park Development Co Ltd	上海证券交易所	0.09
600900	长江电力	China Yangtze Power Co Ltd	上海证券交易所	0.93
600909	华安证券	HUAAN SECURITIES CO., LTD.	上海证券交易所	0.07
600919	江苏银行	Bank of Jiangsu Co., Ltd	上海证券交易所	0.45
600926	杭州银行	BANK OF HANGZHOU CO., LTD	上海证券交易所	0.04
600958	东方证券	ORIENT SECURITIES COMPANY LIMITED	上海证券交易所	0.33
600959	江苏有线	Jiangsu Broadcasting Cable Information Network Corporation Limited	上海证券交易所	0.1
600977	中国电影	CHINA FILM CO., LTD.	上海证券交易所	0.11
600999	招商证券	China Merchants Securities Co Ltd	上海证券交易所	0.35
601006	大秦铁路	Daqin Railway Co Ltd	上海证券交易所	0.43
601009	南京银行	Bank of Nanjing Co Ltd	上海证券交易所	0.37
601012	隆基股份	Longi Green Energy Technology Co., Ltd.	上海证券交易所	0.42
601018	宁波港	Ningbo Port Co Ltd	上海证券交易所	0.19
601021	春秋航空	Spring Airlines Co., Ltd.	上海证券交易所	0.07
601088	中国神华	China Shenhua Energy Co Ltd	上海证券交易所	0.36
601099	太平洋	The Pacific Securities Co.Ltd	上海证券交易所	0.17
601111	中国国航	Air China Ltd	上海证券交易所	0.21
601117	中国化学	China National Chemical Engineering Co Ltd	上海证券交易所	0.13
601118	海南橡胶	China Hainan Rubber Industry Group Co Ltd	上海证券交易所	0.07
601155	新城控股	Future Land Holdings Co., Ltd.	上海证券交易所	0.28
601163	三角轮胎	TRIANGLE TYRE CO., LTD.	上海证券交易所	0.04
601166	兴业银行	Industrial Bank	上海证券交易所	1.83
601169	北京银行	Bank of Beijing Co Ltd	上海证券交易所	0.9
601186	中国铁建	China Railway Construction Co Ltd	上海证券交易所	0.4
601198	东兴证券	DONGXING SECURITIES CO., LTD.	上海证券交易所	0.14
601211	国泰君安	Guotai Junan Securities Co., Ltd.	上海证券交易所	0.57
601212	白银有色	Baiyin Nonferrous Group Co., Ltd.	上海证券交易所	0.04
601216	君正集团	Inner Mongolia Junzheng Energy & Chemical Group Co.,Ltd.	上海证券交易所	0.14
601225	陕西煤业	Shaanxi Coal Industry Company Limited	上海证券交易所	0.27
601228	广州港	GUANGZHOU PORT COMPANY LIMITED	上海证券交易所	0.04
601229	上海银行	Bank of Shanghai Co., Ltd.	上海证券交易所	0.11
601288	农业银行	Agricultural Bank of China Co Ltd	上海证券交易所	1.32
601318	中国平安	Ping An Insurance (Group) Company of China Ltd	上海证券交易所	6.24
601328	交通银行	Bank of Communications Co LTD	上海证券交易所	1.5
601333	广深铁路	Guangshen Railway Company Limited	上海证券交易所	0.14
601336	新华保险	New China Life Insurance Co Ltd	上海证券交易所	0.34
601375	中原证券	CENTRAL CHINA SECURITIES CO., LTD.	上海证券交易所	0.04
601377	兴业证券	Industrial Securities Co Ltd	上海证券交易所	0.27
601390	中国中铁	China Railway Group Limited	上海证券交易所	0.36
601398	工商银行	Industrial and Commercial Bank of China Ltd	上海证券交易所	1.16
601555	东吴证券	Soochow Securities Co Ltd	上海证券交易所	0.18
601600	中国铝业	Aluminum Corporation of China Limited	上海证券交易所	0.27
601601	中国太保	China Pacific Insurance (Group) Co Ltd	上海证券交易所	0.94
601607	上海医药	Shanghai Pharmaceuticals Holding Co.,Ltd	上海证券交易所	0.25
601608	中信重工	CITIC HEAVY INDUSTRIES CO., LTD.	上海证券交易所	0.05
601611	中国核建	China Nuclear Engineering Corporation Limited	上海证券交易所	0.07
601618	中国中冶	Metallurgical Corporation of China Co Ltd	上海证券交易所	0.18
601628	中国人寿	China Life Insurance Company Limited	上海证券交易所	0.37
601633	长城汽车	Great Wall Motor Co Ltd	上海证券交易所	0.12
601668	中国建筑	China State Construction Engineering Co Ltd	上海证券交易所	1.15
601669	中国电建	Power Construction Corporation of China,Ltd	上海证券交易所	0.27
601688	华泰证券	Huatai Securities Co Ltd	上海证券交易所	0.5
601718	际华集团	Jihua Group Co Ltd	上海证券交易所	0.07
601727	上海电气	Shanghai Electric Group Co Ltd	上海证券交易所	0.19
601766	中国中车	CRRC Corporation Limited	上海证券交易所	0.65
601788	光大证券	Everbright Securities Co Ltd	上海证券交易所	0.21
601800	中国交建	China Communications Construction Company Limited	上海证券交易所	0.17
601818	光大银行	China Everbright Bank Co Ltd	上海证券交易所	0.57
601857	中国石油	PetroChina Co Ltd	上海证券交易所	0.44
601866	中远海发	COSCO SHIPPING Development Co.,Ltd.	上海证券交易所	0.09
601872	招商轮船	China Merchants Energy Shipping Co., Ltd.	上海证券交易所	0.07
601877	正泰电器	Zhejiang Chint Electrics Co Ltd	上海证券交易所	0.1
601878	浙商证券	ZHESHANG SECURITIES CO., LTD.	上海证券交易所	0.04
601881	中国银河	China Galaxy Securities Co., Ltd.	上海证券交易所	0.06
601888	中国国旅	China International Travel Service Co Ltd	上海证券交易所	0.46
601898	中煤能源	China Coal Energy Co Ltd	上海证券交易所	0.08
601899	紫金矿业	Zijin Mining Group Co Ltd	上海证券交易所	0.4
601901	方正证券	Founder Securities Co Ltd	上海证券交易所	0.23
601919	中远海控	COSCO SHIPPING Holdings Co., Ltd.	上海证券交易所	0.2
601933	永辉超市	Yonghui Superstores Co Ltd	上海证券交易所	0.33
601939	建设银行	China Construction Bank	上海证券交易所	0.46
601958	金钼股份	Jinduicheng Molybdenum Co Ltd	上海证券交易所	0.06
601966	玲珑轮胎	Shandong Linglong Tyre Co., Ltd.	上海证券交易所	0.07
601985	中国核电	China National Nuclear Power Co.,Ltd.	上海证券交易所	0.28
601988	中国银行	Bank of China Ltd	上海证券交易所	0.73
601989	中国重工	China Shipbuilding Industry Co Ltd	上海证券交易所	0.44
601991	大唐发电	Datang International Power Generation Co.,Ltd.	上海证券交易所	0.08
601992	金隅集团	BBMG Corporation	上海证券交易所	0.15
601997	贵阳银行	Bank of Guiyang Co.,Ltd.	上海证券交易所	0.18
601998	中信银行	China Citic Bank Corporation Limited	上海证券交易所	0.17
603160	汇顶科技	Shenzhen Huiding Technology Co., Ltd.	上海证券交易所	0.04
603799	华友钴业	ZHEJIANG HUAYOU COBALT CO., LTD.	上海证券交易所	0.31
603833	欧派家居	Oppein Home Group Inc.	上海证券交易所	0.05
603858	步长制药	SHANDONG BUCHANG PHARMACEUTICALS CO., LTD.	上海证券交易所	0.03
603993	洛阳钼业	China Molybdenum Co., Ltd.	上海证券交易所	0.2
000001	平安银行	Ping An Bank Co., Ltd.	深圳证券交易所	0.83
000002	万科A	China Vanke Co Ltd	深圳证券交易所	1.43
000008	神州高铁	China High-Speed Railway Technology Co., Ltd.	深圳证券交易所	0.1
000060	中金岭南	Shenzhen Zhongjin Lingnan Nonfemet Co Ltd	深圳证券交易所	0.14
000063	中兴通讯	ZTE Corporation	深圳证券交易所	0.63
000069	华侨城A	Shenzhen Overseas Chinese Town Co Ltd	深圳证券交易所	0.24
000100	TCL集团	TCL Corporation	深圳证券交易所	0.25
000157	中联重科	Zoomlion Heavy Industry Science & Technology Co Ltd	深圳证券交易所	0.16
000166	申万宏源	Shenwan Hongyuan Group CO., LTD	深圳证券交易所	0.2
000333	美的集团	Midea Group CO., LTD	深圳证券交易所	2.18
000338	潍柴动力	Wei Chai Power Co Ltd	深圳证券交易所	0.35
000402	金 融 街	Financial Street Holding Co Ltd	深圳证券交易所	0.1
000413	东旭光电	Dongxu Optoelectronic Technology Co., Ltd.	深圳证券交易所	0.26
000415	渤海金控	Bohai Financial Investment Holding Co.,Ltd.	深圳证券交易所	0.1
000423	东阿阿胶	Shandong Dong-Ee Jiao Co Ltd	深圳证券交易所	0.28
000425	徐工机械	XCMG Construction Machinery Co Ltd	深圳证券交易所	0.15
000503	海虹控股	Searainbow Holding Corp	深圳证券交易所	0.25
000538	云南白药	Yunnan Baiyao Group Co., Ltd.	深圳证券交易所	0.46
000540	中天金融	Zhongtian Financial Group Company Limited	深圳证券交易所	0.18
000559	万向钱潮	Wanxiang Qianchao Co Ltd	深圳证券交易所	0.11
000568	泸州老窖	Luzhou Lao Jiao Co Ltd	深圳证券交易所	0.37
000623	吉林敖东	Jilin Aodong Pharmaceutical Group Co., Ltd.	深圳证券交易所	0.17
000625	长安汽车	Chongqing Changan Automobile Co Ltd	深圳证券交易所	0.19
000627	天茂集团	Hubei Biocause Pharmaceutical Co Ltd	深圳证券交易所	0.1
000630	铜陵有色	Tongling Nonferrous Metals Group Co. Ltd	深圳证券交易所	0.15
000651	格力电器	Gree Electric Appliances,Inc. of Zhuhai	深圳证券交易所	1.99
000671	阳光城	Sunshine City Group Co., Ltd.	深圳证券交易所	0.11
000686	东北证券	Northeast Securities Co Ltd	深圳证券交易所	0.1
000709	河钢股份	HESTEEL COMPANY LIMITED	深圳证券交易所	0.13
000723	美锦能源	Shanxi Meijin Energy Co.,Ltd.	深圳证券交易所	0.06
000725	京东方A	BOE Technology Group Co Ltd	深圳证券交易所	1.11
000728	国元证券	Guoyuan Securities Company Limited	深圳证券交易所	0.16
000738	航发控制	AECC AERO-ENGINE CONTROL CO.,LTD.	深圳证券交易所	0.07
000750	国海证券	Sealand Securities Co., Ltd.	深圳证券交易所	0.11
000768	中航飞机	Avic Aircraft Co.,Ltd.	深圳证券交易所	0.21
000776	广发证券	GF Securities Co., Ltd.	深圳证券交易所	0.43
000783	长江证券	Changjiang Securities Company Limited	深圳证券交易所	0.25
000792	盐湖股份	Qinghai Salt Lake Industry Co Ltd	深圳证券交易所	0.16
000826	启迪桑德	TUS-SOUND ENVIRONMENTAL RESOURCES CO., LTD.	深圳证券交易所	0.13
000839	中信国安	CITIC Guoan Information Industry Co Ltd	深圳证券交易所	0.17
000858	五粮液	Wuliangye Yibin Co Ltd	深圳证券交易所	1.11
000876	新希望	NEW HOPE LIUHE CO., LTD	深圳证券交易所	0.14
000895	双汇发展	Henan Shuanghui Investment & Development Co Ltd	深圳证券交易所	0.22
000898	鞍钢股份	Angang Steel Co Ltd	深圳证券交易所	0.1
000938	紫光股份	Unisplendour Co., Ltd.	深圳证券交易所	0.09
000959	首钢股份	Beijing Shougang Co Ltd	深圳证券交易所	0.07
000961	中南建设	Jiangsu Zhongnan Construction Group Co.,Ltd	深圳证券交易所	0.12
000963	华东医药	Huadong Medicine Co Ltd	深圳证券交易所	0.28
000983	西山煤电	Shanxi Xishan Coal And Electricity Power Co Ltd	深圳证券交易所	0.11
001979	招商蛇口	CHINA MERCHANTS SHEKOU INDUSTRIAL ZONE HOLDINGS CO.,LTD	深圳证券交易所	0.46
002007	华兰生物	Hualan Biological Engineering INC	深圳证券交易所	0.15
002008	大族激光	Han's Laser Technology Industry Group Co., Ltd.	深圳证券交易所	0.41
002024	苏宁易购	SUNING.COM CO.,LTD.	深圳证券交易所	0.46
002027	分众传媒	Focus Media Information Technology Co., Ltd.	深圳证券交易所	0.56
002044	美年健康	Meinian Onehealth Healthcare Holdings Co., Ltd.	深圳证券交易所	0.25
002065	东华软件	DHC Software Co.,Ltd.	深圳证券交易所	0.14
002074	国轩高科	GUOXUAN HIGH-TECH CO.,LTD.	深圳证券交易所	0.13
002081	金螳螂	Suzhou Gold Mantis Construction Decoration Co Ltd	深圳证券交易所	0.18
002142	宁波银行	Bank of Ningbo Co Ltd	深圳证券交易所	0.43
002146	荣盛发展	Risesun Real Estate Development Co Ltd	深圳证券交易所	0.15
002153	石基信息	Beijing Shiji Information Technology Co Ltd	深圳证券交易所	0.08
002174	游族网络	YOUZU Interactive CO., LTD.	深圳证券交易所	0.08
002202	金风科技	Xinjiang Goldwind Science & Technology Co Ltd	深圳证券交易所	0.33
002230	科大讯飞	Iflytek Co.,Ltd.	深圳证券交易所	0.52
002236	大华股份	Zhejiang Dahua Technology Co Ltd	深圳证券交易所	0.39
002241	歌尔股份	GoerTek Inc	深圳证券交易所	0.23
002252	上海莱士	Shanghai RAAS Blood Products Co Ltd	深圳证券交易所	0.26
002292	奥飞娱乐	Alpha Group	深圳证券交易所	0.06
002294	信立泰	Shenzhen Salubris Pharmaceuticals Co Ltd	深圳证券交易所	0.16
002304	洋河股份	Jiangsu Yanghe Brewery Joint-Stock Co Ltd	深圳证券交易所	0.57
002310	东方园林	Beijing Orient Landscape Co Ltd	深圳证券交易所	0.25
002352	顺丰控股	S.F. Holding Co., Ltd.	深圳证券交易所	0.1
002385	大北农	Beijing Dabeinong Technology Group Co Ltd	深圳证券交易所	0.1
002411	必康股份	JiangSu Bicon Pharmaceutical Listed Company	深圳证券交易所	0.07
002415	海康威视	Hangzhou Hikvision Digital Technology Co Ltd	深圳证券交易所	1.34
002424	贵州百灵	Guizhou Bailing Group Pharmaceutical Co Ltd	深圳证券交易所	0.05
002426	胜利精密	Suzhou Victory Precision Manufacture Co Ltd	深圳证券交易所	0.09
002450	康得新	Kangde Xin Composite Material Group Co.,Ltd.	深圳证券交易所	0.37
002456	欧菲科技	O-film Tech Co., Ltd.	深圳证券交易所	0.34
002460	赣锋锂业	Ganfeng Lithium Co Ltd	深圳证券交易所	0.35
002465	海格通信	Guangzhou Haige Communications Group Incorporated Company	深圳证券交易所	0.15
002466	天齐锂业	Tianqi Lithium Industries, Inc.	深圳证券交易所	0.36
002468	申通快递	STO Express Co.,Ltd.	深圳证券交易所	0.07
002470	金正大	Kingenta Ecological Engineering Group Co., Ltd	深圳证券交易所	0.12
002475	立讯精密	Luxshare Precision Industry Co., Ltd.	深圳证券交易所	0.34
002500	山西证券	Shanxi Securities Co Ltd	深圳证券交易所	0.12
002508	老板电器	Hangzhou Robam Appliances Co Ltd	深圳证券交易所	0.15
002555	三七互娱	Wuhu Shunrong Sanqi Interactive Entertainment Network Technology Co.,Ltd.	深圳证券交易所	0.05
002558	巨人网络	Giant Network Group Co., Ltd.	深圳证券交易所	0.17
002572	索菲亚	Suofeiya Home Collection Co Ltd	深圳证券交易所	0.17
002594	比亚迪	BYD Co Ltd	深圳证券交易所	0.45
002601	龙蟒佰利	Lomon Billions Group Co., Ltd.	深圳证券交易所	0.1
002602	世纪华通	ZHEJIANG CENTURY HUATONG GROUP CO., LTD	深圳证券交易所	0.13
002608	江苏国信	Jiangsu Guoxin Corporation Limited	深圳证券交易所	0.05
002624	完美世界	Perfect World Co., Ltd.	深圳证券交易所	0.12
002673	西部证券	WESTERN SECURITIES CO., LTD	深圳证券交易所	0.15
002714	牧原股份	Muyuan Foodstuff Co., Ltd	深圳证券交易所	0.14
002736	国信证券	GUOSEN SECURITIES CO., LTD.	深圳证券交易所	0.24
002739	万达电影	WANDA FILM HOLDING CO., LTD	深圳证券交易所	0.22
002797	第一创业	First Capital Securities Co., Ltd.	深圳证券交易所	0.15
002831	裕同科技	ShenZhen YUTO Packaging Technology Co., Ltd.	深圳证券交易所	0.02
002839	张家港行	Jiangsu Zhangjiagang Rural Commercial Bank Co., Ltd	深圳证券交易所	0.02
002841	视源股份	Guangzhou Shiyuan Electronic Technology Company Limited	深圳证券交易所	0.03
300003	乐普医疗	Lepu Medical Technology (Beijing) Co Ltd	深圳证券交易所	0.32
300015	爱尔眼科	Aier Eye Hospital Group Co Ltd	深圳证券交易所	0.22
300017	网宿科技	Wangsu Science and Technology Co.,Ltd.	深圳证券交易所	0.19
300024	机器人	Siasun Robot & Automation Co Ltd	深圳证券交易所	0.2
300027	华谊兄弟	Huayi Brothers Media Co Ltd	深圳证券交易所	0.14
300033	同花顺	Hithink Royalflush Information Network Co.,Ltd.	深圳证券交易所	0.1
300059	东方财富	East Money Information Co Ltd	深圳证券交易所	0.45
300070	碧水源	Beijing Originwater Technology Co Ltd	深圳证券交易所	0.3
300072	三聚环保	Beijing SJ Environmental Protection and New Material Co Ltd	深圳证券交易所	0.26
300122	智飞生物	Chongqing Zhifei Biological Products Co Ltd	深圳证券交易所	0.14
300124	汇川技术	Shenzhen Inovance Technology Co Ltd	深圳证券交易所	0.31
300136	信维通信	Shenzhen Sunway Communication Co Ltd	深圳证券交易所	0.26
300144	宋城演艺	SONGCHENG PERFORMANCE DEVELOPMENT CO., LTD.	深圳证券交易所	0.13
300251	光线传媒	Beijing Enlight Media Co Ltd	深圳证券交易所	0.1
300315	掌趣科技	OURPALM CO., LTD	深圳证券交易所	0.14
"""

import pandas as pd
from io import StringIO

hushen_300 = pd.read_csv(StringIO(data), sep="\t", header=0, dtype={"code": str})
# print(data.columns)
# print(data["code"])
