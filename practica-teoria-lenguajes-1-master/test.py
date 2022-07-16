from operaciones import derivar
import unittest

class TestDerivar(unittest.TestCase):
    
    def test_1(self):
        resultado = derivar('a', 'a')
        self.assertEqual(resultado, 'ε')

    def test_2(self):
        resultado = derivar('b', 'a')
        self.assertEqual(resultado, '∅')

    def test_3(self):
        resultado = derivar('(a)', 'a')
        self.assertEqual(resultado, '(ε)')

    def test_4(self):
        resultado = derivar('(b)', 'a')
        self.assertEqual(resultado, '(∅)')

    def test_5(self):
        resultado = derivar('ε', 'a')
        self.assertEqual(resultado, '∅')

    def test_6(self):
        resultado = derivar('(ε)', 'a')
        self.assertEqual(resultado, '(∅)')

    def test_7(self):
        resultado = derivar('∅', 'a')
        self.assertEqual(resultado, '∅')

    def test_8(self):
        resultado = derivar('(∅)', 'a')
        self.assertEqual(resultado, '(∅)')

    def test_9(self):
        resultado = derivar('a*', 'a')
        self.assertEqual(resultado, 'a*')

    def test_10(self):
        resultado = derivar('(a*)', 'a')
        self.assertEqual(resultado, '(a*)')

    def test_11(self):
        resultado = derivar('(a)*', 'a') 
        self.assertEqual(resultado, '(a)*')

    def test_12(self):
        resultado = derivar('b*', 'a')
        self.assertEqual(resultado, '∅')

    def test_13(self):
        resultado = derivar('(b*)', 'a')
        self.assertEqual(resultado, '(∅)')

    def test_14(self):
        resultado = derivar('(b)*', 'a')
        self.assertEqual(resultado, '(∅)')

    def test_15(self):
        resultado = derivar('(ab)*', 'a')
        self.assertEqual(resultado, 'b((ab)*)')
        
    def test_16(self):
        resultado = derivar('(ba)*', 'a')
        self.assertEqual(resultado, '∅')

    def test_17(self):
        resultado = derivar('(a+b)*', 'a')
        self.assertEqual(resultado, '(a+b)*')

    def test_18(self):
        resultado = derivar('(b+a)*', 'a')
        self.assertEqual(resultado, '(b+a)*')

    def test_19(self):
        resultado = derivar('(ab+c)*', 'a')
        self.assertEqual(resultado, '(b)((ab+c)*)')

    def test_20(self):
        resultado = derivar('(b+ac)*', 'a')
        self.assertEqual(resultado, '(c)((b+ac)*)')

    def test_21(self):
        resultado = derivar('ab*', 'a') 
        self.assertEqual(resultado, 'b(ab*)')

    def test_22(self):
        resultado = derivar('(ab*)', 'a') 
        self.assertEqual(resultado, 'b(ab*)')

    def test_23(self):
        resultado = derivar('a*b', 'a') 
        self.assertEqual(resultado, 'a*b')

    def test_24(self):
        resultado = derivar('b*a', 'a') 
        self.assertEqual(resultado, '∅')

    def test_25(self):
        resultado = derivar('a+b', 'a') 
        self.assertEqual(resultado, 'ε')

    def test_26(self):
        resultado = derivar('b+a', 'a') 
        self.assertEqual(resultado, 'ε')

    def test_27(self):
        resultado = derivar('ab+cd', 'a') 
        self.assertEqual(resultado, 'b')

    def test_28(self):
        resultado = derivar('ba+aab', 'a') 
        self.assertEqual(resultado, 'ab')

    def test_29(self):
        resultado = derivar('(a+b)', 'a') 
        self.assertEqual(resultado, '(ε)')

    def test_30(self):
        resultado = derivar('(b+a)', 'a') 
        self.assertEqual(resultado, '(ε)')

    def test_31(self):
        resultado = derivar('(ab+c)', 'a') 
        self.assertEqual(resultado, '(b)')

    def test_32(self):
        resultado = derivar('(ab+acd)', 'a') 
        self.assertEqual(resultado, '(b+cd)')

    def test_33(self):
        resultado = derivar('(bcd+aef)', 'a') 
        self.assertEqual(resultado, '(ef)')

    def test_34(self):
        resultado = derivar('a*+b', 'a') 
        self.assertEqual(resultado, 'a*')

    def test_35(self):
        resultado = derivar('b*+a', 'a') 
        self.assertEqual(resultado, 'ε')

    def test_36(self):
        resultado = derivar('a+b*', 'a') 
        self.assertEqual(resultado, 'ε')

    def test_37(self):
        resultado = derivar('b+a*', 'a') 
        self.assertEqual(resultado, 'a*')

    def test_38(self):
        resultado = derivar('ab*+c', 'a') 
        self.assertEqual(resultado, 'b(ab*)')

    def test_39(self):
        resultado = derivar('b*+c', 'a') 
        self.assertEqual(resultado, '∅')

    def test_40(self):
        resultado = derivar('bc*+acd*', 'a') 
        self.assertEqual(resultado, 'cd(acd*)')
       
    def test_41(self):
        resultado = derivar('a(b)', 'a') 
        self.assertEqual(resultado, '(b)')

    def test_42(self):
        resultado = derivar('b(a)', 'a') 
        self.assertEqual(resultado, '∅')

    def test_43(self):
        resultado = derivar('a(b+c)', 'a') 
        self.assertEqual(resultado, '(b+c)')

    def test_44(self):
        resultado = derivar('a(a+b)', 'a') 
        self.assertEqual(resultado, '(a+b)')

    def test_45(self):
        resultado = derivar('a(ab+c)', 'a') 
        self.assertEqual(resultado, '(ab+c)+(b)')

    def test_46(self):
        resultado = derivar('a(b+ac)', 'a') 
        self.assertEqual(resultado, '(b+ac)+(c)')

    def test_47(self):
        resultado = derivar('a(ab*)', 'a') 
        self.assertEqual(resultado, '(ab*)+(b(ab*))')

    def test_48(self):
        resultado = derivar('a(ab*+ac)', 'a') 
        self.assertEqual(resultado, '(ab*+ac)+(b(ab*)+c)')

    def test_49(self):
        resultado = derivar('(a)b', 'a') 
        self.assertEqual(resultado, 'b')

    def test_50(self):
        resultado = derivar('(a+b)b', 'a') 
        self.assertEqual(resultado, 'b')

    def test_51(self):
        resultado = derivar('(ab*)b', 'a') 
        self.assertEqual(resultado, '(b(ab*))b')





if __name__ == '__main__':
    unittest.main()
