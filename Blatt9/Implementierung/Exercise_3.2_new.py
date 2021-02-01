import dload
import os
import zipfile
import Assistant_Functions as af
import random 
import cmath



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

    dict_job = { 'admin.':[1,0,0,0,0,0,0,0,0,0,0,0], 'unknown':[0,1,0,0,0,0,0,0,0,0,0,0],\
                 'unemployed':[0,0,1,0,0,0,0,0,0,0,0,0], 'management':[0,0,0,1,0,0,0,0,0,0,0,0],\
                 'housemaid':[0,0,0,0,1,0,0,0,0,0,0,0], 'entrepreneur':[0,0,0,0,0,1,0,0,0,0,0,0],\
                 'student':[0,0,0,0,0,0,1,0,0,0,0,0], 'blue-collar':[0,0,0,0,0,0,0,1,0,0,0,0],\
                 'self-employed':[0,0,0,0,0,0,0,0,1,0,0,0], 'retired':[0,0,0,0,0,0,0,0,0,1,0,0],\
                 'technician':[0,0,0,0,0,0,0,0,0,0,1,0], 'services':[0,0,0,0,0,0,0,0,0,0,0,1]}

    dict_marital = {'married':[1,0,0], 'divorced':[0,1,0], 'single':[0,0,1]}

    dict_education = {'unknown':[1,0,0,0], 'primary':[0,1,0,0], \
                      'secondary':[0,0,1,0], 'tertiary':[0,0,0,1] }

    dict_contact = { 'unknown':[1,0,0], 'cellular':[0,1,0], 'telephone':[0,0,1]}

    ksi =  cmath.rect(1,cmath.pi/6)
    dict_month = { 'jan':[ksi.real,ksi.imag], 'feb':[(ksi**2).real,(ksi**2).imag], \
                   'mar':[(ksi**3).real,(ksi**3).imag], 'apr':[(ksi**4).real,(ksi**4).imag],\
                   'may':[(ksi**5).real,(ksi**5).imag], 'jun':[(ksi**6).real,(ksi**6).imag], \
                   'jul':[(ksi**7).real,(ksi**7).imag], 'aug':[(ksi**8).real,(ksi**8).imag], \
                   'sep':[(ksi**9).real,(ksi**9).imag], 'oct':[(ksi**10).real,(ksi**10).imag],\
                   'nov':[(ksi**11).real,(ksi**11).imag], 'dec':[(ksi**12).real,(ksi**12).imag] }

    dict_outcome = { "unknown":[1,0,0,0],"other":[0,1,0,0],\
                     "failure":[0,0,1,0],"success":[0,0,0,1] }

    dictionary_others = {'yes':1, 'no':-1 }

    temp_dict = { 5:0, 9:0, 11:0, 12:0, 13:0, 14:0 }

    for p in data:
        for i in [5,9,11,12,13,14]:
            p[i] = float(p[i])
            temp_dict[i] = max( temp_dict[i], abs(p[i]) )

    for p in data:
        for i in [5,9,11,12,13,14]:
            p[i] = p[i]/temp_dict[i]

    result = []

    for p in data:
        temp = []
        temp.append( float(p[0])/100)
        temp = temp + dict_job[p[1]]
        temp = temp + dict_marital[p[2]] 
        temp = temp + dict_education[p[3]]
        temp.append(dictionary_others[p[4]])
        temp.append(p[5])
        temp.append(dictionary_others[p[6]])
        temp.append(dictionary_others[p[7]])
        temp = temp + dict_contact[p[8]]
        temp.append(p[9])        
        temp = temp + dict_month[p[10]]
        temp.append(p[11])
        temp.append(p[12])
        temp.append(p[13])
        temp.append(p[14])
        temp = temp + dict_outcome[p[15]]
        temp.insert(0,dictionary_others[p[16]])
        result.append(temp)

    test = []
    train = []
    
    for p in result: 
        if random.randint(0,1) == 1: 
            test.append(p)
        else:
            train.append(p)
    
    af.writeCsv('bank-marketing.csv',result)
    af.writeCsv('bank-marketing.train.csv',train)
    af.writeCsv('bank-marketing.test.csv',test)




#####     Execution Area     #####

#download_extract_full_bank_file()
read_modified_save_data_set()