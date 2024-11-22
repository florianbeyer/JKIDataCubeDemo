import requests # python package to handle REST query

def get_phases_from_point(year, cube, easting, northing, host, epsg=32632, printout=False, get_query=False):
    '''
    get PHASE data from JKI DataCube 
    (more info: https://sf.julius-kuehn.de/openapi/phase/)
    
    PARAMETERS:
        year (str): year YYYY
        cube (str): choose one of the available crops on JKI DataCube
        easting (float): longitude coordinate
        northing (float): latitude coordinate
        host (str): the host adress of the Data Cube
        epsg (int): defines coordinate reference system (CRS) of the input (easting and northing) and output coordinates. Defaults to 32632.
        printout (bool(opt)): If True, some information will be printed about the success of request. Defaults to False.
        get_query (bool(opt)): If True, final WCS URL will be printed. Defaults to False.
        
    RETURNS:
        list_ (list): A list of the potential starting dates of the phenological stages.
    
    '''
    try:
        date = str(year)+'-01-01' # multiband layers of the whole year are always stored at the 1st of january

        query = f'{host}?&SERVICE=WCS&VERSION=2.0.1&REQUEST=GetCoverage&COVERAGEID={cube}&SUBSET=ansi(\"{date}\")&subsettingCrs=http://ows.rasdaman.org/def/crs/EPSG/0/{str(epsg)}&SUBSET=E({str(easting)})&SUBSET=N({str(northing)})&outputCrs=http://ows.rasdaman.org/def/crs/EPSG/0/{str(epsg)}&FORMAT=text/csv'
        
        if get_query == True:
            print(query)

        # run query
        response = requests.get(query)
        
        
        # check if query successful
        if response.status_code == 200: # status code 200 means request wasd successful
            if printout==True:
                print('request was sucessfull! Request Status: {}'.format(response.status_code))
            # transform binary result to python-like list
            list_ =str(response.content).split('"')[1].split(' ') 
            for ind, i in enumerate(list_):
                list_[ind] = float(i)
            return list_
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
        print('something went wrong: {}'.format(e))
        