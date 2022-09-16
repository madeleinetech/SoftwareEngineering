#Deena Dayal

#CIS 472
#Individual Project 1: Stock Ticker Application

#random for sub menu option 2
import random
#library for up to date stock info
import yfinance as yf
#sense hat emulator
from sense_emu import SenseHat
#call an instance of sense hat
sense = SenseHat()

#all stock symbols for DJIA index
DJIA = ["AXP","AMGN","AAPL","CAT","CSCO","CVX","HON","IBM","INTC","JNJ","JPM","MCD","MMM","MRK","MSFT","NKE","TRV","UNH",
"CRM","WBA","WMT","DIS","DOW"]

#all stock symbols for NASDAQ index
NASDAQ = ["AAL","AAME","AAOI","AAON","AAPL","AAWW","AAXJ","ABCB","ABIO","ABMD","ACAD","ACET","ACFN","ACGL","ACHC","ACIW","ACLS","ACNB",
"ACOR","ACRX","ACST","ACTG","ACWI","ACWX","ADBE","ADES","ADI","ADMA","ADMP","ADP","ADRA","ADRE","ADSK","ADTN","ADUS","ADXS","AEHR","AEIS",
"AERI","AEY","AEZS","AFMD","AGEN","AGIO","AGNC","AGNCP","AGRX","AGTC","AGYS","AGZD","AHPI","AIMC","AIQ","AIRR",
"AIRT","AKAM","AKBA","ALCO","ALDX","ALGN","ALGT","ALIM","ALKS","ALLT","ALNY","ALOT","ALTR","AMAT","AMBA","AMBC","AMCX","AMD",
"AMED","AMGN","AMKR","AMNB","AMOT","AMOV","AMPH","AMRK","AMRN","AMRS","AMSC","AMSF","AMSWA","AMTX","AMWD","AMZN","ANAC","ANDE","ANGI","ANGO","ANIK","ANIP","ANSS",
"ANY","AOSL","APDN","APEI","APOG","AAL","AAME","AAOI","AAON","AAPL","AAWW","AAXJ","ABCB","ABIO","ABMD","ACAD","ACET","ACFN","ACGL","ACHC","ACIW","ACLS","ACNB",
"ACOR","ACRX","ACST","ACTG","ACWI","ACWX","ADBE","ADES","ADI","ADMA","ADMP","ADP","ADRA","ADRE","ADSK","ADTN","ADUS","ADXS",
"AEHR","AEIS","AERI","AEY","AEZS","AFMD","AGEN","AGIO","AGNC","AGNCP","AGRX","AGTC","AGYS","AGZD","AHPI","AIMC","AIQ","AIRR",
"AIRT","AKAM","AKBA","ALCO","ALDX","ALGN","ALGT","ALIM","ALKS","ALLT","ALNY","ALOT","ALTR","AMAT","AMBA","AMBC","AMCX","AMD",
"AMED","AMGN","AMKR","AMNB","AMOT","AMOV","AMPH","AMRK","AMRN","AMRS","AMSC","AMSF","AMSWA","AMTX","AMWD","AMZN","ANAC","ANDE","ANGI","ANGO","ANIK","ANIP","ANSS",
"ANY","AOSL","APDN","APEI","APOG","APTO","APWC", "ARAY","ARCB","ARCC","ARDX","ARIS","ARKR","ARLP","AROW",
"ARRY","ARTNA","ARTW","ARWR", "ASMB","ASML","ASPS","ASRV","ASTC","ASTE","ASTI","ASUR","ASYS","ATAI","ATAX","ATEC","ATHX","ATLC","ATLO",
"ATNI","ATOS","ATRA","ATRC","ATRI","ATRO","ATSG","ATVI","AUBN","AUDC",
"AUPH","AVAV","AVEO","AVGO","AVHI","AVID","AVNW","AWAY","AWRE","AXAS","AXDX","AXGN","AXTI","AZPN","BANF","BANR","BANX","BBBY","BBC","BBGI",
"BBP","BBSI","BCBP","BCLI","BCOR","BCOV","BCPC","BCRX","BEAT","BEBE","BECN","BELFA","BELFB","BFIN","BGCP","BGFV",
"BIB","BICK","BIDU","BIIB","BIOC","BIOL","BIOS","BIS","BJRI","BKCC","BKSC","BLCM","BLDP",
"BLDR","BLFS","BLIN","BLKB","BLMN","BLRX","BLUE","BMRC","BMRN","BNDX",
"BNFT","BNSO","BOKF","BOOM","BOSC","BOTJ","BPOP","BPOPM", "BPTH","BRID","BRKL","BRKR","BSET","BSQR",
"BSRR","BUR","BUSE","BWEN","BWFG","BYFC","CAAS","CAC","CACC","CACG","CAKE","CALA", "CALM","CAMP","CAMT","CAR","CARA","CARV","CARZ","CASH",
"CASI","CASS","CASY","CATY","CBAN","CBAY","CBFV", "CBNK","CBOE","CBRL","CBSH","CCBG","CCLP",
"CCNE","CCOI","CCRN","CCXI","CDC","CDNA","CDNS","CDW","CDXS","CDZI","CECE","CEMI","CENT","CENTA","CENX","CERE","CERS","CEVA","CFA","CFBK","CFFI","CFFN",
"CFO","CFRX","CGEN","CGNX","CGO","CHCI","CHCO","CHDN","CHEF","CHI","CHKP","CHMG","CHNR","CHRS","CHRW","CHSCM","CHSCN","CHSCO","CHSCP","CHTR","CHUY","CHW","CHY","CIDM","CINF","CIZ","CIZN","CJJD",
"CLDX","CLFD","CLIR","CLMT","CLNE","CLRB","CLRO","CLSN","CLVS","CLWT","CMCO","CMCSA","CMCT","CME","CMLS","CMPR","CMRX","CMTL","CNCE","CNET",
"CNMD","CNOB","CNSL","CNTY", "COCO","COHR","COHU","COKE","COLB","COLM","COMM","COMT","CONN","COOL","CORT","COST",
"COWN","COWNL","CPHC","CPIX","CPLP","CPRT","CPRX","CPSI","CPSS", "CRAI","CREG","CRESW","CRESY","CRIS","CRMT","CRNT","CROX",
"CRTO","CRUS","CRVL","CRWS","CSCO","CSF","CSGP","CSGS","CSII","CSIQ","CSPI",
"CSQ","CSTE","CSWC","CTAS","CTBI","CTG","CTHR","CTIB","CTIC","CTRE","CTRN",
"CTSH","CTSO", "CTXS","CUBA","CUTR","CVBF","CVCO","CVCY","CVGI","CVGW","CVLT","CVLY",
"CVV","CWBC","CWCO","CWST","CXDC","CYAN","CYBE","CYBR","CYCC","CYCCP","CYRN","CYTK",
"CYTR","CZNC","CZR","CZWI","DAIO","DAKT", "DAVE","DAX","DBVT","DCOM","DCTH",
"DENN","DERM","DGICA","DGICB","DGII","DGLY","DGRE","DGRS","DGRW","DHIL",
"DIOD","DISH","DJCO","DLHC","DLTR","DMLP","DMRC","DORM","DOX","DRIV","DRRX","DSGX", "DSWL","DVAX","DWAT","DWSN","DXCM","DXGE",
"DXJS","DXLG","DXPE","DXYN","DYNT", "EAC","EBAY","EBIX","EBMT","EBTC","ECPG","EDAP","EDUC","EEFT","EEMA","EFOI",
"EFSC","EGAN","EGBN","EGHT","EGLE","EGRX","EHTH", "ELSE","ELTK","EMCB","EMCF","EMIF","EMITF","EMKR","EML",
"ENG","ENPH","ENSG","ENTA","ENTG","ENTR","ENZN", "EQIX","ERIC","ERIE","ERII","ESCA","ESEA","ESGR","ESLT",
"ESPR","ESSA","EUFN","EVK","EVLV","EVOK", "EVOL","EWBC","EXAS","EXEL","EXLS","EXPD","EXPE","EXPO","EXTR",
"EZPW","FALC","FANG","FARM","FARO","FAST","FATE","FBIZ","FBMS","FBNC","FCAP","FCBC","FCCO",
"FCEL","FCFS","FCNCA","FDUS","FEIM","FELE","FEMB","FEUZ","FFBC","FFHL","FFIC","FFIN","FFIV","FFNW","FFWM","FGEN",
"FISI","FISV","FITB","FITBI","FIVE","FIVN","FIZZ","FLEX","FLIC","FLL", "FLWS","FLXS","FMB","FMBH","FMNB","FNHC","FNLC",
"FOLD","FONR","FORD","FORM","FORR","FORTY","FOSL","FOX","FOXA","FOXF","FPXI","FRBA","FRBK",
"FREE","FRGI","FRME","FRPH","FRPT","FRSH","FSBW","FSFG","FSLR","FSTR","FTCS","FTEK","FTGC","FTHI","FTNT","FTSL","FTSM",
"FULT","FUNC","FUND","FWP","FWRD","GABC","GAIA","GAIN","GALT","GAME","GASS","GBCI","GBDC","GBLI","GCBC","GENC","GENE",
"GEOS","GERN","GEVO", "GGAL","GIFI","GIGA","GIGM","GIII","GILD","GILT",
"GLAD","GLBS","GLBZ","GLDD","GLDI","GLMD","GLNG","GLPI","GLRE","GLRI","GLYC","GNCA","GNMA","GNTX","GOGO","GOLD","GOOD","GOODN",
"GOODO","GOOG","GOOGL","GPOR","GPRE","GPRO","GRBK","GRFS","GRID","GRMN","GROW","GRPN","GRVY","GSBC","GSIT","GSM","GTIM","GTLS","GULTU","GURE","GYRO",
"HAFC","HAIN","HALL","HALO","HART","HAS","HAYN","HBAN","HBANP","HBCP","HBIO","HBNC","HCCI","HCKT","HCOM","HCSG",
"HDSN","HEAR","HEES","HELE","HERO","HFBL","HFWA","HIBB","HIFS",
"HIHO","HIMX","HLIT","HMNF","HMNY","HMST","HMTV","HNNA", "HNRG","HOFT","HOLI","HOLX","HOMB","HOVNP","HQY","HRTX","HRZN","HSIC","HSII",
"HSKA","HSON","HSTM","HTBI","HTBK","HTHT","HTLD","HTLF","HUBG","HURC","HURN", "HWBK","HWKN","HYLS","HYZD","HZNP","IART","IBB","IBCP","IBKR","IBOC",
"IBTX","ICAD","ICCC","ICFI","ICLN","ICLR","ICPT","ICUI","IDCC","IDRA","IDXX","IEP","IESC","IEUS","IFGL","IFV","IGLD","IGOV",
"III","IIIN","ILMN","IMGN","IMKTA","IMMR","IMOS","INBK","INCR","INCY","INDB","INDY","INFA","INFI","INFN","INGN",
"INO","INOD","INSM","INTC","INTG","INTU","INVE","IOSP","IPAR","IPDN","IPGP","IPKW","IPWR",
"IRBT","IRDM","IRIX","IRMD","IROQ","IRWD","ISHG","ISIG","ISRG","ISSC","ISTR","ITCI","ITIC","ITRI","ITRN","JACK",
"JAKK","JAZZ","JBHT","JBLU","JBSS","JCTCF","JJSF","JKHY","JOUT","JRVR","JSM","JVA","JYNT","KALU",
"KBAL","KELYA","KELYB","KEQU","KFFB","KFRC","KINS","KIRK", "KLAC","KLIC","KMDA","KNDI","KOPN","KOSS","KPTI",
"KRNY","KTCC","KTEC","KTOS","KVHI","KWEB","LAKE","LAMR","LANC","LAND","LARK","LBAI",
"LBRDA","LBRDK","LBTYA","LBTYB","LBTYK","LCNB","LCUT","LECO","LEDS",
"LFUS","LFVN","LGIH","LGND","LHCG","LINC","LION","LIVE","LKFN","LKQ","LMAT","LMBS","LMNR",
"LNDC","LOAN","LOCO","LOGI","LOPE","LPCN","LPLA","LPSN","LPTH","LQDT","LRCX","LSBK","LSCC","LSTR","LTBR","LTRPA","LTRPB","LTRX","LULU",
"LUNA","LWAY","LXRX","LYTS","MACK","MAG","MANH","MANT","MAR","MARA","MARK","MARPS","MASI",
"MAT","MATW","MAYS","MBCN","MBSD","MBUU","MBWM","MCBC","MCBK","MCHP","MCHX","MCRI","MDIV","MDLZ","MDRX",
"MDWD","MDXG","MEIP","MELI","MEOH","MERC","MFLX","MGEE","MGI","MGIC","MGNX","MGPI","MGRC","MGYR",
"MHLD","MICT","MIDD","MIND","MITK","MKSI","MKTX","MLAB","MLNK","MLVF","MMLP","MMSI","MMYT","MNDO","MNKD","MNOV","MNRO","MNST","MNTX",
"MOFG","MOMO","MORN","MPAA","MPB","MPWR","MRCC","MRCY","MRNS","MRTN","MRTX","MRVL","MSEX","MSFT","MSTR","MTBC",
"MTEX","MTLS","MTRX","MTSI","MVIS","MYGN","MYRG","NAII","NATH","NATI","NATR","NAVI","NBIX","NBN","NBTB",
"NCLH","NCMI","NCTY","NDAQ","NDLS","NDSN","NECB","NEO","NEOG","NEON","NEPT","NERV",
"NEWP","NEWT","NFBK","NFLX","NICE","NICK","NILE","NKSH","NKTR","NLST","NMIH","NNBR","NRIM","NSIT","NSSC","NSTG","NSYS","NTAP","NTCT","NTES",
"NTGR","NTIC","NTRS","NTWK","NURO","NUVA","NVAX","NVCN","NVDA","NVEC","NVEE","NVFY","NVMI","NWBI","NWBO","NWFL","NWLI","NWPX","NWS","NWSA","NXPI","NXST",
"NYMT","NYMX","OCC","OCFC","OCUL","ODFL","ODP","OFED","OFIX","OFLX","OFS","OIIM","OLED","OMAB","OMCL","OMER","OMEX","ONB",
"ONCY","ONEQ","ONTX","OPHC","OPOF","OPTT","ORLY","ORMP","ORRF","OSBC","OSIS","OSTK","OSUR","OTEX","OTIC",
"OTTR","OVBC","OVLY","OXBR","OXBRW","OXLC","OXLCN","OXLCO","OXLCP","PAAS","PACB","PACW","PAHC","PANL","PATK","PAYX","PBHC","PBPB",
"PCAR","PCH","PCRX","PCTI","PCTY","PCYG","PCYO","PDBC","PDCE","PDCO","PDEX","PDFS","PEBK","PEBO","PEGA","PENN","PERI","PESI",
"PETS","PFBC","PFBX","PFIE","PFIN","PFIS","PFLT","PFMT","PFSW","PGC","PGTI",
"PINC","PKBK","PKOH","PLAB","PLAY","PLBC","PLCE","PLPC","PLUG","PLUS","PLXS","PMD","PME","PNBK","PNFP","PNNT","PNQI","PNRG","PODD",
"POOL","POWI","POWL","PPBI","PPC","PPSI","PRAA","PRFT","PRFZ","PRGS","PRIM","PRKR","PRMW","PROV","PRPH","PRQR","PRTA","PRTK","PRTS",
"PSCC","PSCD","PSCE","PSCF","PSCH","PSCI","PSCM","PSCT","PSEC","PSMT","PTC","PTCT","PTEN","PTNR","PTSI","PWOD","PZZA",
"QABA","QAT","QBAK","QCCO","QCLN","QCOM","QCRH","QDEL","QGEN","QLYS","QNST","QQEW","QQQ","QQQX","QQXT","QRHC","QRVO",
"QTEC","QTNT","QUIK","QUMU","QURE","QYLD","RADA","RAIL","RAND","RARE","RAVE",
"RBCAA","RBCN","RCII","RCKY","RCMT","RCON","RDCM","RDHL","RDI","RDIB","RDNT",
"RDVY","RDWR","REFR","REGN","RELL","RENT","RFIL","RGCO","RGEN","RGLD","RGLS","RIBT","RICK","RIGL",
"RMBS","RMCF","RMTI","RNA","RNST","RNWK","ROBO","ROCK","ROIC","ROLL","ROSE","ROST","ROYL","RPRX","RRGB",
"RUSHA","RUSHB","RUTH","RVNC","RVSB","RWLK","RXDX","RYAAY","SABR","SAFT","SAGE","SAIA","SAL","SALM","SAMG","SANM","SANW","SASR","SATS","SAVE","SBAC",
"SBCF","SBFG","SBGI","SBLK","SBNY","SBRA","SBSI","SBUX","SCHL","SCHN",
"SCOR","SCSC","SCVL","SCYX","SEAC","SEED","SEIC","SEMI","SENEA","SENEB","SEV","SFBC","SFBS","SFM","SFNC","SFST","SGC","SGEN","SGMA","SGMO",
"SGRP","SHBI","SHEN","SHIP","SHOO","SIEB","SIEN","SIFY","SIGA","SIGI","SILC","SIMO","SIRI","SIVB",
"SKOR","SKYW","SKYY","SLAB","SLGN","SLM","SLMBP","SLP","SLRC","SLVO","SMBC","SMCI","SMIT","SMLR","SMMF","SMPL","SMRT","SMSI","SMTC",
"SNCR","SNFCA","SNPS","SOCL","SOFO","SOHO","SOHU","SOXX","SPCB","SPLK","SPNS","SPOK","SPPI","SPRO","SPSC","SPTN","SPWH","SPWR",
"SQQQ","SRCE","SRCL","SRDX","SRNE","SRPT","SSB","SSBI","SSNC","SSYS","STAA","STBA","STEM","STKL","STLD","STRA","STRL","STRM",
"STRN","STRS","STRT","STX","STXS","SUPN","SURG","SVA","SVVC","SWIR","SWKS","SYBT","SYNA","SYPR",
"TACT","TAIT","TAST","TATT","TAYD","TBBK","TBK","TBNK","TBPH","TCBI",
"TCBK","TCCO","TCFC","TCPC","TCX","TDIV","TECH","TEDU","TENX","TESS","TFSL","TGA","TGEN","TGLS","TGTX","THFF","THRM","THRX",
"TIGR","TILE","TINY","TIPT","TITN","TLF","TNDM","TNXP","TOPS","TORM","TOUR","TOWN","TQQQ","TREE","TRIB","TRIP","TRMB","TRMK","TRNS","TRNX",
"TROW","TRS","TRST","TRTL","TRUE","TRVN","TSBK","TSCO","TSEM","TSLA","TSRI","TTEC","TTEK","TTGT","TTMI","TTOO","TTWO",
"TWIN","TWOU","TXN","TXRH","TZOO","UAE","UBCP","UBFO","UBOH","UBSI","UCBI","UCTT","UEIC","UFCS","UFPI","UFPT","UHAL","UIHC","ULBI","ULTA",
"ULTR","UMBF","UMPQ","UNAM","UNB","UNFI","UNTY","UPLD","URBN","USAK","USAP","USEG","USLM","UTHR","UTMD","UTSI","UVSP","VALU",
"VBFC","VBIV","VBLT","VBND","VBTX","VCEL","VCIT","VCLT","VCSH","VCYT","VECO",
"VGIT","VGLT","VGSH","VIA","VICR","VIDI","VIEW","VIRC","VIVO","VLGEA","VMBS","VNDA","VNET","VNOM","VNQI","VOD","VONE","VONG",
"VONV","VOXX","VRA","VRNS","VRNT","VRSK","VRSN","VRTS","VRTX","VSAT","VSEC","VSTM","VTHR","VTIP","VTNR","VTWG","VTWO","VTWV","VUSE","VWOB",
"VXUS","WABC","WAFD","WASH","WATT","WAYN","WBA","WDC","WDFC","WEN","WERN","WETF","WEYS","WABC","WAFD","WASH","WATT","WAYN","WBA","WDC","WDFC","WEN",
"WHF","WHLM","WHLR","WHLRP","WABC","WAFD","WASH","WATT","WAYN","WBA","WDC","WDFC","WEN","WILC","WINA","WIRE","WIX","WLDN","WLFC","WOOD","WOOF",
"WPRT","WRLD","WSBC","WSBF","WSFS","WSTG","WSTL","WTBA","WTFC","WVFC", "WVVI","WWD","WYNN",
"XENE","XNCR","XNET","XOMA","XRAY","XTLB","YORW","ZBRA","ZEUS","ZION","ZUMZ"]

#all stock symbols for NYSE index
NYSE = ["AAC",   "AAN",   "AAP",   "AAT",  "ABB",   "ABBV",   "ABC",   "ABEV",   "ABG",
"ABM",   "ABR",   "ABT",  "ACCO",  "ACI", "ACM",  "ACN",   "ACP",   "ACRE",   "ACT",
"ADC",   "ADM",   "ADPT",  "ADT",   "ADX",  "AEE",   "AEG",  "AEL","AEM",   "AEO",   "AEP",   "AER",   "AES",
"AFB",   "AFG",   "AFGE",   "AFL",  "AFT",   "AGCO",
"AGD", "AGI",   "AGM",  "AGO", "AGRO",   "AGX","AHH",  "AHT",  "AIB",   "AIF",   "AIG",  "AIN",   "AIR",   "AIT",   "AIV","AIZ",
"AJG",  "AKR", "ALB","ALE",   "ALEX",   "ALG",  "ALK",   "ALL",   "ALLE", "ALLY",  "ALR",  "ALSN",
"ALV",   "ALX","AMC",   "AME",   "AMG",   "AMH",  "AMID",   "AMP",   "AMRC",  "AMT","AMTD", "AMX", "ANET",   "ANF",
 "AOD", "AON",   "AOS",   "APA",   "APAM",    "APD","APH",  "APO",    "ARC",   "ARCO",   "ARDC",   "ARE",  "ARES",
"ARI",  "ARL", "ARMK", "ARR","ARW",  "ASA",   "ASB",  "ASC",   "ASG",   "ASGN",   "ASH",   "ASPN",   "ASR",   "ASX",
"ATEN",   "ATHM",   "ATI",   "ATO",   "ATR",   "ATTO",   "AUY","AVA",   "AVAL",   "AVB",   "AVD","AVIV",   "AVK",  "AVT",  "AVY",
"AWF",   "AWH",   "AWI",   "AWK",   "AWP",   "AWR",  "AXL",   "AXP",   "AXR",   "AXS",  "AXTA","AYI",
"AZN",   "AZO",   "AZZ", "BABA",   "BAC", "BAH",   "BAK",   "BALT",   "BAM",   "BANC",  "BAP",
"BAX",   "BBD",   "BBDO",  "BBN","BBVA",   "BBW",   "BBY", "BCC",   "BCE",   "BCH",   "BCO",   "BCS",
"BCX",   "BDC",   "BDJ",   "BDN",   "BDX",   "BEN",   "BEP", "BERY", "BFAM",   "BFK",
"BFS",   "BFZ", "BGB", "BGH",   "BGR",   "BGS",   "BGT",   "BGX",   "BGY",  "BHE",   "BHK",     "BHLB",   "BHP",
"BIG",    "BIO", "BIP",   "BIT","BKD",   "BKE",   "BKH",   "BKN",
"BKT",   "BKU",    "BLK",   "BLW","BLX",   "BMA",   "BME",   "BMI",  "BMO",
"BMY", "BNS",   "BNY",  "BOE",   "BOH", "BOOT",   "BPT","BR",   "BRC",   "BRFS",   "BRO",   "BRP",    "BRT",   "BRX",   "BSAC","BSBR",
"BSL",   "BSMX",   "BST",   "BSX",   "BTA",   "BTF",  "BTO",   "BTT",
"BTU",   "BTZ",   "BUD",   "BUI",   "BURL",   "BVN",   "BWA",   "BWC",   "BWG",
"BXC",  "BXMT","BXMX",   "BXP",  "BYD",   "BYM",   "BZH",
"CACI",   "CAE",   "CAF",   "CAG",   "CAH",   "CAJ",   "CALX",   "CAPL",  "CAT",
"CATO",   "CBD",  "CBL", "CBT",   "CBU",   "CBZ",  "CCI",  "CCJ",   "CCK",
"CCL",   "CCM",   "CCO",   "CCS",   "CCU",   "CCV",    "CDE",
"CEA",    "CEE",    "CEM",   "CEN",  "CEQP",   "CFG","CFR",    "CGA",   "CHD",   "CHE",   "CHGG",   "CHH",   "CHK","CHKR",
"CHMI",   "CHN",   "CHS",    "CHT",    "CIA",   "CIB",
"CIEN",   "CIF",   "CIG",  "CII",   "CIM",   "CIO",   "CIR",   "CIVI","CLB",     "CLDT",   "CLF",   "CLH",   "CLR",   "CLS",
"CLW",   "CLX",  "CMA",    "CMC",   "CMCM",   "CMG",   "CMI", "CMP",   "CMRE",    "CMS",   "CMU",   "CNA",   "CNC",
"CNHI",   "CNI","CNK",     "CNO",   "CNP",   "CNQ",   "CNS",   "CNX",    "CODI",   "COF",
"COO",   "COP",  "CORR",  "COTY", "COUP", "CPA",   "CPAC",   "CPB",   "CPE",   "CPF",   "CPG",   "CPK",   "CPS", "CPT",  "CRC",
"CRH",   "CRI",   "CRK",   "CRL",   "CRM",  "CRS",   "CRT","CSL",   "CSTM",   "CSV",   "CSX",
"CTLT",   "CTR",   "CTS",   "CTT",   "CTV",  "CUBE","CUBI",   "CUBS",   "CUK",   "CUZ",   "CVE",   "CVEO",   "CVI",
"CVS",   "CVT",   "CVX", "CWT",  "CXE",   "CXH",  "CXW",   "CYD","CYH",   "CYN",  "CYT",
"DAC",   "DAL",   "DAN","DAR",  "DBD",   "DBL",  "DCI",   "DCO",   "DCT",
"DDD",   "DDF",    "DDS",   "DDT",  "DECK", "DEI", "DEO",   "DEX",   "DFP",   "DFS",
"DGX",   "DHF",    "DHI",   "DHR",   "DHT",   "DHX",   "DIAX",   "DIN",   "DIS",   "DKL",   "DKS",
"DLB",   "DLNG",  "DLR",  "DLX",    "DMB",    "DMO",
"DNB",   "DNOW",   "DNP",  "DOC",   "DOOR",   "DOV",   "DOW",   "DPG",
"DPZ",   "DRD",   "DRE",   "DRH",   "DRI",    "DRQ",    "DSL",   "DSM",
"DSU",    "DSX",    "DTE",   "DTF",   "DUK", "DVA",   "DVN",   "DYN","EARN",   "EAT",   "EBF",   "EBR",   "EBS", "ECC","ECL",   "ECOM",
"EDD", "EDF",   "EDI",   "EDN",   "EDR",   "EDU",  "EEA",
"EFC","EFR",   "EFT",   "EFX",   "EGF",     "EGO",   "EGP",   "EGY",   "EHI","EIG",   "EIX",   "ELA",  "ELP",   "ELS",
"EMD",   "EME",     "EMF",   "EMN",   "EMO",     "EMR",  "ENB",
"ENJ",   "ENLC",    "ENR",   "ENS",   "ENV",   "ENVA",   "ENZ",  "EOD",   "EOG",   "EOI",   "EOS", "EOT",   "EPAM",   "EPD",   "EPR",   "EQC",
"EQR",   "EQS",   "EQT",     "ERF",   "ERJ",  "ESE",   "ESI",    "ESNT",   "ESRT",   "ESS",
"ETB",  "ETG",   "ETJ",    "ETN",   "ETO",  "ETR",   "ETV",   "ETW",   "ETX",
"ETY", "EVC",   "EVER",   "EVF",   "EVG",   "EVGN",   "EVN",   "EVR",   "EVT",   "EVTC","EXC",    "EXD",   "EXG",   "EXK",  "EXP",   "EXPR",   "EXR",
"FAF",   "FAM",  "FBC",   "FBHS",   "FBP","FCF",    "FCN",   "FCT",   "FCX",   "FDP",   "FDS",   "FDX", "FEI",
"FENG",   "FEO",   "FET",   "FFA",   "FFC",   "FGB",    "FHN","FICO",   "FIF",   "FIG",  "FIS",   "FIX",    "FLC",   "FLO",   "FLR",   "FLS",   "FLT",   "FMC",
"FMN",  "FMS",    "FMX",   "FMY",  "FNB",   "FNF","FNV",  "FOF",   "FOR",   "FPF",   "FPL",   "FRA",   "FRC",
"FRO",   "FRT",  "FSD",    "FSM",   "FSS",   "FTI","FTK",   "FUL",   "FUN",  "GAB",    "GAM",
"GBAB",   "GBL",   "GBX",   "GCI",   "GCO",   "GCV",  "GDL","GDO",   "GDOT",   "GDV",   "GEF",
"GEL",   "GEO",   "GER",   "GES",    "GFF",   "GFI",  "GGB",   "GGE",
"GGG",   "GGT",    "GGZ",   "GHC", "GHL",   "GHM",   "GHY",   "GIB",   "GIL",   "GIM","GIS",  "GJO",   "GJP",   "GJR",   "GJS",   "GLOB",     "GLOP",   "GLP",
"GLT",   "GLW",    "GME",   "GMED",  "GNE","GNRC",   "GNT",   "GNW",   "GOF",   "GOL",   "GPC", "GPI",   "GPK",   "GPN",   "GPRK",   "GPS",
"GRX",   "GSK","GSL", "GTN",    "GTY",    "GUT",   "GVA","GWRE",   "GWW",    "HAE",   "HAL",
"HASI",  "HBI",   "HBM",  "HCA",   "HCC",   "HCI",   "HCP",  "HDB","HEI",   "HEP",   "HEQ",   "HES",
"HHC",   "HHS",    "HIE",   "HIG",     "HII",   "HIL",   "HIO",   "HIVE",   "HIW",   "HIX",
"HLF", "HLT",   "HLX",   "HMC",    "HMLP",   "HMN",   "HMY",   "HNI","HOG",   "HON",    "HOV",   "HPF",   "HPI",   "HPP",   "HPQ",   "HPS",
"HQH",   "HQL",   "HRB",  "HRL",  "HRTG",   "HSBC",  "HSC",  "HST",   "HSY",
"HTD", "HTGC",   "HTH",    "HTY",   "HTZ",   "HUBS",   "HUM","HUN",  "HVT",    "HXL",     "HYB",
"HYI",   "HYT",   "HZO",   "IAE",   "IAG",   "IBA",   "IBM",   "IBN","IBP", "ICD",   "ICE",   "ICL",   "IDA",   "IDE",    "IDT",  "IEX",   "IFF",   "IFN",
"IGA",   "IGD",   "IGI",   "IGR",   "IGT",    "IHD",   "IHG",   "IHS",   "IIF",   "IIM",   "IMAX","INFY",   "ING",   "INGR",   "INN",   "INT",  "IPG",
"IPI",    "IQI",   "IRL",   "IRM",    "IRS",   "ISD","ITT",   "ITUB",   "ITW",   "IVC",   "IVH",   "IVR",    "IVZ","JBK",   "JBL",
"JBT",   "JCE",   "JCI", "JEQ",  "JFR",   "JGH",   "JHI",   "JHS","JHX",   "JKS",   "JLL",   "JLS","JMM",   "JNJ",   "JNPR",
"JOE",   "JOF", "JPC",  "JPI",   "JPM",   "JPS",   "JQC",   "JRI",   "JRO","JSD",   "JWN",  "KAI",   "KAMN",     "KAR",    "KBH",   "KBR",
"KIO",   "KKR",   "KMB",   "KMF",
"KMI",  "KMPR",   "KMT",   "KMX", "KNOP",   "KNX",     "KODK",    "KOF",   "KOP",    "KOS",    "KRC",   "KRG",   "KRO",     "KSM",
"KSS",  "KTF",   "KTH",   "KTN",    "KWR",     "KYN",     "LAD",   "LADR","LAZ",  "LCI",  "LDOS",   "LDP",  "LEA",  "LEE",   "LEG",   "LEJU",   "LEN",
"LEO",   "LEU",  "LGI",   "LII",   "LITB",   "LLL",   "LLY",    "LMT",   "LNC",   "LND","LNN",   "LNT",    "LOW",   "LPG",   "LPI",   "LPL",   "LPX",     "LRN",   "LTC",
"LUV",   "LVS",   "LXFR",   "LXP",    "LXU",   "LYB",   "LYG",   "LYV",   "LZB",   "MAA","MAC",   "MAIN",   "MAN",   "MANU",   "MAS",   "MATX",   "MAV",   "MBI",
"MCD",   "MCI",   "MCK","MCN",   "MCO",  "MCR",   "MCS",    "MCY",   "MDC",  "MDT",   "MDU",   "MED","MEG",   "MEI",
"MET",   "MFA",   "MFC",   "MFD",   "MFG",   "MFM",     "MFV",    "MGA","MGF",   "MGM",   "MGR",   "MGU",    "MHD",   "MHF",
"MHI",   "MHK",   "MHN",  "MHNC","MHO",  "MIG",    "MIN",   "MITT",   "MIXT",   "MIY",
"MKC",   "MKL",   "MLI",   "MLM",   "MLP",   "MLR",    "MMC",   "MMD",   "MMI",   "MMM",   "MMP",   "MMS",   "MMT",   "MMU",
"MNP",  "MOD",   "MODN",     "MOH",   "MON",   "MOS",   "MOV",   "MPA",   "MPC",
"MPLX",   "MPV",   "MPW",   "MPX",   "MQT",   "MQY",   "MRC",    "MRIN",   "MRK",   "MRO",    "MSA",   "MSB",
"MSCI",   "MSD",   "MSI",   "MSM",    "MTB",      "MTCN",   "MTD","MTDR",   "MTG",   "MTH",   "MTL",   "MTN",   "MTR",   "MTRN",
"MTW",   "MTX",   "MTZ",   "MUA","MUC",   "MUE", "MUI",   "MUJ",   "MUR",    "MUSA",   "MUX",
"MVO",   "MVT",   "MWA", "MXE",   "MXF",   "MXL",   "MYD",   "MYE",   "MYI","MYN", "NAC",   "NAD", "NAN",   "NAT",   "NAZ",   "NBB",
"NBHC", "NBR",  "NCA",  "NCR",  "NCV",   "NCZ",   "NDP","NEA",   "NEE",   "NEM",   "NEP",  "NEU",  "NEWR",   "NFG",   "NFJ",   "NGG",   "NGL",
"NGS",   "NGVC",  "NHI",    "NID",   "NIE",   "NIM",   "NIO",   "NIQ",  "NJR",   "NKE",   "NKG",   "NKX","NLS",   "NLSN",   "NLY",
"NMFC",   "NMI",   "NMM",   "NMR",   "NMS",   "NMT",   "NNI",   "NNN",  "NNY",   "NOA",   "NOAH",   "NOC",   "NOK",  "NOV",   "NOW",
"NPK", "NPO", "NPV",   "NQP",  "NRG",   "NRK",   "NRP",   "NRT",   "NRZ",  "NSC",   "NSL",   "NSP",   "NSS",
"NTG", "NTP",  "NTZ",    "NUE",   "NUO",   "NUS",   "NUV",   "NUW",   "NVGS","NVO",   "NVR",   "NVRO",   "NVS",   "NWE",
"NWL",   "NWN",  "NXC",   "NXJ",   "NXN",   "NXP","NYCB",  "NYT","OCN",  "ODC",   "OEC",   "OFC",
"OFG",   "OGE",   "OGS",   "OHI",  "OIA",    "OII",     "OIS",   "OKE",    "OLN",   "OLP",   "OMC",
"OMI",  "OPK",    "OPY",   "ORA",   "ORAN",    "ORC",   "ORCL",   "ORI",
"ORN",   "OSK",  "OUT",    "OXM",   "OXY",   "PAA",   "PAC",    "PAG",   "PAGP",    "PAI",
"PAM",   "PANW",   "PAR",   "PAY",   "PAYC",   "PBA",   "PBF",   "PBFX",   "PBH",   "PBI",  "PBR",     "PBT","PBYI",   "PCF","PCG",
"PCK",    "PCM",   "PCN", "PCQ",   "PDI",   "PDM",   "PDS",   "PDT",   "PEB", "PEG",   "PEI","PEO",   "PEP",
"PFD",   "PFE",   "PFG",    "PFH",  "PFL",   "PFN",   "PFO",   "PFS",   "PFSI",   "PFX",
"PGP",   "PGR",   "PGRE",   "PGZ",  "PHD",   "PHG",  "PHI",   "PHK",   "PHM",   "PHT","PHX",   "PII",   "PIM",
"PKE",   "PKG",   "PKI", "PKX", "PLD",   "PLL",   "PLOW",    "PMF",   "PML",   "PMM",   "PMO",   "PMT",   "PMX",   "PNC",    "PNF",   "PNI",
"PNM",   "PNR",    "PNW",    "POL",    "POR",   "POST",    "PPG",   "PPL","PPT",   "PRA",   "PRE",  "PRGO",   "PRH",   "PRI",   "PRLB",   "PRO",   "PRU",
"PSA",   "PSF",  "PSO",   "PSX",    "PTR",   "PTY",   "PUK",   "PVH","PWR",   "PXD",   "PYN",   "PYS",   "PYT",     "PZC",   "PZN",   "QSR",
"QTWO",   "QUAD",  "RAD",   "RBA",  "RCI","RCL",   "RCS",   "RDN",  "RDY",    "REG",   "RENN",   "RES",   "RESI",   "REV",   "REX",   "REXR",   "RFI",   "RFP",
"RGA",   "RGC",   "RGP",   "RGR",   "RGS",   "RGT",   "RHI",   "RHP",    "RIG",  "RIO",
"RJF",   "RKT",     "RLI",   "RLJ",   "RMAX",   "RMD","RMT",   "RNG",    "RNP",   "RNR",   "ROC",   "ROG",   "ROK",   "ROL",   "ROP",
"RPM",   "RPT",    "RQI",   "RRC",   "RRTS",   "RSG","RVT",   "RWT",     "RYAM",   "RYI",    "RYN",   "RZA",    "SAH",   "SAIC",   "SAM","SAN",   "SAP",
"SAR",    "SBH",     "SBR",   "SBS",    "SCCO",   "SCD","SCHW",   "SCI",   "SCL",   "SCM",   "SCS",   "SCU",   "SCX",   "SEAS",   "SEE","SEM",
"SFE",    "SFL",    "SFY","SGU",    "SHG",   "SHI",   "SHLX",   "SHO",   "SHW",   "SID",   "SIG",   "SIR",   "SIX",   "SJI",   "SJM",   "SJR","SJT",   "SJW",
"SKM",   "SKT",   "SKX",   "SLB",   "SLCA",   "SLF",   "SLG","SMFG",   "SMG",   "SMI",   "SMLP",   "SMM",   "SMP",   "SNA",   "SNN",   "SNOW",   "SNP",
"SNV",   "SNX",   "SNY",   "SOL",   "SON",   "SOR","SPB",   "SPE",  "SPG",   "SPH",   "SPLP",   "SPR","SPXX",   "SQM",   "SQNS",   "SRC",   "SRE",   "SRI",   "SRLP",   "SRT",   "SRV",   "SSD",
"SSL","SSP",    "SSTK",    "STAG",   "STAR",    "STC",   "STE","STK", "STM",   "STN",   "STNG",   "STON",   "STOR",   "STR",   "STRI",   "STT",   "STWD",   "STZ","SUI",   "SUN",
"SUP",   "SVM",    "SWI",   "SWK",   "SWN","SWX",  "SWZ",   "SXC",    "SXI",  "SXT",    "SYF",   "SYK",
"SYY",   "SZC",  "TAC","TAL",  "TAP",    "TARO",   "TBI",
"TCI",  "TCRX",   "TCS", "TDC",  "TDF",   "TDG","TDS",   "TDW",   "TDY",   "TEF",  "TEI",   "TEL",   "TEN",   "TEO",   "TER",  "TEVA",   "TEX",
"TFG",   "TFX",   "TGH",   "TGI","TGS",   "TGT",   "THC",   "THG",  "THO",   "THQ",   "THR",   "THS","TIME",   "TISI",   "TJX",  "TKC",   "TKR",   "TLK",  "TLYS",    "TMHC",
"TMO",   "TMST",   "TMUS",   "TNC",   "TNET",   "TNK",   "TNP",  "TOL",   "TPC",   "TPH",   "TPL","TPVG",   "TPX",   "TPZ",    "TRC",     "TREX",  "TRGP",   "TRI",
"TRMR",   "TRN",   "TRNO",     "TROX",   "TRP",   "TRQ","TRUP",   "TRV", "TSE",   "TSI",   "TSL",
"TSLX",   "TSM",   "TSN",  "TSQ",   "TTC", "TTI",   "TTM",   "TTP",  "TUP","TVC",   "TVE","TWI",   "TWN",   "TWO",   "TWTR",    "TXT", "TYG",   "TYL",
"UAL", "UAN",   "UBA",   "UBP",    "UBS",   "UDR",   "UFI",   "UGI",   "UGP",   "UHS",   "UHT","UIS",   "UMC",   "UMH",    "UNF",   "UNH",   "UNM",   "UNP",
"UPS",   "URI",   "USA",   "USAC",   "USB","USDP", "USM",   "USNA",   "USPH",   "UTF",   "UTI",   "UTL", "UVE",   "UVV",    "VAC","VAL",   "VALE",
"VBF", "VCV",   "VEEV",   "VET",   "VFC",     "VGI",   "VGM",   "VGR",   "VHI","VIPS",   "VIV",   "VJET",   "VKQ",   "VLO",
"VLRS",   "VLT",   "VLY",    "VMC",   "VMI",   "VMO",   "VMW",   "VNCE","VNO",   "VOC",   "VOYA",   "VPG",   "VPV",
"VRTV",   "VSH",  "VTN",   "VTR", "VVC",   "VVI",   "VVR",  "WAB",  "WAL",   "WAT","WBS",   "WCC", "WCN",  "WDAY",    "WEA",   "WEC",   "WES",   "WEX",   "WFC",
"WGO", "WHG",   "WHR", "WIA",   "WIT",   "WIW",   "WLK",   "WLKP","WMB",   "WMC",   "WMK",   "WMS",   "WMT",   "WNC", "WNS",   "WOR",   "WPC",  "WPP",
"WRB",   "WRE", "WSM",   "WSO",   "WSR",   "WST",   "WTI",   "WTM",   "WTS","WTW","WWE",   "WWW","XEL",   "XIN",   "XOM",
"XPO", "XRX",  "XYL",  "YELP",  "YPF",   "YUM", "ZBK",   "ZEN",  "ZNH",  "ZTR",   "ZTS"]

#set up welcome menu for main menu options
print("\nWelcome to the Stock Ticker Application!")
print("\nMAIN MENU")
print("Main Menu Item 1: DJIA")
print("Main Menu Item 2: NASDAQ")
print("Main Menu Item 3: NYSE")

#accept user input, store it as variable mainMenuOption
mainMenuOption = int(input("\nChoose a menu option number: "))
#while user inputs number other than 1, 2, or 3
while (mainMenuOption != 1) and (mainMenuOption != 2) and (mainMenuOption != 3):
    #repeat asking for valid input
    mainMenuOption = int(input("\nInvalid number. Choose a new menu option number (1-3): "))

#set up menu for sub menu options
print("\nSUB MENU")
print("Sub Menu Item 1: Search by symbol")
print("Sub Menu Item 2: Display a random symbol")
print("Sub Menu Item 3: Display all symbols")

#accept user input, store it as variable subMenuOption
subMenuOption = int(input("\nChoose a sub menu option number: "))
#while user inputs number other than 1, 2, or 3
while (subMenuOption != 1) and (subMenuOption != 2) and (subMenuOption != 3):
    #repeat asking for valid input
    subMenuOption = int(input("\nInvalid number. Choose a new submenu option number (1-3): "))

#if user chooses main option 1 (DJIA)
if mainMenuOption == 1:
    #if user chooses sub option 1
    if subMenuOption == 1:
        #accept user input, store in variable tickerSymbol
        tickerSymbol = input("Enter a symbol: ")
        #while length of input is NOT 3, 4, or 5
        while (len(tickerSymbol) < 3) or (len(tickerSymbol) > 5):
            #repeat asking for valid input
            tickerSymbol = input("Invalid input. Enter a symbol (3-5 characters): ")
        #get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            #convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        #else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2)/round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 2
    elif subMenuOption == 2:
        #choose a random symbol from DJIA list, store in variable tickerSymbol
        tickerSymbol = random.choice(DJIA)
        # get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            #convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        # else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 3
    elif subMenuOption == 3:
        #iterate through all symbols in DJIA list
        for stock in DJIA:
            # assign the stock to variable tickerSymbol
            tickerSymbol = stock
            # get data on this symbol
            tickerData = yf.Ticker(tickerSymbol)
            # set variable to grab stock info from 1 day (today price)
            todayData = tickerData.history(period='1d')
            # display uppercase stock symbol
            sense.show_message(tickerSymbol.upper())
            # display new price of stock
            sense.show_message("{:.2f}".format(todayData['Close'][0]))
            # set variable to grab stock info from 2 days ago (yesterday price)
            yesterdayData = tickerData.history(period='2d')
            # formula for change, new price-old price
            change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
            # round change to 2 decimals
            change = round(change, 2)
            # if change is positive
            if change > 0:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change with a + sign
                sense.show_message("+{0}".format(change))
            # else
            else:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change as is (already will have a - sign)
                sense.show_message(change)
            # convert change back to int for math
            change = int(float(change))
            # formula for percent change, change/old price * 100
            percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
            # round percent change to 2 decimals
            percentChange = round(percentChange, 2)
            # if percent change is positive
            if percentChange > 0:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change with a + sign
                sense.show_message("+{0}%".format(percentChange))
            # else
            else:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change as is (already will have a - sign)
                sense.show_message("{0}%".format(percentChange))
            # display old price of stock
            sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))


#if user chooses main option 2 (NASDAQ)
elif mainMenuOption == 2:
    #if user chooses sub option 1
    if subMenuOption == 1:
        #accept user input, store in variable tickerSymbol
        tickerSymbol = input("Enter a symbol: ")
        #while length of input is NOT 3, 4, or 5
        while (len(tickerSymbol) < 3) or (len(tickerSymbol) > 5):
            #repeat asking for valid input
            tickerSymbol = input("Invalid input. Enter a symbol (3-5 characters): ")
        # get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        # else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 2
    elif subMenuOption == 2:
        #choose a random symbol from NASDAQ list, store in variable tickerSymbol
        tickerSymbol = random.choice(NASDAQ)
        # get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            #convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        # else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 3
    elif subMenuOption == 3:
        #iterate through all symbols in NASDAQ list
        for stock in NASDAQ:
            # assign the stock to variable tickerSymbol
            tickerSymbol = stock
            # get data on this symbol
            tickerData = yf.Ticker(tickerSymbol)
            # set variable to grab stock info from 1 day (today price)
            todayData = tickerData.history(period='1d')
            # display uppercase stock symbol
            sense.show_message(tickerSymbol.upper())
            # display new price of stock
            sense.show_message("{:.2f}".format(todayData['Close'][0]))
            # set variable to grab stock info from 2 days ago (yesterday price)
            yesterdayData = tickerData.history(period='2d')
            # formula for change, new price-old price
            change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
            # round change to 2 decimals
            change = round(change, 2)
            # if change is positive
            if change > 0:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change with a + sign
                sense.show_message("+{0}".format(change))
            # else
            else:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change as is (already will have a - sign)
                sense.show_message(change)
            # convert change back to int for math
            change = int(float(change))
            # formula for percent change, change/old price * 100
            percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
            # round percent change to 2 decimals
            percentChange = round(percentChange, 2)
            # if percent change is positive
            if percentChange > 0:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change with a + sign
                sense.show_message("+{0}%".format(percentChange))
            # else
            else:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change as is (already will have a - sign)
                sense.show_message("{0}%".format(percentChange))
            # display old price of stock
            sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))


#if user chooses main option 3 (NYSE)
elif mainMenuOption == 3:
    #if user chooses sub option 1
    if subMenuOption == 1:
        #accept user input, store in variable tickerSymbol
        tickerSymbol = input("Enter a symbol: ")
        #while length of input is NOT 3, 4, or 5
        while (len(tickerSymbol) < 3) or (len(tickerSymbol) > 5):
            #repeat asking for valid input
            tickerSymbol = input("Invalid input. Enter a symbol (3-5 characters): ")
        # get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            #convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        # else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 2
    elif subMenuOption == 2:
        #choose a random symbol from NYSE list, store in variable tickerSymbol
        tickerSymbol = random.choice(NYSE)
        # get data on this symbol
        tickerData = yf.Ticker(tickerSymbol)
        # set variable to grab stock info from 1 day (today price)
        todayData = tickerData.history(period='1d')
        # display uppercase stock symbol
        sense.show_message(tickerSymbol.upper())
        # display new price of stock
        sense.show_message("{:.2f}".format(todayData['Close'][0]))
        # set variable to grab stock info from 2 days ago (yesterday price)
        yesterdayData = tickerData.history(period='2d')
        # formula for change, new price-old price
        change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
        # round change to 2 decimals
        change = round(change, 2)
        # if change is positive
        if change > 0:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change with a + sign
            sense.show_message("+{0}".format(change))
        # else
        else:
            # convert change to string for sense hat emulator
            change = str(change)
            # display change as is (already will have a - sign)
            sense.show_message(change)
        # convert change back to int for math
        change = int(float(change))
        # formula for percent change, change/old price * 100
        percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
        # round percent change to 2 decimals
        percentChange = round(percentChange, 2)
        # if percent change is positive
        if percentChange > 0:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change with a + sign
            sense.show_message("+{0}%".format(percentChange))
        #else
        else:
            # convert percent change to string for sense hat emulator
            percentChange = str(percentChange)
            # display percent change as is (already will have a - sign)
            sense.show_message("{0}%".format(percentChange))
        # display old price of stock
        sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))

    #else if user chooses sub option 3
    elif subMenuOption == 3:
        #iterate through all symbols in NYSE list
        for stock in NYSE:
            # assign the stock to variable tickerSymbol
            tickerSymbol = stock
            # get data on this symbol
            tickerData = yf.Ticker(tickerSymbol)
            # set variable to grab stock info from 1 day (today price)
            todayData = tickerData.history(period='1d')
            # display uppercase stock symbol
            sense.show_message(tickerSymbol.upper())
            # display new price of stock
            sense.show_message("{:.2f}".format(todayData['Close'][0]))
            # set variable to grab stock info from 2 days ago (yesterday price)
            yesterdayData = tickerData.history(period='2d')
            # formula for change, new price-old price
            change = round(todayData['Close'][0], 2) - round(yesterdayData['Close'][0], 2)
            # round change to 2 decimals
            change = round(change, 2)
            # if change is positive
            if change > 0:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change with a + sign
                sense.show_message("+{0}".format(change))
            # else
            else:
                # convert change to string for sense hat emulator
                change = str(change)
                # display change as is (already will have a - sign)
                sense.show_message(change)
            # convert change back to int for math
            change = int(float(change))
            # formula for percent change, change/old price * 100
            percentChange = (round(change, 2) / round(yesterdayData['Close'][0], 2)) * 100
            # round percent change to 2 decimals
            percentChange = round(percentChange, 2)
            # if percent change is positive
            if percentChange > 0:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change with a + sign
                sense.show_message("+{0}%".format(percentChange))
            # else
            else:
                # convert percent change to string for sense hat emulator
                percentChange = str(percentChange)
                # display percent change as is (already will have a - sign)
                sense.show_message("{0}%".format(percentChange))
            #display old price of stock
            sense.show_message("{:.2f}".format(yesterdayData['Close'][0]))
