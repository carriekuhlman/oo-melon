""""Classes for melon orders."""
import random

class AbstractMelonOrder():
    """A melon order."""

    def __init__(self, species, qty, country_code=None):
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True
    
    def get_base_price(self):
        """Select random number for base_price"""
        base_price = random.randrange(5, 10)

        return base_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        
        if self.species == 'Christmas melon':
            base_price *= 1.5
        
        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == 'international' and self.qty < 10:
            total += 3

        return total


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    tax = 0.08
    order_type = 'domestic'


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17
    order_type = 'international'

    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A government melon order."""

    tax = 0
    passed_inspection = False
    order_type = "government"

    def mark_inspection(self, passed):

        if passed == True: 
            self.passed_inspection = True



