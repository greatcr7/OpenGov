"""Top-level package for OpenGov."""
import requests
from opengov import *

__author__ = """Brandon Jin"""
__email__ = 'brandonjincmu@gmail.com'
__version__ = '0.1.0'

data_sources = dict()
data_sources["Available"] = ['FDA - US Food & Drug Administration', 'FTC - Federal Trade Commission']
data_sources["In Development"] = ['SEC - US Securities & Exchange Commission']
data_sources["Planned"] = ["FHFA - Federal Housing Finance Agency", "CFPB - Consumer Financial Protection Bureau"]



def list_agencies(available_only = True):
    # print only sources available
    if available_only:
        print("AVAILABLE DATA SOURCES (Version " + __version__ + ") : ")
        print("============")
        for source in data_sources["Available"]:
            print(source)

    # when asked, print all the data sources planned as well
    else:
        print("AVAILABLE DATA SOURCES (Version " + __version__ + ") : ")
        print("============")
        if data_sources["Available"] == []:
            print("None")
        else:
            for source in data_sources["Available"]:
                print(source)

        print("\n")
        print("IN DEVELOPMENT DATA SOURCES (Version " + __version__ + ") : ")
        print("============")
        if data_sources["In Development"] == []:
            print("None")
        else:
            for source in data_sources["In Development"]:
                print(source)

        print("\n")
        print("PLANNED DATA SOURCES (Version " + __version__ + ") : ")
        print("============")
        if data_sources["Planned"] == []:
            print("None")
        else:
            for source in data_sources["Planned"]:
                print(source)


    print("\n")
    print("Done!")
