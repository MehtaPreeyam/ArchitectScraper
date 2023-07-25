from enum import Enum
from disease_categories import category_dict, Category

class DigitalHealthStartup:

    name = ''
    locations_serviced = []
    insurance_plans = []
    cost_info = ''
    min_age = ''
    max_age = ''
    targeted_sex = ''
    targeted_gender = ''
    targeted_race_or_ethnicity = ''
    targeted_income = ''
    disease_category = Category.Other
    disease_subcategory = ''


    def __init__(self, name):
        self.name = name
    
    def add_location_serviced(self, location):
        self.locations_serviced.append(location)
    
    def add_insurance_plan(self, insurance_plan):
        self.insurance_plans.append(insurance_plan)
    
    def set_disease_category(self, disease_category: Category):
        self.disease_category = disease_category
    
    def set_disease_subcategory(self, disease_subcategory):
        self.disease_subcategory = disease_subcategory
    
    def convert_to_csv():