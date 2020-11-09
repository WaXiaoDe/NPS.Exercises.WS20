import csv
import os
import matplotlib.pyplot as plt


# This function creates the output csv file as required 
def writeCsv(name,data):
    # First, we generate a 'temp.csv' to store the resulting data
    with open('temp.csv', 'w', newline='\n') as output_file:
        writer = csv.writer(output_file, delimiter=',')
        for p in data:
            writer.writerow(p)
            #writer.writerow(point)
    output_file.close()
    
    # Then, we copy the content of 'temp.csv' to the target file and
    # replace every ',' with ', ' 
    with open('temp.csv') as infile, open(name, 'w') as outfile:
        for line in infile:
            line = line.replace(",", ", ")
            outfile.write(line)
    # Finally, the 'temp.csv' will be deleted
    os.remove('temp.csv')




# Define the function for graphical illustration
def plot_data(X,Y):
    snow_x = []
    snow_y = []
    black_x = []
    black_y = []
    for i in range(len(Y)):
        if Y[i] == 1:
            snow_x.append(X[i][0])
            snow_y.append(X[i][1])
        else: 
            black_x.append(X[i][0])
            black_y.append(X[i][1])
    plt.scatter(black_x,black_y,s=4,color="black")
    plt.scatter(snow_x,snow_y,s=4,color="silver")

    plt.show()
    

# Read the Data from a csv file 

def read_csv(name):
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    Path_csv = os.path.join(THIS_FOLDER, name)
    with open(Path_csv) as File:
        Data = csv.reader(File, delimiter=',')
        pointSet = []
        for point in Data:
            for i in range(len(point)):
                point[i] = float(point[i])
            #pointSet.append([ point[0], np.array(point[1:]) ])
            pointSet.append([ point[0], point[1:]])
    File.close()
    return pointSet
