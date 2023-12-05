class FancyFoodItem:
    def __init__(self, food, amount):
        self._food_name = food
        self._amount_in_pounds = amount
        self._standard_price_per_pound = self._get_standard_price()
        self._calculated_price = self._calculate_cost()

    def _get_standard_price(self):
        if self._food_name == 'Dry Cured Iberian Ham':
            return 177.80
        elif self._food_name == 'Wagyu Steaks':
            return 450.00
        elif self._food_name == 'Matsutake Mushrooms':
            return 272.00
        elif self._food_name == 'Kopi Luwak Coffee':
            return 306.50
        elif self._food_name == 'Moose Cheese':
            return 487.20
        elif self._food_name == 'White Truffles':
            return 3600.00
        elif self._food_name == 'Blue Fin Tuna':
            return 3603.00
        elif self._food_name == 'Le Bonnotte Potatoes':
            return 270.81
        else:
            return 0.00  

    def _calculate_cost(self):
        return self._amount_in_pounds * self._standard_price_per_pound

    def get_food_name(self):
        return self._food_name

    def get_amount_ordered(self):
        return self._amount_in_pounds

    def get_standard_price_per_pound(self):
        return self._standard_price_per_pound

    def get_calculated_price(self):
        return self._calculated_price

    def __str__(self):
        return f"Item: {self._food_name}\nAmount ordered: {self._amount_in_pounds:.1f} pounds\n" \
               f"Price per pound: ${self._standard_price_per_pound:.2f}\n" \
               f"Price of order: ${self._calculated_price:.2f}"
