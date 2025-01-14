# Copyright 2016 - 2018 Raik Gruenberg

# This file is part of the LabHamster project (https://github.com/graik/labhamster).
# LabHamster is released under the MIT open source license, which you can find
# along with this project (LICENSE) or at <https://opensource.org/licenses/MIT>.
from django.urls import re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'^', admin.site.urls),
]
