"""Download script for geopotential height at 300, 500, 750, 850, 975 hPa for climatology (2011-21)"""

import cdsapi

climatology = [
    "2011", 
    "2012", 
    "2013", 
    "2014", 
    "2015", 
    "2016", 
    "2017", 
    "2018", 
    "2019", 
    "2020", 
    "2021", 
               ]

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": ["geopotential"],
    "year": [],
    "month": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ],
    "day": [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ],
    "time": [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ],
    "pressure_level": [
        "300", "500", "700",
        "850", "975"
    ],
    "data_format": "netcdf",
    "download_format": "zip",
    "area": [62, -20, 33, 28]
}

def set_request_year(r, year):
    r["year"] = [year]
    return r

for year in climatology:
    request = set_request_year(request, year)
    client = cdsapi.Client()
    client.retrieve(dataset, request).download()
