import unittest
from TestUtils import TestUtils


class TestSymbolTable(unittest.TestCase):
    # def test_0(self):
    #     input = ["INSERT a1 number", "INSERT b2 string"]
    #     expected = ["success", "success"]

    #     self.assertTrue(TestUtils.check(input, expected, 100))

    # def test_1(self):
    #     input = ["INSERT x number", "INSERT y string", "INSERT x string"]
    #     expected = ["Redeclared: INSERT x string"]

    #     self.assertTrue(TestUtils.check(input, expected, 101))

    # def test_2(self):
    #     input = [
    #         "INSERT x number",
    #         "INSERT y string",
    #         "ASSIGN x 15",
    #         "ASSIGN y 17",
    #         "ASSIGN x 'abc'",
    #     ]
    #     expected = ["TypeMismatch: ASSIGN y 17"]

    #     self.assertTrue(TestUtils.check(input, expected, 102))

    # def test_3(self):
    #     input = [
    #         "INSERT x number",
    #         "INSERT y string",
    #         "BEGIN",
    #         "INSERT x number",
    #         "BEGIN",
    #         "INSERT y string",
    #         "END",
    #         "END",
    #     ]
    #     expected = ["success", "success", "success", "success"]

    #     self.assertTrue(TestUtils.check(input, expected, 103))

    # def test_4(self):
    #     input = [
    #         "INSERT x number",
    #         "INSERT y string",
    #         "BEGIN",
    #         "INSERT x number",
    #         "LOOKUP x",
    #         "LOOKUP y",
    #         "END",
    #     ]
    #     expected = ["success", "success", "success", "1", "0"]

    #     self.assertTrue(TestUtils.check(input, expected, 104))

    # def test_5(self):
    #     input = [
    #         "INSERT x number",
    #         "INSERT y string",
    #         "BEGIN",
    #         "INSERT x number",
    #         "INSERT z number",
    #         "PRINT",
    #         "END",
    #     ]
    #     expected = ["success", "success", "success", "success", "y//0 x//1 z//1"]

    #     self.assertTrue(TestUtils.check(input, expected, 105))

    # def test_6(self):
    #     input = [
    #         "INSERT x number",
    #         "INSERT y string",
    #         "BEGIN",
    #         "INSERT x number",
    #         "INSERT z number",
    #         "RPRINT",
    #         "END",
    #     ]
    #     expected = ["success", "success", "success", "success", "z//1 x//1 y//0"]

    #     self.assertTrue(TestUtils.check(input, expected, 106))
    # ---------------------------------------------------- START TESTING ----------------------------------------------------
    # INSERT ----------------------------------------------------------------------------------------------------------------
    def test_0(self):
        input = ["INSERT x number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10000))

    def test_1(self):
        input = ["INSERT x string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10001))

    def test_2(self):
        input = ["INSERT y1 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10002))

    def test_3(self):
        input = ["INSERT y1 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10003))

    def test_4(self):
        input = ["INSERT yY2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10004))

    def test_5(self):
        input = ["INSERT yY2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10005))

    def test_6(self):
        input = ["INSERT yY_2 number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10006))

    def test_7(self):
        input = ["INSERT yY_2 string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10007))

    def test_8(self):
        input = ["INSERT y_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10008))

    def test_9(self):
        input = ["INSERT y_ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10009))

    def test_10(self):
        input = ["INSERT y2_ number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10010))

    def test_11(self):
        input = ["INSERT y2__ string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10011))

    def test_12(self):
        input = ["INSERT string string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10012))

    def test_13(self):
        input = ["INSERT string number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10013))

    def test_14(self):
        input = ["INSERT number string"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10014))

    def test_15(self):
        input = ["INSERT number number"]
        expected = ["success"]
        self.assertTrue(TestUtils.check(input, expected, 10015))
      
    def test_16(self):
        input = ["INSERT X string"]
        expected = ["Invalid: INSERT X string"]
        self.assertTrue(TestUtils.check(input, expected, 10016))

    def test_17(self):
        input = ["INSERT X number"]
        expected = ["Invalid: INSERT X number"]
        self.assertTrue(TestUtils.check(input, expected, 10017))

    def test_18(self):
        input = ["INSERT Xy string"]
        expected = ["Invalid: INSERT Xy string"]
        self.assertTrue(TestUtils.check(input, expected, 10018))

    def test_19(self):
        input = ["INSERT Xy number"]
        expected = ["Invalid: INSERT Xy number"]
        self.assertTrue(TestUtils.check(input, expected, 10019))

    def test_20(self):
        input = ["INSERT X1 string"]
        expected = ["Invalid: INSERT X1 string"]
        self.assertTrue(TestUtils.check(input, expected, 10020))

    def test_21(self):
        input = ["INSERT X1 number"]
        expected = ["Invalid: INSERT X1 number"]
        self.assertTrue(TestUtils.check(input, expected, 10021))

    def test_22(self):
        input = ["INSERT _ string"]
        expected = ["Invalid: INSERT _ string"]
        self.assertTrue(TestUtils.check(input, expected, 10022))

    def test_23(self):
        input = ["INSERT ___ number"]
        expected = ["Invalid: INSERT ___ number"]
        self.assertTrue(TestUtils.check(input, expected, 10023))

    def test_24(self):
        input = ["INSERT 3x string"]
        expected = ["Invalid: INSERT 3x string"]
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_25(self):
        input = ["INSERT 3x number"]
        expected = ["Invalid: INSERT 3x number"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_26(self):
        input = [" INSERT x string"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10026))

    def test_27(self):
        input = ["INSERT  x string"]
        expected = ["Invalid: INSERT  x string"]
        self.assertTrue(TestUtils.check(input, expected, 10027))

    def test_28(self):
        input = ["INSERT x  string"]
        expected = ["Invalid: INSERT x  string"]
        self.assertTrue(TestUtils.check(input, expected, 10028))

    def test_29(self):
        input = ["INSERT x string "]
        expected = ["Invalid: INSERT x string "]
        self.assertTrue(TestUtils.check(input, expected, 10029))

    def test_30(self):
        input = ["INSERT x string number"]
        expected = ["Invalid: INSERT x string number"]
        self.assertTrue(TestUtils.check(input, expected, 10030))

    def test_31(self):
        input = ["INSERT bc ed string"]
        expected = ["Invalid: INSERT bc ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10031))

    def test_32(self):
        input = ["INSERT bc@ed number"]
        expected = ["Invalid: INSERT bc@ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10032))

    def test_33(self):
        input = ["INSERT bc@ed string"]
        expected = ["Invalid: INSERT bc@ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10033))

    def test_34(self):
        input = ["INSERT bc`ed number"]
        expected = ["Invalid: INSERT bc`ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10034))

    def test_35(self):
        input = ["INSERT bc`ed string"]
        expected = ["Invalid: INSERT bc`ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10035))

    def test_36(self):
        input = ["INSERT bc~ed number"]
        expected = ["Invalid: INSERT bc~ed number"]
        self.assertTrue(TestUtils.check(input, expected, 10036))

    def test_37(self):
        input = ["INSERT bc~ed string"]
        expected = ["Invalid: INSERT bc~ed string"]
        self.assertTrue(TestUtils.check(input, expected, 10037))

    def test_38(self):
        input = ["INSERT bced Number"]
        expected = ["Invalid: INSERT bced Number"]
        self.assertTrue(TestUtils.check(input, expected, 10038))

    def test_39(self):
        input = ["INSERT bced String"]
        expected = ["Invalid: INSERT bced String"]
        self.assertTrue(TestUtils.check(input, expected, 10039))

    def test_40(self):
        input = ["INSERT bced nuMber"]
        expected = ["Invalid: INSERT bced nuMber"]
        self.assertTrue(TestUtils.check(input, expected, 10040))

    def test_41(self):
        input = ["INSERT bced stRing"]
        expected = ["Invalid: INSERT bced stRing"]
        self.assertTrue(TestUtils.check(input, expected, 10041))

    def test_42(self):
        input = ["INSERT bced "]
        expected = ["Invalid: INSERT bced "]
        self.assertTrue(TestUtils.check(input, expected, 10042))

    def test_43(self):
        input = ["INSERT bced"]
        expected = ["Invalid: INSERT bced"]
        self.assertTrue(TestUtils.check(input, expected, 10043))

    def test_44(self):
        input = ["INSERT string bced"]
        expected = ["Invalid: INSERT string bced"]
        self.assertTrue(TestUtils.check(input, expected, 10044))

    def test_45(self):
        input = ["INSERT number bced"]
        expected = ["Invalid: INSERT number bced"]
        self.assertTrue(TestUtils.check(input, expected, 10045))

    def test_46(self):
        input = ["INSERT  string"]
        expected = ["Invalid: INSERT  string"]
        self.assertTrue(TestUtils.check(input, expected, 10046))

    def test_47(self):
        input = ["INSERT  number"]
        expected = ["Invalid: INSERT  number"]
        self.assertTrue(TestUtils.check(input, expected, 10047))

    def test_48(self):
        input = ["INSERT  "]
        expected = ["Invalid: INSERT  "]
        self.assertTrue(TestUtils.check(input, expected, 10048))

    def test_49(self):
        input = ["INSERT "]
        expected = ["Invalid: INSERT "]
        self.assertTrue(TestUtils.check(input, expected, 10049))

    def test_50(self):
        input = ["INSERT"]
        expected = ["Invalid: INSERT"]
        self.assertTrue(TestUtils.check(input, expected, 10050))

    def test_51(self):
        input = ["INSERT x number", "INSERT xy string"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10051))

    def test_52(self):
        input = ["INSERT x number", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10052))

    def test_53(self):
        input = ["INSERT x number", "INSERT x string"]
        expected = ["Redeclared: INSERT x string"]
        self.assertTrue(TestUtils.check(input, expected, 10053))

    def test_54(self):
        input = ["INSERT x number", "INSERT a number", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10054))

    def test_55(self):
        input = ["INSERT abcde number", "INSERT abc number", "INSERT abcd number", "INSERT abcdef number", "INSERT abc number", "INSERT abcde number"]
        expected = ["Redeclared: INSERT abc number"]
        self.assertTrue(TestUtils.check(input, expected, 10055))
    # ASSIGN ----------------------------------------------------------------------------------------------------------------
    def test_56(self):
        input = ["INSERT x number", "ASSIGN x 0"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10056))

    def test_57(self):
        input = ["INSERT x number", "ASSIGN x 12"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10057))

    def test_58(self):
        input = ["INSERT x number", "ASSIGN x 123"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10058))

    def test_59(self):
        input = ["INSERT x number", "ASSIGN x 10.1"]
        expected = ["Invalid: ASSIGN x 10.1"]
        self.assertTrue(TestUtils.check(input, expected, 10059))

    def test_60(self):
        input = ["INSERT x number", "ASSIGN x -1"]
        expected = ["Invalid: ASSIGN x -1"]
        self.assertTrue(TestUtils.check(input, expected, 10060))

    def test_61(self):
        input = ["INSERT x string", "ASSIGN x 'a'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10061))

    def test_62(self):
        input = ["INSERT x string", "ASSIGN x '1'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10062))

    def test_63(self):
        input = ["INSERT x string", "ASSIGN x '1a'"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10063))

    def test_64(self):
        input = ["INSERT x string", "ASSIGN x 'a__a'"]
        expected = ["Invalid: ASSIGN x 'a__a'"]
        self.assertTrue(TestUtils.check(input, expected, 10064))

    def test_65(self):
        input = ["INSERT x string", "ASSIGN x 'a a'"]
        expected = ["Invalid: ASSIGN x 'a a'"]
        self.assertTrue(TestUtils.check(input, expected, 10065))

    def test_66(self):
        input = ["ASSIGN _ 1"]
        expected = ["Invalid: ASSIGN _ 1"]
        self.assertTrue(TestUtils.check(input, expected, 10066))

    def test_67(self):
        input = ["ASSIGN _x 1"]
        expected = ["Invalid: ASSIGN _x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10067))

    def test_68(self):
        input = ["ASSIGN bc@ed 1"]
        expected = ["Invalid: ASSIGN bc@ed 1"]
        self.assertTrue(TestUtils.check(input, expected, 10068))

    def test_69(self):
        input = ["INSERT x string", "ASSIGN x X"]
        expected = ["Invalid: ASSIGN x X"]
        self.assertTrue(TestUtils.check(input, expected, 10069))

    def test_70(self):
        input = ["INSERT x number", "ASSIGN x X"]
        expected = ["Invalid: ASSIGN x X"]
        self.assertTrue(TestUtils.check(input, expected, 10070))

    def test_71(self):
        input = ["INSERT x string", "ASSIGN x Xy"]
        expected = ["Invalid: ASSIGN x Xy"]
        self.assertTrue(TestUtils.check(input, expected, 10071))

    def test_72(self):
        input = ["INSERT x number", "ASSIGN x Xy"]
        expected = ["Invalid: ASSIGN x Xy"]
        self.assertTrue(TestUtils.check(input, expected, 10072))

    def test_73(self):
        input = ["INSERT x string", "ASSIGN x X2"]
        expected = ["Invalid: ASSIGN x X2"]
        self.assertTrue(TestUtils.check(input, expected, 10073))

    def test_74(self):
        input = ["INSERT x number", "ASSIGN x X2"]
        expected = ["Invalid: ASSIGN x X2"]
        self.assertTrue(TestUtils.check(input, expected, 10074))

    def test_75(self):
        input = ["INSERT x string", "ASSIGN x _"]
        expected = ["Invalid: ASSIGN x _"]
        self.assertTrue(TestUtils.check(input, expected, 10075))

    def test_76(self):
        input = ["INSERT x number", "ASSIGN x _"]
        expected = ["Invalid: ASSIGN x _"]
        self.assertTrue(TestUtils.check(input, expected, 10076))

    def test_77(self):
        input = ["INSERT x string", "ASSIGN x _x"]
        expected = ["Invalid: ASSIGN x _x"]
        self.assertTrue(TestUtils.check(input, expected, 10077))

    def test_78(self):
        input = ["INSERT x number", "ASSIGN x _x"]
        expected = ["Invalid: ASSIGN x _x"]
        self.assertTrue(TestUtils.check(input, expected, 10078))

    def test_79(self):
        input = ["INSERT x string", "ASSIGN x 3e"]
        expected = ["Invalid: ASSIGN x 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10079))

    def test_80(self):
        input = ["INSERT x number", "ASSIGN x 3e"]
        expected = ["Invalid: ASSIGN x 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10080))

    def test_81(self):
        input = ["INSERT x number", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10081))

    def test_82(self):
        input = ["INSERT x string", "ASSIGN x bc@ed"]
        expected = ["Invalid: ASSIGN x bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10082))

    def test_83(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10083))

    def test_84(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN x y"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10084))

    def test_85(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10085))

    def test_86(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10086))

    def test_87(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN y number"]
        expected = ["Undeclared: ASSIGN y number"]
        self.assertTrue(TestUtils.check(input, expected, 10087))

    def test_88(self):
        input = ["INSERT x number", "INSERT y number", "ASSIGN y string"]
        expected = ["Undeclared: ASSIGN y string"]
        self.assertTrue(TestUtils.check(input, expected, 10088))

    def test_89(self):
        input = ["INSERT x string", "INSERT y number", "ASSIGN x y"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10089))

    def test_90(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x y"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10090))

    def test_91(self):
        input = ["INSERT x string", "INSERT y number", "ASSIGN y x"]
        expected = ["TypeMismatch: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10091))

    def test_92(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN y x"]
        expected = ["TypeMismatch: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10092))

    def test_93(self):
        input = ["ASSIGN string 1"]
        expected = ["Undeclared: ASSIGN string 1"]
        self.assertTrue(TestUtils.check(input, expected, 10093))

    def test_94(self):
        input = ["INSERT x string", "ASSIGN x a"]
        expected = ["Undeclared: ASSIGN x a"]
        self.assertTrue(TestUtils.check(input, expected, 10094))

    def test_95(self):
        input = ["INSERT x number", "ASSIGN x a2"]
        expected = ["Undeclared: ASSIGN x a2"]
        self.assertTrue(TestUtils.check(input, expected, 10095))

    def test_96(self):
        input = ["INSERT x string", "ASSIGN x a2"]
        expected = ["Undeclared: ASSIGN x a2"]
        self.assertTrue(TestUtils.check(input, expected, 10096))

    def test_97(self):
        input = ["INSERT x number", "ASSIGN x aA2"]
        expected = ["Undeclared: ASSIGN x aA2"]
        self.assertTrue(TestUtils.check(input, expected, 10097))

    def test_98(self):
        input = ["INSERT x string", "ASSIGN x aA2"]
        expected = ["Undeclared: ASSIGN x aA2"]
        self.assertTrue(TestUtils.check(input, expected, 10098))

    def test_99(self):
        input = ["INSERT x string", "ASSIGN x string"]
        expected = ["Undeclared: ASSIGN x string"]
        self.assertTrue(TestUtils.check(input, expected, 10099))

    def test_100(self):
        input = ["INSERT x number", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10100))

    def test_101(self):
        input = ["INSERT x string", "ASSIGN x number"]
        expected = ["Undeclared: ASSIGN x number"]
        self.assertTrue(TestUtils.check(input, expected, 10101))

    def test_102(self):
        input = ["INSERT x string", "ASSIGN x 1"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10102))

    def test_103(self):
        input = ["INSERT x string", "INSERT y string", " ASSIGN x y"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10103))

    def test_104(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN  x y"]
        expected = ["Invalid: ASSIGN  x y"]
        self.assertTrue(TestUtils.check(input, expected, 10104))

    def test_105(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x  y"]
        expected = ["Invalid: ASSIGN x  y"]
        self.assertTrue(TestUtils.check(input, expected, 10105))

    def test_106(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x y "]
        expected = ["Invalid: ASSIGN x y "]
        self.assertTrue(TestUtils.check(input, expected, 10106))

    def test_107(self):
        input = ["INSERT x string", "INSERT y string", " ASSIGN x 'y'"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10107))

    def test_108(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN  x 'y'"]
        expected = ["Invalid: ASSIGN  x 'y'"]
        self.assertTrue(TestUtils.check(input, expected, 10108))

    def test_109(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x  'y'"]
        expected = ["Invalid: ASSIGN x  'y'"]
        self.assertTrue(TestUtils.check(input, expected, 10109))

    def test_110(self):
        input = ["INSERT x string", "INSERT y string", "ASSIGN x 'y' "]
        expected = ["Invalid: ASSIGN x 'y' "]
        self.assertTrue(TestUtils.check(input, expected, 10110))

    def test_111(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  x 1"]
        expected = ["Invalid: ASSIGN  x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10111))

    def test_112(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x  1"]
        expected = ["Invalid: ASSIGN x  1"]
        self.assertTrue(TestUtils.check(input, expected, 10112))

    def test_113(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x 1 "]
        expected = ["Invalid: ASSIGN x 1 "]
        self.assertTrue(TestUtils.check(input, expected, 10113))

    def test_114(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x"]
        expected = ["Invalid: ASSIGN x"]
        self.assertTrue(TestUtils.check(input, expected, 10114))

    def test_115(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN x "]
        expected = ["Invalid: ASSIGN x "]
        self.assertTrue(TestUtils.check(input, expected, 10115))

    def test_116(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  x"]
        expected = ["Invalid: ASSIGN  x"]
        self.assertTrue(TestUtils.check(input, expected, 10116))

    def test_117(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN  "]
        expected = ["Invalid: ASSIGN  "]
        self.assertTrue(TestUtils.check(input, expected, 10117))

    def test_118(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN "]
        expected = ["Invalid: ASSIGN "]
        self.assertTrue(TestUtils.check(input, expected, 10118))

    def test_119(self):
        input = ["INSERT x number", "INSERT y string", "ASSIGN"]
        expected = ["Invalid: ASSIGN"]
        self.assertTrue(TestUtils.check(input, expected, 10119))
    # BEGIN END ----------------------------------------------------------------------------------------------------------------
    def test_120(self):
        input = ["BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10120))

    def test_121(self):
        input = ["BEGIN ", "END"]
        expected = ["Invalid: BEGIN "]
        self.assertTrue(TestUtils.check(input, expected, 10121))

    def test_122(self):
        input = [" BEGIN", "END"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10122))

    def test_123(self):
        input = ["INSERT x number", "BEGIN x", "END"]
        expected = ["Invalid: BEGIN x"]
        self.assertTrue(TestUtils.check(input, expected, 10123))

    def test_124(self):
        input = ["BEGIN", "END "]
        expected = ["Invalid: END "]
        self.assertTrue(TestUtils.check(input, expected, 10124))

    def test_125(self):
        input = ["BEGIN", " END"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10125))

    def test_126(self):
        input = ["BEGIN", "END  "]
        expected = ["Invalid: END  "]
        self.assertTrue(TestUtils.check(input, expected, 10126))

    def test_127(self):
        input = ["INSERT x number", "BEGIN", "END x"]
        expected = ["Invalid: END x"]
        self.assertTrue(TestUtils.check(input, expected, 10127))

    def test_128(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10128))

    def test_129(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10129))

    def test_130(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x 1", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10130))

    def test_131(self):
        input = ["INSERT x string", "BEGIN", "INSERT x number", "ASSIGN x 1", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10131))

    def test_132(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "ASSIGN x 1", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10132))

    def test_133(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "ASSIGN x 1", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10133))

    def test_134(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x '1'", "END"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10134))

    def test_135(self):
        input = ["INSERT x string", "BEGIN", "INSERT x number", "ASSIGN x '1'", "END"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10135))

    def test_136(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "ASSIGN x '1'", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10136))

    def test_137(self):
        input = ["INSERT x string", "BEGIN", "INSERT x string", "ASSIGN x '1'", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10137))

    def test_138(self):
        input = ["BEGIN", "BEGIN", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10138))

    def test_139(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10139))

    def test_140(self):
        input = ["BEGIN", "BEGIN", "END", "END", "BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10140))

    def test_141(self):
        input = ["BEGIN", "BEGIN", "END", "BEGIN", "END", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10141))

    def test_142(self):
        input = ["BEGIN", "BEGIN", "END", "BEGIN", "END", "END", "BEGIN", "END"]
        expected = []
        self.assertTrue(TestUtils.check(input, expected, 10142))

    def test_143(self):
        input = ["BEGIN", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10143))

    def test_144(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10144))

    def test_145(self):
        input = ["BEGIN", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10145))

    def test_146(self):
        input = ["BEGIN", "BEGIN", "END", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10146))

    def test_147(self):
        input = ["INSERT x number",
"INSERT y string",
"BEGIN",
"INSERT z number",
"ASSIGN z x",
"INSERT x string",
"ASSIGN x z",
"END"]
        expected = ["TypeMismatch: ASSIGN x z"]
        self.assertTrue(TestUtils.check(input, expected, 10147))

    def test_148(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END"]
        expected = ["success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10148))

    def test_149(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10149))

    def test_150(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10150))

    def test_151(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10151))

    def test_152(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10152))

    def test_153(self):
        input = ["BEGIN", "INSERT x number", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10153))

    def test_154(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10154))

    def test_155(self):
        input = ["BEGIN", "INSERT x number", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10155))

    def test_156(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "END", "END", "END", "BEGIN"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10156))

    def test_157(self):
        input = ["INSERT x number", "END"]
        expected = ["UnknownBlock"]
        self.assertTrue(TestUtils.check(input, expected, 10157))

    def test_158(self):
        input = ["BEGIN"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10158))

    def test_159(self):
        input = ["BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10159))

    def test_160(self):
        input = ["BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10160))

    def test_161(self):
        input = ["BEGIN", "BEGIN", "BEGIN"]
        expected = ["UnclosedBlock: 3"]
        self.assertTrue(TestUtils.check(input, expected, 10161))

    def test_162(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10162))

    def test_163(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10163))

    def test_164(self):
        input = ["BEGIN", "BEGIN", "BEGIN", "END", "BEGIN", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10164))

    def test_165(self):
        input = ["BEGIN", "BEGIN", "END", "END", "BEGIN", "BEGIN", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10165))

    def test_166(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10166))

    def test_167(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10167))

    def test_168(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10168))

    def test_169(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END"]
        expected = ["UnclosedBlock: 1"]
        self.assertTrue(TestUtils.check(input, expected, 10169))

    def test_170(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END"]
        expected = ["UnclosedBlock: 2"]
        self.assertTrue(TestUtils.check(input, expected, 10170))

    def test_171(self):
        input = ["INSERT x number", "BEGIN", "BEGIN", "INSERT x number", "END", "INSERT x number", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10171))

    def test_172(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "INSERT x number", "END"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10172))

    def test_173(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10173))

    def test_174(self):
        input = ["INSERT x number", "INSERT y string", "BEGIN", "INSERT x number", "INSERT y string", "END", "BEGIN", "INSERT x number", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10174))

    def test_175(self):
        input = ["BEGIN", "INSERT x number", "END", "INSERT x number", "BEGIN", "INSERT x number", "END", "INSERT x number"]
        expected = ["Redeclared: INSERT x number"]
        self.assertTrue(TestUtils.check(input, expected, 10175))

    def test_176(self):
        input = ["BEGIN", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10176))

    def test_177(self):
        input = ["INSERT x number", "BEGIN", "INSERT y number", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10177))

    def test_178(self):
        input = ["INSERT x string", "BEGIN", "INSERT y number", "BEGIN", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10178))

    def test_179(self):
        input = ["INSERT x string", "BEGIN", "INSERT y number", "BEGIN", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10179))

    def test_180(self):
        input = ["INSERT x number", "BEGIN", "INSERT y string", "BEGIN", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["TypeMismatch: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10180))

    def test_181(self):
        input = ["INSERT x number", "BEGIN", "INSERT y number", "BEGIN", "INSERT z string", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10181))

    def test_182(self):
        input = ["INSERT x number", "BEGIN", "INSERT x string", "INSERT y number", "BEGIN", "INSERT y string", "INSERT z number", "ASSIGN x y", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10182))

    def test_183(self):
        input = ["BEGIN", "INSERT x string", "INSERT y number", "BEGIN", "END", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10183))

    def test_184(self):
        input = ["BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "ASSIGN y x", "END"]
        expected = ["Undeclared: ASSIGN y x"]
        self.assertTrue(TestUtils.check(input, expected, 10184))

    def test_185(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "ASSIGN y x", "END"]
        expected = ["success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10185))

    def test_186(self):
        input = ["BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["Undeclared: ASSIGN x y"]
        self.assertTrue(TestUtils.check(input, expected, 10186))

    def test_187(self):
        input = ["INSERT x number", "INSERT y number", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN x y", "END", "BEGIN", "INSERT x number", "INSERT y number", "ASSIGN y x", "END", "ASSIGN x y"]
        expected = ["success", "success", "success", "success", "success", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10187))

    def test_188(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10188))

    def test_189(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10189))

    def test_190(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10190))

    def test_191(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10191))

    def test_192(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10192))

    def test_193(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10193))

    def test_194(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10194))

    def test_195(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "END", "END", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "ASSIGN x '1'"]
        expected = ["TypeMismatch: ASSIGN x '1'"]
        self.assertTrue(TestUtils.check(input, expected, 10195))

    def test_196(self):
        input = ["BEGIN", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10196))

    def test_197(self):
        input = ["BEGIN", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10197))

    def test_198(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["TypeMismatch: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10198))

    def test_199(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "ASSIGN y 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["TypeMismatch: ASSIGN y 1"]
        self.assertTrue(TestUtils.check(input, expected, 10199))

    def test_200(self):
        input = ["BEGIN", "INSERT y number", "ASSIGN x 1", "INSERT x number", "INSERT y number", "END"]
        expected = ["Undeclared: ASSIGN x 1"]
        self.assertTrue(TestUtils.check(input, expected, 10200))
    #  LOOKUP ----------------------------------------------------------------------------------------------------------------
    def test_201(self):
        input = ["LOOKUP X"]
        expected = ["Invalid: LOOKUP X"]
        self.assertTrue(TestUtils.check(input, expected, 10201))

    def test_202(self):
        input = ["LOOKUP Xa"]
        expected = ["Invalid: LOOKUP Xa"]
        self.assertTrue(TestUtils.check(input, expected, 10202))

    def test_203(self):
        input = ["LOOKUP X1"]
        expected = ["Invalid: LOOKUP X1"]
        self.assertTrue(TestUtils.check(input, expected, 10203))

    def test_204(self):
        input = ["LOOKUP _"]
        expected = ["Invalid: LOOKUP _"]
        self.assertTrue(TestUtils.check(input, expected, 10204))

    def test_205(self):
        input = ["LOOKUP _x"]
        expected = ["Invalid: LOOKUP _x"]
        self.assertTrue(TestUtils.check(input, expected, 10205))

    def test_206(self):
        input = ["LOOKUP 3e"]
        expected = ["Invalid: LOOKUP 3e"]
        self.assertTrue(TestUtils.check(input, expected, 10206))

    def test_207(self):
        input = ["LOOKUP bc@ed"]
        expected = ["Invalid: LOOKUP bc@ed"]
        self.assertTrue(TestUtils.check(input, expected, 10207))

    def test_208(self):
        input = ["LOOKUP a"]
        expected = ["Undeclared: LOOKUP a"]
        self.assertTrue(TestUtils.check(input, expected, 10208))

    def test_209(self):
        input = ["LOOKUP b2"]
        expected = ["Undeclared: LOOKUP b2"]
        self.assertTrue(TestUtils.check(input, expected, 10209))

    def test_210(self):
        input = ["LOOKUP string"]
        expected = ["Undeclared: LOOKUP string"]
        self.assertTrue(TestUtils.check(input, expected, 10210))

    def test_211(self):
        input = ["LOOKUP number"]
        expected = ["Undeclared: LOOKUP number"]
        self.assertTrue(TestUtils.check(input, expected, 10211))

    def test_212(self):
        input = ["LOOKUP x "]
        expected = ["Invalid: LOOKUP x "]
        self.assertTrue(TestUtils.check(input, expected, 10212))

    def test_213(self):
        input = ["LOOKUP "]
        expected = ["Invalid: LOOKUP "]
        self.assertTrue(TestUtils.check(input, expected, 10213))

    def test_214(self):
        input = ["LOOKUP"]
        expected = ["Invalid: LOOKUP"]
        self.assertTrue(TestUtils.check(input, expected, 10214))

    def test_215(self):
        input = [" LOOKUP x"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10215))

    def test_216(self):
        input = ["INSERT x number", "LOOKUP x x"]
        expected = ["Invalid: LOOKUP x x"]
        self.assertTrue(TestUtils.check(input, expected, 10216))

    def test_217(self):
        input = ["LOOKUP  x"]
        expected = ["Invalid: LOOKUP  x"]
        self.assertTrue(TestUtils.check(input, expected, 10217))

    def test_218(self):
        input = ["INSERT x number", "LOOKUP x"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10218))

    def test_219(self):
        input = ["INSERT x number", "INSERT y number", "LOOKUP x"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10219))

    def test_220(self):
        input = ["INSERT x string", "INSERT y number", "LOOKUP x"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10220))

    def test_221(self):
        input = ["INSERT y number", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10221))

    def test_222(self):
        input = ["INSERT x number", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10222))

    def test_223(self):
        input = ["BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10223))

    def test_224(self):
        input = ["BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10224))

    def test_225(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10225))

    def test_226(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "2"]
        self.assertTrue(TestUtils.check(input, expected, 10226))

    def test_227(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10227))

    def test_228(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10228))

    def test_229(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10229))

    def test_230(self):
        input = ["BEGIN", "BEGIN", "INSERT x number", "END", "LOOKUP x", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10230))

    def test_231(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "INSERT x number", "END", "END", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10231))

    def test_232(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "2"]
        self.assertTrue(TestUtils.check(input, expected, 10232))

    def test_233(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10233))

    def test_234(self):
        input = ["INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "LOOKUP x", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10234))

    def test_235(self):
        input = ["BEGIN", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "LOOKUP x", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10235))

    def test_236(self):
        input = ["BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "BEGIN", "INSERT y number", "INSERT x string", "INSERT z number", "END", "END", "LOOKUP x"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10236))

    def test_237(self):
        input = ["BEGIN", "LOOKUP x", "INSERT x number", "END"]
        expected = ["Undeclared: LOOKUP x"]
        self.assertTrue(TestUtils.check(input, expected, 10237))

    def test_238(self):
        input = ["BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "INSERT x number", "END", "END"]
        expected = ["success", "1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10238))

    def test_239(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "BEGIN", "LOOKUP x", "INSERT x number", "END", "END"]
        expected = ["success", "success", "1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10239))

    def test_240(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "LOOKUP x", "END"]
        expected = ["success", "success", "success", "1"]
        self.assertTrue(TestUtils.check(input, expected, 10240))

    def test_241(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "LOOKUP x", "END"]
        expected = ["success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10241))

    def test_242(self):
        input = ["INSERT x number", "BEGIN", "INSERT x number", "END", "BEGIN", "INSERT x number", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10242))

    def test_243(self):
        input = ["BEGIN", "INSERT x number", "END", "INSERT x number", "BEGIN", "INSERT x number", "END", "LOOKUP x"]
        expected = ["success", "success", "success", "0"]
        self.assertTrue(TestUtils.check(input, expected, 10243))
    # Print ----------------------------------------------------------------------------------------------------------------
    def test_244(self):
        input = ["PRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10244))

    def test_245(self):
        input = ["PRINT "]
        expected = ["Invalid: PRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10245))

    def test_246(self):
        input = [" PRINT"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10246))

    def test_247(self):
        input = ["PRINT number"]
        expected = ["Invalid: PRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10247))

    def test_248(self):
        input = ["INSERT x string", "PRINT x"]
        expected = ["Invalid: PRINT x"]
        self.assertTrue(TestUtils.check(input, expected, 10248))

    def test_249(self):
        input = ["INSERT x number", "INSERT y string", "PRINT"]
        expected = ["success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10249))

    def test_250(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", ""]
        self.assertTrue(TestUtils.check(input, expected, 10250))

    def test_251(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10251))

    def test_252(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10252))

    def test_253(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10253))

    def test_254(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "PRINT", "END"]
        expected = ["success", "success", "success", "y//0 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10254))

    def test_255(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10255))

    def test_256(self):
        input = ["PRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10256))

    def test_257(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "PRINT", "END", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "x//2 y//2", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10257))

    def test_258(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "PRINT", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//1"]
        self.assertTrue(TestUtils.check(input, expected, 10258))

    def test_259(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10259))

    def test_260(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10260))

    def test_261(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "PRINT", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "x//0 y//0", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10261))

    def test_262(self):
        input = ["INSERT x string", "INSERT y string", "INSERT z string", "PRINT"]
        expected = ["success", "success", "success", "x//0 y//0 z//0"]
        self.assertTrue(TestUtils.check(input, expected, 10262))

    def test_263(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "y//0 x//1 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10263))

    def test_264(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "PRINT", "INSERT z string", "END", "END"]
        expected = ["success", "success", "success", "success", "z//0 y//0 x//1", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10264))

    def test_265(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "PRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "x//1 y//2 z//2"]
        self.assertTrue(TestUtils.check(input, expected, 10265))
    def test_266(self):
        input = ["PRINT", "PRINT"]
        expected = ["", ""]
        self.assertTrue(TestUtils.check(input, expected, 10266))
    def test_267(self):
        input = ["INSERT x number", "INSERT y string", "PRINT", "PRINT"]
        expected = ["success", "success", "x//0 y//0", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10249))
    # RPRINT ---------------------------------------------------------------------------------------------------------------- 
    def test_268(self):
        input = ["RPRINT"]
        expected = [""]
        self.assertTrue(TestUtils.check(input, expected, 10268))

    def test_269(self):
        input = ["RPRINT "]
        expected = ["Invalid: RPRINT "]
        self.assertTrue(TestUtils.check(input, expected, 10269))

    def test_270(self):
        input = [" RPRINT"]
        expected = ["Invalid: Invalid command"]
        self.assertTrue(TestUtils.check(input, expected, 10270))

    def test_271(self):
        input = ["RPRINT  "]
        expected = ["Invalid: RPRINT  "]
        self.assertTrue(TestUtils.check(input, expected, 10271))

    def test_272(self):
        input = ["RPRINT number"]
        expected = ["Invalid: RPRINT number"]
        self.assertTrue(TestUtils.check(input, expected, 10272))

    def test_273(self):
        input = ["INSERT x number", "RPRINT x"]
        expected = ["Invalid: RPRINT x"]
        self.assertTrue(TestUtils.check(input, expected, 10273))

    def test_274(self):
        input = ["INSERT x number", "INSERT y number", "RPRINT"]
        expected = ["success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10274))

    def test_275(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", ""]
        self.assertTrue(TestUtils.check(input, expected, 10275))

    def test_276(self):
        input = ["BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10276))

    def test_277(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10277))

    def test_278(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10278))

    def test_279(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "RPRINT", "END"]
        expected = ["success", "success", "success", "x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10279))

    def test_280(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10280))

    def test_281(self):
        input = ["RPRINT", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["", "success", "success", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10281))

    def test_282(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "RPRINT", "END", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "y//2 x//2", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10282))

    def test_283(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "y//1 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10283))

    def test_284(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10284))

    def test_285(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10285))

    def test_286(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT", "BEGIN", "INSERT x string", "INSERT y string", "END"]
        expected = ["success", "success", "success", "success", "y//0 x//0", "success", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10286))

    def test_287(self):
        input = ["INSERT y string", "BEGIN", "INSERT x string", "INSERT y string", "END", "INSERT x string", "BEGIN", "INSERT x string", "INSERT y string", "END", "RPRINT"]
        expected = ["success", "success", "success", "success", "success", "success", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10287))

    def test_288(self):
        input = ["INSERT x string", "INSERT y string", "INSERT z string", "RPRINT"]
        expected = ["success", "success", "success", "z//0 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10288))

    def test_289(self):
        input = ["INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "RPRINT", "END"]
        expected = ["success", "success", "success", "z//1 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10289))

    def test_290(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT z string", "RPRINT", "END"]
        expected = ["success", "success", "success", "success", "z//1 y//0 x//0"]
        self.assertTrue(TestUtils.check(input, expected, 10290))

    def test_291(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT z string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "z//2 x//1 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10291))

    def test_292(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "RPRINT", "INSERT z string", "END", "END"]
        expected = ["success", "success", "success", "success", "x//1 y//0 z//0", "success"]
        self.assertTrue(TestUtils.check(input, expected, 10292))

    def test_293(self):
        input = ["INSERT z string", "INSERT x string", "INSERT y string", "BEGIN", "INSERT x string", "BEGIN", "INSERT y string", "INSERT z string", "RPRINT", "END", "END"]
        expected = ["success", "success", "success", "success", "success", "success", "z//2 y//2 x//1"]
        self.assertTrue(TestUtils.check(input, expected, 10293))
    def test_294(self):
        input = ["PRINT", "RPRINT"]
        expected = ["", ""]
        self.assertTrue(TestUtils.check(input, expected, 10266))
    def test_295(self):
        input = ["INSERT x number", "INSERT y string", "RPRINT", "PRINT"]
        expected = ["success", "success", "y//0 x//0", "x//0 y//0"]
        self.assertTrue(TestUtils.check(input, expected, 10249))
    # ---------------------------------------------------- END TESTING ----------------------------------------------------

