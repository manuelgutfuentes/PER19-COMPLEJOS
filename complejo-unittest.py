#!/usr/bin/env python3

import unittest

class Complejo(object):
    def __init__(self, real, imag=0):
        self.real = real
        self.imag = imag

    def sumar(self, otro):
        result = Complejo(self.real + otro.real,
                            self.imag + otro.imag)
        return result

    def restar(self, otro):
        result = Complejo(self.real - otro.real,
                            self.imag - otro.imag)
        return result

    def multiplicar(self, otro):
        result = Complejo((self.real*otro.real-self.imag*otro.imag),(self.real*otro.imag+otro.real*self.imag))
        return result

    def dividir(self, otro):
        denom = ((otro.real*otro.real)+(otro.imag*otro.imag))
        dreal = ((self.real*otro.real+self.imag*otro.imag)/denom)
        dimag = ((((-self.real*otro.imag)+(self.imag*otro.real))/denom))
        result = Complejo(dreal, dimag)
        return result
    def igual(self, otro):
        return self.real == otro.real and self.imag == otro.imag 


class TestComplejo(unittest.TestCase):

    def test_sumar(self):

        c1 = Complejo(1,2)
        c2 = Complejo(3,4)

        suma = c1.sumar(c2)

        self.assertEqual(suma.real, 4)
        self.assertEqual(suma.imag, 6)

    def test_restar(self):

        c1 = Complejo(6,1)
        c2 = Complejo(8,4)

        restar = c1.restar(c2)

        self.assertEqual(restar.real, -2)
        self.assertEqual(restar.imag, -3)

    def test_multiplicar(self):
        c1 = Complejo(1,2)
        c2 = Complejo(3,4)
        multiplicar = c1.multiplicar(c2)
        self.assertEqual(multiplicar.real, -5)
        self.assertEqual(multiplicar.imag, 10)


    def test_dividir(self):
        c1 = Complejo(2,1)
        c2 = Complejo(4,4)
        dividir = c1.dividir(c2)
        self.assertEqual(dividir.real, 0.375)
        self.assertEqual(dividir.imag, (-1.0/8))


if __name__ == "__main__":
    unittest.main()
