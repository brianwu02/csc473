import unittest
import tutnese
import string
import random

class TestCase(unittest.TestCase):
	def setUp(self):
		pass
	def tearDown(self):
		pass
	
	def generate_string(self, size=100, chars=string.ascii_uppercase + string.digits):
		return ''.join(random.choice(chars) for x in range(size))

	def test_rand_gen_encode_decode(self):
		"""
		This test generates a random string and then tests
		that the encoded string returns the same value.
		"""
		string = self.generate_string()
		encoded_str = tutnese.encode(string) 
		decoded_str = tutnese.decode(encoded_str)
		string = tutnese.decode(encoded_str)
		self.assertEqual(decoded_str, string)
	
	def test_buncho_stuff(self):
		"""
		generates 100 strings of length 100 and puts them in a list
		for each string, encode, decode, and check if
		the decoded string is same as original string
		"""
		temp = list()
		for i in range(0,100):
			temp.append(self.generate_string())
		for element in temp:
			string = element
			encoded_str = tutnese.encode(string)
			decoded_str = tutnese.decode(encoded_str)
			string = tutnese.decode(encoded_str)
			self.assertEqual(decoded_str, string)
	
	def test_squa_1(self):
		"""
		test to check correct decode for edge case of
		bbbbb
		"""
		string = 'bbbbb'
		answer = 'squabsquabbub'
		encoded_str = tutnese.encode(string)
		self.assertEqual(answer, encoded_str)
	
	def test_squa_2(self):
		string = 'aaaaa'
		answer = 'aaaaa'
		encoded_str = tutnese.encode(string)
		self.assertEqual(answer, encoded_str)

	def test_encode_decode(self):
		string = "Over hill, over dale, Thorough bush,\
				thorough brier, Over park, over pale,\
				Thorough flood, thorough fire!".lower()
		string = "".join(string.split()) ## remove whitespace
		encoded_str = tutnese.encode(string)  ## encode the string & make lower
		## encode the string & rejoin ""
		encoded_str = "".join(tutnese.encode(string).split())
		decoded_str = tutnese.decode(encoded_str) ## decode the string again
		self.assertEqual(decoded_str, string)

	def test_decode_1(self):
		string_1 = "my name is brian"
		string_2 = "mumyub nunamume isus bubrurianun"
		string_1 = "".join(string_1.split())
		string_2 = "".join(string_2.split())
		result = tutnese.decode(string_2)
		self.assertEqual(result, string_1)
		
	def test_decode_2(self):
		string_1 = "Over hill, over dale, Thorough bush,\
				thorough brier, Over park, over pale,\
				Thorough flood, thorough fire!".lower()
		string_2 = "ovuverur hashisqual, ovuverur dudalule,\
				tuthashorurougughash bubusushash, \
				tuthashorurougughash bubrurierur, ovuverur puparurkuck,\
				ovuverur pupalule, tuthashorurougughash \
				fufluloodud, tuthashorurougughash fufirure!"
		string_1 = "".join(string_1.split())
		string_2 = "".join(string_2.split())
		result = tutnese.decode(string_2)
		self.assertEqual(result, string_1)

	def test_encode_1(self):
		string_1 = "Over hill, over dale, Thorough bush, thorough brier, \
				Over park, over pale, Thorough flood, thorough fire!"
		string_2 = "ovuverur hashisqual, ovuverur dudalule, tuthashorurougughash \
				bubusushash,	tuthashorurougughash bubrurierur, ovuverur puparurkuck, \
				ovuverur pupalule, tuthashorurougughash fufluloodud, \
				tuthashorurougughash fufirure!"
		string_1 = "".join(string_1.split())
		string_2 = "".join(string_2.split())
		result = tutnese.encode(string_1)
		self.assertEqual(result, string_2)
	
	def test_encode_2(self):
		string_1 = "my name is brian"
		string_2 = "mumyub nunamume isus bubrurianun"
		result = tutnese.encode(string_1)
		self.assertEqual(result, string_2)

	def test_decode_exception_1(self):
		string = "ovu|verur hashisqual, ovuverur dudalule, tuthashorurougughash bubusushash"
		self.assertRaises(Exception, tutnese.decode, string)

	def test_encode_exception_1(self):
		string = "my name| is brian"
		self.assertRaises(Exception, tutnese.encode, string)

	def test_encode_exception_2(self):
		string1 = "|"
		string2 = "abcdefghijklmopqrstuvwxyz|"
		string3 = " | "
		string4 = "Over hill, over dale, Thorough bush, thorough brier, \
				Over park, over pale, Thorough flo|od, thorough fire!"
		string5 = "Over hil|l, over dale, Thorough bush, thorough brier, \
				Over park, over pale, Thorough flood, thorough fire!"
		self.assertRaises(Exception, tutnese.encode,
				string1, string2, string3, string4, string5)

if __name__ == '__main__':
	unittest.main()
