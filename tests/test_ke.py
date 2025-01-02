from django.test import SimpleTestCase
from django.forms import ValidationError
from .forms import KEPostalCodeField, KEKRAPINField, KENationalIDNumberField, KEPassportNumberField

class KEPostalCodeFieldTest(SimpleTestCase):
    def test_valid_postal_code(self):
        field = KEPostalCodeField()
        valid_postal_codes = ["12345", "54321"]
        for postal_code in valid_postal_codes:
            self.assertEqual(field.clean(postal_code), "12345")

    def test_invalid_postal_code(self):
        field = KEPostalCodeField()
        invalid_postal_codes = ["1234", "ABCDE", "12 345", "12-345"]
        for postal_code in invalid_postal_codes:
            with self.assertRaises(ValidationError):
                field.clean(postal_code)

class KEKRAPINFieldTest(SimpleTestCase):
    def test_valid_kra_pin(self):
        field = KEKRAPINField()
        valid_pins = ["A123456789B", "P987654321C"]
        for pin in valid_pins:
            self.assertEqual(field.clean(pin), pin)

    def test_invalid_kra_pin(self):
        field = KEKRAPINField()
        invalid_pins = ["1234567890", "A123456789", "P987654321", "A12-3456789B"]
        for pin in invalid_pins:
            with self.assertRaises(ValidationError):
                field.clean(pin)

class KENationalIDNumberFieldTest(SimpleTestCase):
    def test_valid_national_id(self):
        field = KENationalIDNumberField()
        valid_ids = ["1234567", "12345678"]
        for id_number in valid_ids:
            self.assertEqual(field.clean(id_number), id_number)

    def test_invalid_national_id(self):
        field = KENationalIDNumberField()
        invalid_ids = ["12345", "12345A", "12-34567", "123456789"]
        for id_number in invalid_ids:
            with self.assertRaises(ValidationError):
                field.clean(id_number)

class KEPassportNumberFieldTest(SimpleTestCase):
    def test_valid_passport_number(self):
        field = KEPassportNumberField()
        valid_passports = ["A123456", "B1234567"]
        for passport in valid_passports:
            self.assertEqual(field.clean(passport), passport)

    def test_invalid_passport_number(self):
        field = KEPassportNumberField()
        invalid_passports = ["12345", "A1234567B", "AB-123456"]
        for passport in invalid_passports:
            with self.assertRaises(ValidationError):
                field.clean(passport)
