from django.test import TestCase

# This import causes RuntimeError: Model class harvest.models.TreeType doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS
# See https://medium.com/@michal.bock/fix-weird-exceptions-when-running-django-tests-f58def71b59a
# from harvest.models import (Property, Harvest, RequestForParticipation, TreeType, 
#                             Equipment, EquipmentType, HarvestYield, Comment, PropertyImage)
