# Class to hanle shipping cost calculation
class ShippingCostCalculator:
    # base rates for different weight ranges
    BASE_RATES = {
        (0, 2): 1.5,
        (2, 5): 2.5,
        (5, 10): 3.5,
        (10, float('inf')): 5
    }

    # constants for extra cost calculation
    EXTRA_COST_DISTANCE = 500
    EXTRA_COST = 50

    def __init__(self, weight, distance):
        self.weight = weight
        self.distance = distance

    def calculate_cost(self) -> float:
        # get the base rate for the given weight
        base_rate = self._get_rate_for_weight(self.weight)
        cost = self.distance * base_rate

        # add extra cost if distance is greater than EXTRA_COST_DISTANCE
        if self.distance > self.EXTRA_COST_DISTANCE:
            cost += self.EXTRA_COST

        return cost
    
    def _get_rate_for_weight(self, weight):
        # get the base rate for the given weight
        for weight_range, base_rate in self.BASE_RATES.items():
            if weight_range[0] <= weight < weight_range[1]:
                return base_rate
        else:
            raise ValueError('Invalid weight')
        

def calculate_shipping_cost():
    # Get input for package weight and distance
    weight = float(input('Enter package weight: '))
    distance = float(input('Enter distance: '))

    scc = ShippingCostCalculator(weight, distance)
    cost = scc.calculate_cost()

    print(f'The shipping cost is: {cost}')

if __name__ == '__main__':   
    calculate_shipping_cost()