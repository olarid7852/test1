from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    production_date = models.DateField()
    color = models.CharField(max_length=20)
    price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.make} {self.model} ({self.production_date})"
    
# from django.db.models import Coimport faker
# from datetime import datetime, timedelta
# from random import randint

# fake = faker.Faker()

# cars = []
# for _ in range(10000):
#     production_date = fake.date_between(start_date="-10y", end_date="-1y")
#     name = fake.company()
#     price = randint(1000, 100000)  # random price between $1,000 and $100,000
#     car = {"production_date": production_date, "name": name, "price": price}
#     cars.append(car)

# # Now you can use the 'cars' list to create records in your database
# from django.db.models import Window
# from django.db.models.functions import Extract, Lag
# from django.db.models import Count, F
# from car.models import Car

# query = Car.objects.annotate(
#     year=Extract('production_date', 'year')
# ).values('year').annotate(
#     total_cars=Count('id')
# ).annotate(
#     lag_total_cars=Window(expression=Lag('total_cars'), order_by='year')
# ).annotate(
#     growth_rate=(F('total_cars') - F('lag_total_cars')) / F('lag_total_cars') * 100
# )

# query = Car.objects.annotate(
#     year=Extract('production_date', 'year')
# ).values('year').annotate(
#     total_cars=Count('id')
# ).annotate(
#     growth_rate=(F('total_cars') * 100
# )
    

# from django.db.models import F, Window
# from django.db.models.functions import Lag

# from django.db.models import F, Window
# from django.db.models.functions import Lag, Sum

# # Assuming your model name is "Car"
# # from .models import Car

# cars = Car.objects.annotate(
#   production_year=Extract('production_date', 'year'),
# ).values(
#   'production_year'
# ).annotate(
#   total_production=Sum('quantity'),
# )

# import random
# from faker import Faker
# from django.db.models import Q
# from car.models import Car

# fake = Faker()

# cars_to_create = [
#     Car(
#         make=fake.company(),
#         model=fake.word(),
#         production_date=fake.date_between(start_date='-20y', end_date='today'),
#         color=fake.color_name()
#     ) for _ in range(1000)
# ]

# Car.objects.bulk_create(cars_to_create)

# from django.db.models import F, Window
# from django.db.models.functions import Lag

# # Assuming your model is named "Car"
# cars = Car.objects.order_by('production_date')

# # Add a lagged column to calculate the previous year's production
# cars = cars.annotate(previous_production=Window(
#     expression=Lag('production', default=0),
#     partition_by=[F('production_date').year],
#     order_by=F('production_date').asc()
# ))

# # Calculate the rate of growth for each year
# cars = cars.annotate(rate_of_growth=(F('previous_production') - F('previous_production')) / F('previous_production') * 100)

# # Fill in missing years with zero growth rate
# for year in range(2000, 2021):
#     cars = cars.annotate(year=F('production_date').year)
#     cars = cars.extra(
#         where=["year = %s"],
#         params=[year],
#         select={'year': str(year)}
#     )

# # Execute the query and retrieve the results
# result = cars.values('year', 'rate_of_growth').order_by('year')

# # Print the results
# for row in result:
#     print(f"Year: {row['year']}, Rate of Growth: {row['rate_of_growth']}%")

# from django.db.models import F, Window
# from django.db.models.functions import Lag, ExtractYear

# # Assuming your model is named "Car"
# cars = Car.objects.order_by('production_date')

# # Add a lagged column to calculate the previous year's production
# cars = cars.annotate(previous_production=Window(
#     expression=Lag('production', default=0),
#     partition_by=[ExtractYear('production_date')],
#     order_by=F('production_date').asc()
# ))

# # Calculate the rate of growth for each year
# cars = cars.annotate(rate_of_growth=(F('production') - F('previous_production')) / F('previous_production') * 100)

# # Fill in missing years with zero growth rate
# for year in range(2000, 2021):
#     cars = cars.annotate(year=ExtractYear('production_date'))
#     cars = cars.extra(
#         where=["year = %s"],
#         params=[year],
#         select={'year': str(year)}
#     )

# # Execute the query and retrieve the results
# result = cars.values('year', 'rate_of_growth').order_by('year')

# # Print the results
# for row in result:
#     print(f"Year: {row['year']}, Rate of Growth: {row['rate_of_growth']}%")

# from django.db.models import Count, Avg
# from django.db.models.functions import ExtractYear

# cars = Car.objects.annotate(year=ExtractYear('production_date')) \
#                     .values('year') \
#                     .annotate(count=Count('id'), avg_price=Avg('price')) \
#                     .order_by('year')

# result = []
# for year in range(2000, 2021):  # iterate over all years from 2000 to 2020
#     year_data = next((c for c in cars if c['year'] == year), None)
#     if year_data:
#         result.append({
#             'year': year,
#             'production_count': year_data['count'],
#             'avg_price': year_data['avg_price']
#         })
#     else:
#         result.append({
#             'year': year,
#             'production_count': 0,
#             'avg_price': 0
#         })
    

# from django.db.models import Count, Avg
# from django.db.models.functions import ExtractYear

# cars = Car.objects.annotate(year=ExtractYear('production_date')) \
#                     .values('year') \
#                     .annotate(count=Count('id'), avg_price=Avg('price')) \
#                     .order_by('year')

# result = []
# for year in range(2000, 2021):  # iterate over all years from 2000 to 2020
#     year_data = next((c for c in cars if c['year'] == year), None)
#     if year_data:
#         result.append({
#             'year': year,
#             'production_count': year_data['count'],
#             'avg_price': year_data['avg_price']
#         })
#     else:
#         result.append({
#             'year': year,
#             'production_count': 0,
#             'avg_price': 0
#         })

# from django.db.models import Count, Avg
# from django.db.models.functions import ExtractYear

# model_counts = Car.objects.annotate(year=ExtractYear('production_date')).values('year').annotate(count=Count('id')).values('year', 'count')

# result = []
# for year in range(2000, 2021):
#     count = model_counts.filter(year=year).first()
#     if count:
#         result.append({'year': year, 'count': count['count']})
#     else:
#         result.append({'year': year, 'count': 0})

# growth_rate = []
# for i in range(1, len(result)):
#     prev_year = result[i-1]
#     curr_year = result[i]
#     growth_rate.append({
#         'year': curr_year['year'],
#         'growth_rate': (curr_year['count'] - prev_year['count']) / prev_year['count'] if prev_year['count'] > 0 else 0
#     })

# from django.db.models import F, Window, Sum
# from django.db.models.functions import Lag, Extract

# # Assuming your model name is "Car"
# from car.models import Car

# def calculate_production_growth_rate():
#     # Calculate the total production for each year
#     cars = Car.objects.annotate(
#         production_year=Extract('production_date', 'year'),
#     ).values(
#         'production_year'
#     ).annotate(
#         total_production=Sum('quantity'),
#     )

#     # Calculate the lagged total production for each year
#     cars = cars.annotate(
#         previous_year_production=Window(
#             expression=Lag('total_production'),
#             order_by=F('production_year').asc(),
#         ),
#     )

#     # Calculate the growth rate as the difference between current year and previous year production
#     cars = cars.annotate(
#         growth_rate=F('total_production') - F('previous_year_production'),
#     )

#     # Return the production year and growth rate
#     return cars.values('production_year', 'growth_rate')

# from django.db.models import Count
# from django.db.models.functions import ExtractYear, TruncYear

# cars = Car.objects.annotate(year=TruncYear('production_date')).values('year').annotate(count=Count('id')).order_by('year')

# growth_rates = []
# for i in range(len(cars) - 1):
#     current_year = cars[i]['year']
#     next_year = cars[i + 1]['year']
#     current_count = cars[i]['count']
#     next_count = cars[i + 1]['count']
#     growth_rate = (next_count - current_count) / current_count
#     growth_rates.append({'year': next_year, 'growth_rate': growth_rate})

# return growth_rates

# from django.db.models import F, Window
# from django.db.models.functions import Lag

# Car.objects.annotate(
#   year=F('production_date__year'),
#   count=Window(expression=Count('id'), partition_by=[F('production_date__year')]),
#   prev_count=Lag(F('count'), 1).over(Window(partition_by=[F('production_date__year')], order_by=F('production_date__year'))),
# ).annotate(
#   growth_rate=(F('count') - F('prev_count')) / F('prev_count') * 100
# ).values('year', 'growth_rate')

# from django.db.models import F, Window
# from django.db.models.functions import Lag

# Car.objects.annotate(
#     year=F('production_date__year'),
#     count=Window(expression=Count('id'), partition_by=[F('production_date__year')]),
# ).annotate(
#     prev_count=Lag(F('count'), 1).over(Window(partition_by=F('year'))),
# ).annotate(
#     growth_rate=(F('count') - F('prev_count')) / F('prev_count') * 100
# ).values('year', 'growth_rate')

# from django.db.models import Subquery, OuterRef

# subquery = Car.objects.filter(
#     production_date__year=OuterRef('production_date__year') - 1
# ).order_by('-production_date').values('production_date__year')

# queryset = Car.objects.annotate(
#     year=F('production_date__year'),
#     count=Window(expression=Count('id'), partition_by=[F('production_date__year')]),
#     prev_count=Subquery(subquery.values('count')[:1]),
# ).annotate(
#     growth_rate=(F('count') - F('prev_count')) / F('prev_count') * 100
# ).values('year', 'growth_rate')