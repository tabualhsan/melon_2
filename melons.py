"""Classes for melon orders."""
class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""

    def __init__(self, name):
        self.name = name

    def get_total(self, price):
        self.price = price * 1.5


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    def __init__(self, species, qty):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.shipped = False
        self.order_type = "domestic"
        self.tax = 0.08

    def get_total(self,tax):
        """Calculate price, including tax."""

        base_price = 5
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has be en shipped."""

        self.shipped = True

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.species = species
        self.qty = qty
        self.country_code = country_code
        self.shipped = False
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        # if needed, try a for loop
        
        if self.qty >= 10:
            base_price = 5
            flat_fee = 3 
            total = (1 + self.tax) * self.qty * base_price + flat_fee
        else:
            base_price = 5
            total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self, shipped):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self, country_code):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):

    def __init__(self):
        self.passed_inspection = False

    def marked_inspection(self, passed):    
        if passed:
            self.passed_inspection = True 
            print("It has passed inspection!")
    
        return self.passed_inspection


christmas_melons = InternationalMelonOrder("Christmas Melon", 10, "AUS")
watermelon = GovernmentMelonOrder()
