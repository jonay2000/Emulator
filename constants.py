# A = some register
# B = some register
# I = some immediate value
# P1 = some pointer to some value (imm)
# P2 = some pointer to some value (reg)


IS = {
	0x0000	:	["NOP",[0]],

	0x0001	:	["ADDABC",[1,1,1]],		# implemented
	0x0002	:	["ADDIBC",[0]],
	0x0003	:	["ADDAIC",[1,2,1]],		# implemented
	0x0004	:	["ADDIIC",[0]],
	0x0005	:	["ADDPBC",[0]],
	0x0006	:	["ADDAP1C",[0]],
	0x0006	:	["ADDAP2C",[0]],
	0x0007	:	["ADDP1P2C",[0]],
	0x0008	:	["ADDP2P1C",[0]],
	0x0009	:	["ADDP2P2C",[0]],
	0x000a	:	["ADDP1IC",[0]],
	0x000b	:	["ADDP2IC",[0]],
	0x000c	:	["ADDIP1C",[0]],
	0x000d	:	["ADDIP2C",[0]],
	0x000e	:	["ADDABP1",[0]],
	0x000f	:	["ADDIBP1",[0]],
	0x0010	:	["ADDAIP1",[0]],
	0x0011	:	["ADDIIP1",[0]],
	0x0012	:	["ADDPBP1",[0]],
	0x0013	:	["ADDAP1P1",[0]],
	0x0014	:	["ADDAP2P1",[0]],
	0x0015	:	["ADDP1P2P1",[0]],
	0x0016	:	["ADDP2P1P1",[0]],
	0x0017	:	["ADDP2P2P1",[0]],
	0x0018	:	["ADDP1IP1",[0]],
	0x0019	:	["ADDP2IP1",[0]],
	0x001a	:	["ADDIP1P1",[0]],
	0x001b	:	["ADDIP2P1",[0]],
	0x001c	:	["ADDABP2",[0]],
	0x001d	:	["ADDIBP2",[0]],
	0x001e	:	["ADDAIP2",[0]],
	0x001f	:	["ADDIIP2",[0]],
	0x0020	:	["ADDPBP2",[0]],
	0x0021	:	["ADDAP1P2",[0]],
	0x0022	:	["ADDAP2P2",[0]],
	0x0023	:	["ADDP1P2P2",[0]],
	0x0024	:	["ADDP2P1P2",[0]],
	0x0025	:	["ADDP2P2P2",[0]],
	0x0026	:	["ADDP1IP2",[0]],
	0x0027	:	["ADDP2IP2",[0]],
	0x0028	:	["ADDIP1P2",[0]],
	0x0029	:	["ADDIP2P2",[0]],


	0x002a	:	["SUBABC",[0]],
	0x002b	:	["SUBIBC",[0]],
	0x002c	:	["SUBAIC",[0]],
	0x002d	:	["SUBIIC",[0]],
	0x002e	:	["SUBPBC",[0]],
	0x002f	:	["SUBAP1C",[0]],
	0x0030	:	["SUBAP2C",[0]],
	0x0031	:	["SUBP1P2C",[0]],
	0x0032	:	["SUBP2P1C",[0]],
	0x0033	:	["SUBP2P2C",[0]],
	0x0034	:	["SUBP1IC",[0]],
	0x0035	:	["SUBP2IC",[0]],
	0x0036	:	["SUBIP1C",[0]],
	0x0037	:	["SUBIP2C",[0]],
	0x0038	:	["SUBABP1",[0]],
	0x0039	:	["SUBIBP1",[0]],
	0x003a	:	["SUBAIP1",[0]],
	0x003b	:	["SUBIIP1",[0]],
	0x003c	:	["SUBPBP1",[0]],
	0x003e	:	["SUBAP1P1",[0]],
	0x003f	:	["SUBAP2P1",[0]],
	0x0040	:	["SUBP1P2P1",[0]],
	0x0041	:	["SUBP2P1P1",[0]],
	0x0042	:	["SUBP2P2P1",[0]],
	0x0043	:	["SUBP1IP1",[0]],
	0x0044	:	["SUBP2IP1",[0]],
	0x0045	:	["SUBIP1P1",[0]],
	0x0046	:	["SUBIP2P1",[0]],
	0x0047	:	["SUBABP2",[0]],
	0x0048	:	["SUBIBP2",[0]],
	0x0049	:	["SUBAIP2",[0]],
	0x004a	:	["SUBIIP2",[0]],
	0x004b	:	["SUBPBP2",[0]],
	0x004c	:	["SUBAP1P2",[0]],
	0x004d	:	["SUBAP2P2",[0]],
	0x004e	:	["SUBP1P2P2",[0]],
	0x004f	:	["SUBP2P1P2",[0]],
	0x005a	:	["SUBP2P2P2",[0]],
	0x0051	:	["SUBP1IP2",[0]],
	0x0052	:	["SUBP2IP2",[0]],
	0x0053	:	["SUBIP1P2",[0]],
	0x0054	:	["SUBIP2P2",[0]],


	0x0055	:	["CMPAB",[0]],
	0x0056	:	["CMPIB",[0]],
	0x0057	:	["CMPAI",[0]],
	0x0058	:	["CMPII",[0]],
	0x0059	:	["CMPPB",[0]],
	0x005a	:	["CMPAP1",[0]],
	0x005b	:	["CMPAP2",[0]],
	0x005c	:	["CMPP1P2",[0]],
	0x005d	:	["CMPP2P1",[0]],
	0x005f	:	["CMPP2P2",[0]],
	0x0060	:	["CMPP1I",[0]],
	0x0061	:	["CMPP2I",[0]],
	0x0062	:	["CMPIP1",[0]],
	0x0063	:	["CMPIP2",[0]],


	0x0064	:	["XORABC",[0]],
	0x0065	:	["XORIBC",[0]],
	0x0066	:	["XORAIC",[0]],
	0x0067	:	["XORIIC",[0]],
	0x0068	:	["XORPBC",[0]],
	0x0069	:	["XORAP1C",[0]],
	0x0070	:	["XORAP2C",[0]],
	0x0071	:	["XORP1P2C",[0]],
	0x0072	:	["XORP2P1C",[0]],
	0x0073	:	["XORP2P2C",[0]],
	0x0074	:	["XORP1IC",[0]],
	0x0075	:	["XORP2IC",[0]],
	0x0076	:	["XORIP1C",[0]],
	0x0077	:	["XORIP2C",[0]],
	0x0078	:	["XORABP1",[0]],
	0x0079	:	["XORIBP1",[0]],
	0x007a	:	["XORAIP1",[0]],
	0x007b	:	["XORIIP1",[0]],
	0x007c	:	["XORPBP1",[0]],
	0x007d	:	["XORAP1P1",[0]],
	0x007e	:	["XORAP2P1",[0]],
	0x007f	:	["XORP1P2P1",[0]],
	0x0080	:	["XORP2P1P1",[0]],
	0x0081	:	["XORP2P2P1",[0]],
	0x0082	:	["XORP1IP1",[0]],
	0x0083	:	["XORP2IP1",[0]],
	0x0084	:	["XORIP1P1",[0]],
	0x0085	:	["XORIP2P1",[0]],
	0x0086	:	["XORABP2",[0]],
	0x0087	:	["XORIBP2",[0]],
	0x0088	:	["XORAIP2",[0]],
	0x0089	:	["XORIIP2",[0]],
	0x008a	:	["XORPBP2",[0]],
	0x008b	:	["XORAP1P2",[0]],
	0x008c	:	["XORAP2P2",[0]],
	0x008d	:	["XORP1P2P2",[0]],
	0x008e	:	["XORP2P1P2",[0]],
	0x008f	:	["XORP2P2P2",[0]],
	0x0090	:	["XORP1IP2",[0]],
	0x0091	:	["XORP2IP2",[0]],
	0x0092	:	["XORIP1P2",[0]],
	0x0093	:	["XORIP2P2",[0]],


	0x0094	:	["ANDABC",[0]],
	0x0095	:	["ANDIBC",[0]],
	0x0096	:	["ANDAIC",[0]],
	0x0097	:	["ANDIIC",[0]],
	0x0098	:	["ANDPBC",[0]],
	0x0099	:	["ANDAP1C",[0]],
	0x009a	:	["ANDAP2C",[0]],
	0x009b	:	["ANDP1P2C",[0]],
	0x009c	:	["ANDP2P1C",[0]],
	0x009d	:	["ANDP2P2C",[0]],
	0x009e	:	["ANDP1IC",[0]],
	0x009f	:	["ANDP2IC",[0]],
	0x00a0	:	["ANDIP1C",[0]],
	0x00a1	:	["ANDIP2C",[0]],
	0x00a2	:	["ANDABP1",[0]],
	0x00a3	:	["ANDIBP1",[0]],
	0x00a4	:	["ANDAIP1",[0]],
	0x00a5	:	["ANDIIP1",[0]],
	0x00a6	:	["ANDPBP1",[0]],
	0x00a7	:	["ANDAP1P1",[0]],
	0x00a8	:	["ANDAP2P1",[0]],
	0x00a9	:	["ANDP1P2P1",[0]],
	0x00aa	:	["ANDP2P1P1",[0]],
	0x00ab	:	["ANDP2P2P1",[0]],
	0x00ac	:	["ANDP1IP1",[0]],
	0x00ad	:	["ANDP2IP1",[0]],
	0x00ae	:	["ANDIP1P1",[0]],
	0x00af	:	["ANDIP2P1",[0]],
	0x00b0	:	["ANDABP2",[0]],
	0x00b1	:	["ANDIBP2",[0]],
	0x00b2	:	["ANDAIP2",[0]],
	0x00b3	:	["ANDIIP2",[0]],
	0x00b4	:	["ANDPBP2",[0]],
	0x00b5	:	["ANDAP1P2",[0]],
	0x00b6	:	["ANDAP2P2",[0]],
	0x00b7	:	["ANDP1P2P2",[0]],
	0x00b8	:	["ANDP2P1P2",[0]],
	0x00b9	:	["ANDP2P2P2",[0]],
	0x00ba	:	["ANDP1IP2",[0]],
	0x00bb	:	["ANDP2IP2",[0]],
	0x00bc	:	["ANDIP1P2",[0]],
	0x00bd	:	["ANDIP2P2",[0]],


	0x00be	:	["NANDABC",[0]],
	0x00bf	:	["NANDIBC",[0]],
	0x00c0	:	["NANDAIC",[0]],
	0x00c1	:	["NANDIIC",[0]],
	0x00c2	:	["NANDPBC",[0]],
	0x00c3	:	["NANDAP1C",[0]],
	0x00c4	:	["NANDAP2C",[0]],
	0x00c5	:	["NANDP1P2C",[0]],
	0x00c6	:	["NANDP2P1C",[0]],
	0x00c7	:	["NANDP2P2C",[0]],
	0x00c8	:	["NANDP1IC",[0]],
	0x00c9	:	["NANDP2IC",[0]],
	0x00ca	:	["NANDIP1C",[0]],
	0x00cb	:	["NANDIP2C",[0]],
	0x00cd	:	["NANDABP1",[0]],
	0x00ce	:	["NANDIBP1",[0]],
	0x00cf	:	["NANDAIP1",[0]],
	0x00d0	:	["NANDIIP1",[0]],
	0x00d1	:	["NANDPBP1",[0]],
	0x00d2	:	["NANDAP1P1",[0]],
	0x00d3	:	["NANDAP2P1",[0]],
	0x00d4	:	["NANDP1P2P1",[0]],
	0x00d5	:	["NANDP2P1P1",[0]],
	0x00d6	:	["NANDP2P2P1",[0]],
	0x00d7	:	["NANDP1IP1",[0]],
	0x00d8	:	["NANDP2IP1",[0]],
	0x00d9	:	["NANDIP1P1",[0]],
	0x00da	:	["NANDIP2P1",[0]],
	0x00db	:	["NANDABP2",[0]],
	0x00dc	:	["NANDIBP2",[0]],
	0x00dd	:	["NANDAIP2",[0]],
	0x00de	:	["NANDIIP2",[0]],
	0x00df	:	["NANDPBP2",[0]],
	0x00e0	:	["NANDAP1P2",[0]],
	0x00e1	:	["NANDAP2P2",[0]],
	0x00e2	:	["NANDP1P2P2",[0]],
	0x00e3	:	["NANDP2P1P2",[0]],
	0x00e4	:	["NANDP2P2P2",[0]],
	0x00e5	:	["NANDP1IP2",[0]],
	0x00e6	:	["NANDP2IP2",[0]],
	0x00e7	:	["NANDIP1P2",[0]],
	0x00e8	:	["NANDIP2P2",[0]],


	0x00e9	:	["ORABC",[0]],
	0x00ea	:	["ORIBC",[0]],
	0x00eb	:	["ORAIC",[0]],
	0x00ec	:	["ORIIC",[0]],
	0x00ed	:	["ORPBC",[0]],
	0x00ee	:	["ORAP1C",[0]],
	0x00ef	:	["ORAP2C",[0]],
	0x00f0	:	["ORP1P2C",[0]],
	0x00f1	:	["ORP2P1C",[0]],
	0x00f2	:	["ORP2P2C",[0]],
	0x00f3	:	["ORP1IC",[0]],
	0x00f4	:	["ORP2IC",[0]],
	0x00f5	:	["ORIP1C",[0]],
	0x00f6	:	["ORIP2C",[0]],
	0x00f7	:	["ORABP1",[0]],
	0x00f8	:	["ORIBP1",[0]],
	0x00f9	:	["ORAIP1",[0]],
	0x00fa	:	["ORIIP1",[0]],
	0x00fb	:	["ORPBP1",[0]],
	0x00fc	:	["ORAP1P1",[0]],
	0x00fd	:	["ORAP2P1",[0]],
	0x00fe	:	["ORP1P2P1",[0]],
	0x00ff	:	["ORP2P1P1",[0]],
	0x0100	:	["ORP2P2P1",[0]],
	0x0101	:	["ORP1IP1",[0]],
	0x0102	:	["ORP2IP1",[0]],
	0x0103	:	["ORIP1P1",[0]],
	0x0104	:	["ORIP2P1",[0]],
	0x0105	:	["ORABP2",[0]],
	0x0106	:	["ORIBP2",[0]],
	0x0107	:	["ORAIP2",[0]],
	0x0108	:	["ORIIP2",[0]],
	0x0109	:	["ORPBP2",[0]],
	0x010a	:	["ORAP1P2",[0]],
	0x010b	:	["ORAP2P2",[0]],
	0x010c	:	["ORP1P2P2",[0]],
	0x010d	:	["ORP2P1P2",[0]],
	0x010e	:	["ORP2P2P2",[0]],
	0x010f	:	["ORP1IP2",[0]],
	0x0110	:	["ORP2IP2",[0]],
	0x0111	:	["ORIP1P2",[0]],
	0x0112	:	["ORIP2P2",[0]],


	0x0113	:	["NORABC",[0]],
	0x0114	:	["NORIBC",[0]],
	0x0115	:	["NORAIC",[0]],
	0x0116	:	["NORIIC",[0]],
	0x0117	:	["NORPBC",[0]],
	0x0118	:	["NORAP1C",[0]],
	0x0119	:	["NORAP2C",[0]],
	0x011a	:	["NORP1P2C",[0]],
	0x011b	:	["NORP2P1C",[0]],
	0x011c	:	["NORP2P2C",[0]],
	0x011d	:	["NORP1IC",[0]],
	0x011e	:	["NORP2IC",[0]],
	0x011f	:	["NORIP1C",[0]],
	0x0120	:	["NORIP2C",[0]],
	0x0121	:	["NORABP1",[0]],
	0x0122	:	["NORIBP1",[0]],
	0x0123	:	["NORAIP1",[0]],
	0x0124	:	["NORIIP1",[0]],
	0x0125	:	["NORPBP1",[0]],
	0x0126	:	["NORAP1P1",[0]],
	0x0127	:	["NORAP2P1",[0]],
	0x0128	:	["NORP1P2P1",[0]],
	0x0129	:	["NORP2P1P1",[0]],
	0x012a	:	["NORP2P2P1",[0]],
	0x012b	:	["NORP1IP1",[0]],
	0x012c	:	["NORP2IP1",[0]],
	0x012d	:	["NORIP1P1",[0]],
	0x012e	:	["NORIP2P1",[0]],
	0x012f	:	["NORABP2",[0]],
	0x0130	:	["NORIBP2",[0]],
	0x0131	:	["NORAIP2",[0]],
	0x0132	:	["NORIIP2",[0]],
	0x0133	:	["NORPBP2",[0]],
	0x0134	:	["NORAP1P2",[0]],
	0x0135	:	["NORAP2P2",[0]],
	0x0136	:	["NORP1P2P2",[0]],
	0x0137	:	["NORP2P1P2",[0]],
	0x0138	:	["NORP2P2P2",[0]],
	0x0139	:	["NORP1IP2",[0]],
	0x013a	:	["NORP2IP2",[0]],
	0x013b	:	["NORIP1P2",[0]],
	0x013c	:	["NORIP2P2",[0]],


	0x013d	:	["ALSABC",[0]],
	0x013e	:	["ALSIBC",[0]],
	0x013f	:	["ALSAIC",[0]],
	0x0140	:	["ALSIIC",[0]],
	0x0141	:	["ALSPBC",[0]],
	0x0142	:	["ALSAP1C",[0]],
	0x0143	:	["ALSAP2C",[0]],
	0x0144	:	["ALSP1P2C",[0]],
	0x0145	:	["ALSP2P1C",[0]],
	0x0146	:	["ALSP2P2C",[0]],
	0x0147	:	["ALSP1IC",[0]],
	0x0148	:	["ALSP2IC",[0]],
	0x0149	:	["ALSIP1C",[0]],
	0x014a	:	["ALSIP2C",[0]],
	0x014b	:	["ALSABP1",[0]],
	0x014c	:	["ALSIBP1",[0]],
	0x014d	:	["ALSAIP1",[0]],
	0x014e	:	["ALSIIP1",[0]],
	0x014f	:	["ALSPBP1",[0]],
	0x0150	:	["ALSAP1P1",[0]],
	0x0151	:	["ALSAP2P1",[0]],
	0x0152	:	["ALSP1P2P1",[0]],
	0x0153	:	["ALSP2P1P1",[0]],
	0x0154	:	["ALSP2P2P1",[0]],
	0x0155	:	["ALSP1IP1",[0]],
	0x0156	:	["ALSP2IP1",[0]],
	0x0157	:	["ALSIP1P1",[0]],
	0x0158	:	["ALSIP2P1",[0]],
	0x0159	:	["ALSABP2",[0]],
	0x015a	:	["ALSIBP2",[0]],
	0x015b	:	["ALSAIP2",[0]],
	0x015c	:	["ALSIIP2",[0]],
	0x015d	:	["ALSPBP2",[0]],
	0x015e	:	["ALSAP1P2",[0]],
	0x015f	:	["ALSAP2P2",[0]],
	0x0160	:	["ALSP1P2P2",[0]],
	0x0161	:	["ALSP2P1P2",[0]],
	0x0162	:	["ALSP2P2P2",[0]],
	0x0163	:	["ALSP1IP2",[0]],
	0x0164	:	["ALSP2IP2",[0]],
	0x0165	:	["ALSIP1P2",[0]],
	0x0166	:	["ALSIP2P2",[0]],


	0x0167	:	["ALRABC",[0]],
	0x0168	:	["ALRIBC",[0]],
	0x0169	:	["ALRAIC",[0]],
	0x016a	:	["ALRIIC",[0]],
	0x016b	:	["ALRPBC",[0]],
	0x016c	:	["ALRAP1C",[0]],
	0x016d	:	["ALRAP2C",[0]],
	0x016e	:	["ALRP1P2C",[0]],
	0x016f	:	["ALRP2P1C",[0]],
	0x0170	:	["ALRP2P2C",[0]],
	0x0171	:	["ALRP1IC",[0]],
	0x0172	:	["ALRP2IC",[0]],
	0x0173	:	["ALRIP1C",[0]],
	0x0174	:	["ALRIP2C",[0]],
	0x0175	:	["ALRABP1",[0]],
	0x0176	:	["ALRIBP1",[0]],
	0x0177	:	["ALRAIP1",[0]],
	0x0178	:	["ALRIIP1",[0]],
	0x0179	:	["ALRPBP1",[0]],
	0x017a	:	["ALRAP1P1",[0]],
	0x017b	:	["ALRAP2P1",[0]],
	0x017c	:	["ALRP1P2P1",[0]],
	0x017d	:	["ALRP2P1P1",[0]],
	0x017e	:	["ALRP2P2P1",[0]],
	0x017f	:	["ALRP1IP1",[0]],
	0x0180	:	["ALRP2IP1",[0]],
	0x0181	:	["ALRIP1P1",[0]],
	0x0182	:	["ALRIP2P1",[0]],
	0x0183	:	["ALRABP2",[0]],
	0x0184	:	["ALRIBP2",[0]],
	0x0185	:	["ALRAIP2",[0]],
	0x0186	:	["ALRIIP2",[0]],
	0x0187	:	["ALRPBP2",[0]],
	0x0188	:	["ALRAP1P2",[0]],
	0x0189	:	["ALRAP2P2",[0]],
	0x018a	:	["ALRP1P2P2",[0]],
	0x018b	:	["ALRP2P1P2",[0]],
	0x018c	:	["ALRP2P2P2",[0]],
	0x018d	:	["ALRP1IP2",[0]],
	0x018e	:	["ALRP2IP2",[0]],
	0x018f	:	["ALRIP1P2",[0]],
	0x0190	:	["ALRIP2P2",[0]],


	0x0191	:	["NOTAC",[0]],
	0x0192	:	["NOTIC",[0]],
	0x0193	:	["NOTP1C",[0]],
	0x0194	:	["NOTP2C",[0]],
	0x0195	:	["NOTAP1",[0]],
	0x0196	:	["NOTIP1",[0]],
	0x0197	:	["NOTPP1",[0]],
	0x0198	:	["NOTP2P1",[0]],
	0x0199	:	["NOTAP2",[0]],
	0x019a	:	["NOTIP2",[0]],
	0x019b	:	["NOTP1P2",[0]],
	0x019c	:	["NOTP2P2",[0]],


	0x019d	:	["MULABC",[0]],
	0x019e	:	["MULIBC",[0]],
	0x019f	:	["MULAIC",[0]],
	0x01a0	:	["MULIIC",[0]],
	0x01a1	:	["MULPBC",[0]],
	0x01a2	:	["MULAP1C",[0]],
	0x01a3	:	["MULAP2C",[0]],
	0x01a4	:	["MULP1P2C",[0]],
	0x01a5	:	["MULP2P1C",[0]],
	0x01a6	:	["MULP2P2C",[0]],
	0x01a7	:	["MULP1IC",[0]],
	0x01a8	:	["MULP2IC",[0]],
	0x01a9	:	["MULIP1C",[0]],
	0x01aa	:	["MULIP2C",[0]],
	0x01ab	:	["MULABP1",[0]],
	0x01ac	:	["MULIBP1",[0]],
	0x01ad	:	["MULAIP1",[0]],
	0x01ae	:	["MULIIP1",[0]],
	0x01af	:	["MULPBP1",[0]],
	0x01b0	:	["MULAP1P1",[0]],
	0x01b1	:	["MULAP2P1",[0]],
	0x01b2	:	["MULP1P2P1",[0]],
	0x01b3	:	["MULP2P1P1",[0]],
	0x01b4	:	["MULP2P2P1",[0]],
	0x01b5	:	["MULP1IP1",[0]],
	0x01b6	:	["MULP2IP1",[0]],
	0x01b7	:	["MULIP1P1",[0]],
	0x01b8	:	["MULIP2P1",[0]],
	0x01b9	:	["MULABP2",[0]],
	0x01ba	:	["MULIBP2",[0]],
	0x01bb	:	["MULAIP2",[0]],
	0x01bc	:	["MULIIP2",[0]],
	0x01bd	:	["MULPBP2",[0]],
	0x01be	:	["MULAP1P2",[0]],
	0x01bf	:	["MULAP2P2",[0]],
	0x01c0	:	["MULP1P2P2",[0]],
	0x01c1	:	["MULP2P1P2",[0]],
	0x01c2	:	["MULP2P2P2",[0]],
	0x01c3	:	["MULP1IP2",[0]],
	0x01c4	:	["MULP2IP2",[0]],
	0x01c5	:	["MULIP1P2",[0]],
	0x01c6	:	["MULIP2P2",[0]],


	0x01c7	:	["DIVABC",[0]],
	0x01c8	:	["DIVIBC",[0]],
	0x01c9	:	["DIVAIC",[0]],
	0x01ca	:	["DIVIIC",[0]],
	0x01cb	:	["DIVPBC",[0]],
	0x01cc	:	["DIVAP1C",[0]],
	0x01cd	:	["DIVAP2C",[0]],
	0x01ce	:	["DIVP1P2C",[0]],
	0x01cf	:	["DIVP2P1C",[0]],
	0x01d0	:	["DIVP2P2C",[0]],
	0x01d1	:	["DIVP1IC",[0]],
	0x01d2	:	["DIVP2IC",[0]],
	0x01d3	:	["DIVIP1C",[0]],
	0x01d4	:	["DIVIP2C",[0]],
	0x01d5	:	["DIVABP1",[0]],
	0x01d6	:	["DIVIBP1",[0]],
	0x01d7	:	["DIVAIP1",[0]],
	0x01d8	:	["DIVIIP1",[0]],
	0x01d9	:	["DIVPBP1",[0]],
	0x01da	:	["DIVAP1P1",[0]],
	0x01db	:	["DIVAP2P1",[0]],
	0x01dc	:	["DIVP1P2P1",[0]],
	0x01dd	:	["DIVP2P1P1",[0]],
	0x01de	:	["DIVP2P2P1",[0]],
	0x01df	:	["DIVP1IP1",[0]],
	0x01e0	:	["DIVP2IP1",[0]],
	0x01e1	:	["DIVIP1P1",[0]],
	0x01e2	:	["DIVIP2P1",[0]],
	0x01e3	:	["DIVABP2",[0]],
	0x01e4	:	["DIVIBP2",[0]],
	0x01e5	:	["DIVAIP2",[0]],
	0x01e6	:	["DIVIIP2",[0]],
	0x01e7	:	["DIVPBP2",[0]],
	0x01e8	:	["DIVAP1P2",[0]],
	0x01e9	:	["DIVAP2P2",[0]],
	0x01ea	:	["DIVP1P2P2",[0]],
	0x01eb	:	["DIVP2P1P2",[0]],
	0x01ec	:	["DIVP2P2P2",[0]],
	0x01ed	:	["DIVP1IP2",[0]],
	0x01ee	:	["DIVP2IP2",[0]],
	0x01ef	:	["DIVIP1P2",[0]],
	0x01f0	:	["DIVIP2P2",[0]],


	0x01f1	:	["MODABC",[0]],
	0x01f2	:	["MODIBC",[0]],
	0x01f3	:	["MODAIC",[0]],
	0x01f4	:	["MODIIC",[0]],
	0x01f5	:	["MODPBC",[0]],
	0x01f6	:	["MODAP1C",[0]],
	0x01f7	:	["MODAP2C",[0]],
	0x01f8	:	["MODP1P2C",[0]],
	0x01f9	:	["MODP2P1C",[0]],
	0x01fa	:	["MODP2P2C",[0]],
	0x01fb	:	["MODP1IC",[0]],
	0x01fc	:	["MODP2IC",[0]],
	0x01fd	:	["MODIP1C",[0]],
	0x01fe	:	["MODIP2C",[0]],
	0x01ff	:	["MODABP1",[0]],
	0x0200	:	["MODIBP1",[0]],
	0x0201	:	["MODAIP1",[0]],
	0x0202	:	["MODIIP1",[0]],
	0x0203	:	["MODPBP1",[0]],
	0x0204	:	["MODAP1P1",[0]],
	0x0205	:	["MODAP2P1",[0]],
	0x0206	:	["MODP1P2P1",[0]],
	0x0207	:	["MODP2P1P1",[0]],
	0x0208	:	["MODP2P2P1",[0]],
	0x0209	:	["MODP1IP1",[0]],
	0x020a	:	["MODP2IP1",[0]],
	0x020b	:	["MODIP1P1",[0]],
	0x020c	:	["MODIP2P1",[0]],
	0x020d	:	["MODABP2",[0]],
	0x020e	:	["MODIBP2",[0]],
	0x020f	:	["MODAIP2",[0]],
	0x0210	:	["MODIIP2",[0]],
	0x0211	:	["MODPBP2",[0]],
	0x0212	:	["MODAP1P2",[0]],
	0x0213	:	["MODAP2P2",[0]],
	0x0214	:	["MODP1P2P2",[0]],
	0x0215	:	["MODP2P1P2",[0]],
	0x0216	:	["MODP2P2P2",[0]],
	0x0217	:	["MODP1IP2",[0]],
	0x0218	:	["MODP2IP2",[0]],
	0x0219	:	["MODIP1P2",[0]],
	0x021a	:	["MODIP2P2",[0]],
	

	0x021b	:	["POPA",[0]],			# in-progress
	0x021c	:	["POPP1",[0]],			# in-progress
	0x021d	:	["POPP2",[0]],			# in-progress


	0x021e	:	["PUSHA",[0]],			# in-progress
	0x021f	:	["PUSHI",[0]],			# in-progress
	0x0221	:	["PUSHP1",[0]],			# in-progress
	0x0222	:	["PUSHP2",[0]],			# in-progress


	0x0223	:	["RET",[0]],			# in-progress
	0x0224	:	["CALL",[0]],			# in-progress


	0x0225	:	["MOVAB",[1,1]],		# implemented
	0x0226	:	["MOVAI",[1,2]],		# implemented
	0x0227	:	["MOVAP1",[0]],
	0x0228	:	["MOVAP2",[0]],
	0x0229	:	["MOVP1B",[0]],
	0x022a	:	["MOVP1I",[0]],
	0x022b	:	["MOVP1P1",[0]],
	0x022c	:	["MOVP1P2",[0]],
	0x022d	:	["MOVP2B",[0]],
	0x022e	:	["MOVP2I",[0]],
	0x022f	:	["MOVP2P1",[0]],
	0x0230	:	["MOVP2P2",[0]],


	0x0231	:	["INT",[0]],


	0x0232	:	["JMPI",[2]],
	0x0233	:	["JMPNEGI",[0]],
	0x0234	:	["JMPABSI",[0]],


	0x0235	:	["JMPIFEQUALI",[0]],
	0x0236	:	["JMPIFEQUALNEGI",[0]],
	0x0237	:	["JMPIFEQUALABSI",[0]],


	0x0238	:	["JMPIFGREATERI",[0]],
	0x0239	:	["JMPIFGREATERNEGI",[0]],
	0x023a	:	["JMPIFGREATERABSI",[0]],


	0x023b	:	["JMPIFLESSI",[0]],
	0x023c	:	["JMPIFLESSNEGI",[0]],
	0x023e	:	["JMPIFLESSABSI",[0]],


	0x023f	:	["JMPIFNOTEQUALI",[0]],
	0x0240	:	["JMPIFNOTEQUALNEGI",[0]],
	0x0241	:	["JMPIFNOTEQUALABSI",[0]],
}




