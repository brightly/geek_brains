class Division_By_Null:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def corrently_division(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = Division_By_Null(300, 50)
print(Division_By_Null.corrently_division(14, 0))
print(Division_By_Null.corrently_division(78, 0.5))
print(div.corrently_division(456, 0))