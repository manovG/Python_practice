# -*- coding: utf-8 -*-
"""
Created on Wed Feb 16 22:02:44 2022

@author: manov
"""
class Patient(object):
     ''' Medical centre patient'''
     
     status = 'patient'
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions}.')
         
     def add_info(self,information):
         self.conditions.append(information)
#     
#
#steve = Patient('Steven Hughes',48)
#abigail = Patient('Abigail Sandwick',32)

class Infant(Patient):
    ''' Patient under 2 years'''
    
    def __init__(self,name,age):
        self.vaccinations = []
        super().__init__(name,age)
        
    def add_vac(self,vaccine):
        self.vaccinations.append(vaccine)
        
    def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Patient has had {self.vaccinations} vaccines.' \
               f' Current information: {self.conditions}.' \
               f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')
        
#archie = Infant('Archie Fittleworth',0)        
#archie.add_vac('MMR') 
         
class Patient(object):
     ''' 
         Attributes
         ----------
         name: Patient name
         age: Patient age
         conditions: Existing medical conditions
     '''
     
     status = 'patient'
     
     def __init__(self,name,age):
         self.name = name
         self.age = age
         self.conditions = []
         
     def get_details(self):
         print(f'Patient record: {self.name}, {self.age} years.' \
               f' Current information: {self.conditions}.')
         
     def add_info(self,information):
         self.conditions.append(information)    



