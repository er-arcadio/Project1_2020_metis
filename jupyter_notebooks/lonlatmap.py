#!/usr/bin/env python
# coding: utf-8
# In[ ]:
"""
The following code was inspired by 
https://www.kaggle.com/muonneutrino/mapping-new-york-city-census-data/#The-Census-Data
The convert_to_2d function is used to take geo information and return a grid area of lon and lats
the make_plot function uses matplotlib to graph area by density of values
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def convert_to_2d(lats, lons, values):
    """
    this function converts geo information
    """
    latmin = 40.48
    lonmin = -74.28
    latmax = 40.93
    lonmax = -73.65
    lon_vals = np.mgrid[lonmin:lonmax:200j]
    lat_vals = np.mgrid[latmin:latmax:200j]
    map_values = np.zeros([200, 200])
    dlat = lat_vals[1] - lat_vals[0]
    dlon = lon_vals[1] - lon_vals[0]
    for lat, lon, value in zip(lats, lons, values):
        lat_idx = int(np.rint((lat - latmin) / dlat))
        lon_idx = int(np.rint((lon - lonmin) / dlon))        
        if not np.isnan(value):
            map_values[lon_idx, lat_idx] = value
    return lat_vals, lon_vals, map_values

def make_plot(blocks, data_values, title='', colors='White'):
    """
    this function uses grid information to create a density map
    """
    lat_vals, lon_vals, values = convert_to_2d(blocks.Latitude, blocks.Longitude, data_values)
    fig, ax = plt.subplots(figsize = [12, 12])
    limits = np.min(lon_vals), np.max(lon_vals), np.min(lat_vals), np.max(lat_vals)
    im = ax.imshow(values.T, origin='lower', cmap=colors, extent=limits, zorder = 1)
    ax.autoscale(False)
    plt.xlabel('Longitude [degrees]')
    plt.ylabel('Latitude [degrees]')
    plt.title(title)
    plt.colorbar(im, fraction=0.035, pad=0.04)
    plt.show()
