from requests.auth import HTTPBasicAuth
import requests
#from pyproj import Transformer

def get_precipitation_from_point(startdate, enddate, cube, easting, northing, host, user='', pw='', epsg=32632, printout=False, get_query=False, use_credentials=False):
    '''
    get precipitation data from JKI DataCube
    
    PARAMETERS:
        startdate (str): YYYY-MM-DD
        enddate (str): YYYY-MM-DD
        layer (str): layer name of the data cube (coverage ID) 
        easting (float): longitude coordinate
        northing (float): latitude coordinate
        host (str): the host adress of the Data Cube
        epsg (int): defines coordinate reference system (CRS) of the input (easting and northing) and output coordinates. Defaults to 32632.
        user (str): credentials username
        pw (str): credentials password
        printout (bool(opt)): If True, some information will be printed about the success of request. Defaults to False.
        get_query (bool(opt)): If True, final WCS URL will be printed. Defaults to False. 
        use_credentials (bool(opt)): If True: personal credentials for datacube service will be used. Defaults to False.
        
    RETURNS:
        float_list (list): list of daily sums of precipitation in mm as float numbers
    
    '''
    try:
        query = f'{host}?&SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID={cube}&SUBSET=ansi("{startdate}T00:00:00.000Z","{enddate}T11:59:00.000Z")&subsettingCrs=http://ows.rasdaman.org/def/crs/EPSG/0/{str(epsg)}&SUBSET=E({easting})&SUBSET=N({northing})&outputCrs=http://ows.rasdaman.org/def/crs/EPSG/0/{str(epsg)}&FORMAT=text/csv'
        
        if get_query == True:
            print(query)
        
        # run querry
        if use_credentials == True:
            response = requests.get(query, auth=HTTPBasicAuth(user,pw))
        else:
            response = requests.get(query)
        
        # check if query successful
        if response.status_code == 200: # status code 200 means request wasd successful
            if printout==True:
                print('request was sucessfull! Request Status: {}'.format(response.status_code))
            
            float_map = map(float, str(response.content).split("'")[1].split(','))
            float_list = list(float_map)
            
            if float_list[0] != -9999 and len(float_list)>1:
                for ind, i in enumerate(float_list):
                    if i==-9999.0:
                        float_list[ind]=0.0
                    float_list[ind]=float_list[ind]/10
                return float_list
            elif float_list[0] == -9999:
                print('No precipitation data, returning a list of zeros...')
                float_list = [0] * len(float_list)
                return float_list
            
        elif response.status_code == 404: # status code 404 means bad request
            if printout==True:
                print('bad request! Request Status: {}'.format(response.status_code))
                print('response content: ', response.text)
            return response
        else:
            if printout==True:
                print('something went wrong. Request was answered with request code: {}. URL: {}'.format(response.status_code, response.url))
                print('response content: ', response.text)
            else:
                pass
            return response
   

    except Exception as e:
        print(e)