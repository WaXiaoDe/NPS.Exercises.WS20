import dload
import os
import zipfile
import Assistant_Functions as af
import random 



def download_extract_full_bank_file():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00222/bank.zip"
    dload.save_unzip(url)
    filename = os.getcwd()+'/bank.zip'
    fz = zipfile.ZipFile(filename, 'r')
    fz.extractall()
    os.remove(os.getcwd()+'/bank.zip')
    os.remove(os.getcwd()+'/bank.csv')
    os.remove(os.getcwd()+'/bank-full.csv')
    os.remove(os.getcwd()+'/bank-names.txt')
   


def read_modified_save_data_set():
    data = af.read_data_without_label(os.getcwd() + '/bank/bank-full.csv')
    del data[0]

    dictionary_job = {'admin.':43000/75000, 'unknown':48000/75000, 'unemployed':5000/75000,\
                      'management':74000/75000, 'housemaid':33000/75000, 'entrepreneur':75000/75000,\
                      'student':4000/75000, 'blue-collar':35000/75000, 'self-employed':42000/75000, \
                      'retired':40500/75000, 'technician':45000/75000, 'services':49300/75000 }
    dictionary_others = {'yes':1, 'no':-1, \
                         'married':-1, 'divorced':0, 'single':1, \
                         'unknown':0, \
                         'primary':1/3, 'secondary':2/3, 'tertiary':1, \
                         'cellular':1, 'telephone':-1, \
                         'jan':1/12, 'feb':2/12, 'mar':3/12, 'apr':4/12, 'may':5/12, 'jun':6/12, \
                         'jul':7/12, 'aug':8/12, 'sep':9/12, 'oct':10/12, 'nov':11/12, 'dec':12/12, \
                         'success':1, 'failure':-1, 'other':0 }
    temp_dict = { 5:-100, 9:-100, 11:-100, 12:-100, 13:-100, 14:-100 }
    for p in data:
        p[0] = float(p[0])/100
        p[1] = dictionary_job[p[1]]
        for i in [2,3,4,6,7,8,10,15,16]:
            p[i] = dictionary_others[p[i]]
        for i in [5,9,11,12,13,14]:
            p[i] = float(p[i])
            temp_dict[i] = max( temp_dict[i], p[i] )
    
    test = []
    train = []
    
    for p in data: 
        for i in [5,9,11,12,13,14]:
            p[i] = p[i] / temp_dict[i]
        p.insert(0,p[16])
        del p[16]
        if random.randint(0,1) == 1: 
            test.append(p)
        else:
            train.append(p)
    
    af.writeCsv('bank-marketing.csv',data)
    af.writeCsv('bank-marketing.train.csv',train)
    af.writeCsv('bank-marketing.test.csv',test)




#####     Execution Area     #####

#download_extract_full_bank_file()
read_modified_save_data_set()