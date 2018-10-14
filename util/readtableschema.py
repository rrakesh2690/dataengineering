'''
Created on March 29, 2018

@author: Rajnikant Rakesh
This module returns python List of table fields for a table in BigQuery.
It does not read from file it reads from actual table definition from BigQuery 

'''
import logging
import argparse
import os
from google.cloud import bigquery

def readtableschema (projectid, datasetname, tablename):
    tablefields = []
    try:
        bigqclient = bigquery.Client(project=projectid)
        datasetname = bigqclient.dataset(datasetname)
        print datasetname
        table_ref = datasetname.table(tablename)
        #table = bigquery.table
        print table_ref
        #table.reload()
        table = bigqclient.get_table(table_ref)
        tableschema = table.schema
        print(table.schema)
        for fields in tableschema:
            tablefields.append(fields.name)
    except:
        logging.exception('Failed to read tableschema for table {}.{}'.format(datasetname, tablename))
        logging.info('Failed to read tableschema for table {}.{}'.format(datasetname, tablename))
        raise NameError
    return tablefields

def readtableschemaasstring(projectid, datasetname, tablename):
    schema = ""
    try:
        bigqclient = bigquery.Client(project=projectid)
        datasetname = bigqclient.dataset(datasetname)
        table_ref = datasetname.table(tablename)
        #table.reload()
        #tableschema = table.schema
        table = bigqclient.get_table(table_ref)
        tableschema = table.schema
        # print(table.schema)
        for fields in tableschema:
            schema=schema+fields.name+":"+fields.field_type+", "
    except:
        logging.exception('Failed to read tableschema for table {}.{}'.format(datasetname, tablename))
        raise NameError
    return schema