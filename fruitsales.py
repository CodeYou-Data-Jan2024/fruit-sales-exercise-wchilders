# add your code here
import pandas as pd
fruit_sales = {
    'Apples' : [35,41],
    'Bananas' : [21,34]
}

new_fruit_sales = pd.DataFrame(fruit_sales, index=('2017 Sales', '2018 Sales'))
print(new_fruit_sales)