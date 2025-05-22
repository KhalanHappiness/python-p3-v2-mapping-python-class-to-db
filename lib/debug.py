#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb

Department.drop_table()
Department.create_table()

payroll = Department.create("Payroll", "Building A, 5th floor")
print (payroll)

ict = Department.create("Info and Comm Tech", "Times towers" )
print (ict)
# payroll.save()
# print(payroll)

hr = Department.create("Human resource", "Building C, East Wing")
print(hr)

# hr.save()
# print(hr)

hr.name = 'HR'
hr.location = 'Building F, 10th Floor'
hr.update()
print (hr)

print("Delete payroll")
payroll.delete()
print(payroll)

ipdb.set_trace()
