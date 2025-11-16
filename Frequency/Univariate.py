    class Univariate():
    def quanQual(dataset):
        qual = []
        quan = []
        for columnName in dataset.columns:
            if(dataset[columnName].dtype == 'O'):
                qual.append(columnName)
            else:
                quan.append(columnName)
        return quan,qual

    def Univariate(dataset, quan):
        descriptive = pd.DataFrame(index = ["Mean", "Median", "Mode", "Q1:25%", "Q2:50%",
                                            "Q3:75%", "Q4:100%", "IQR", "1.5rule", "Lesser", "Greater", "Min", "Max"], columns = quan)
        for columnName in quan:
            descriptive[columnName]["Mean"] = dataset[columnName].mean()
            descriptive[columnName]["Median"] = dataset[columnName].median()
            descriptive[columnName]["Mode"] = dataset[columnName].mode()[0]
            descriptive[columnName]["Q1:25%"] = dataset.describe()[columnName]["25%"]
            descriptive[columnName]["Q2:50%"] = dataset.describe()[columnName]["50%"]
            descriptive[columnName]["Q3:75%"] = dataset.describe()[columnName]["75%"]
            descriptive[columnName]["Q4:100%"] = dataset.describe()[columnName]["max"]
            descriptive[columnName]["IQR"] = descriptive[columnName]["Q3:75%"]-descriptive[columnName]["Q1:25%"]
            descriptive[columnName]["1.5rule"] = 1.5 * descriptive[columnName]["IQR"]
            descriptive[columnName]["Lesser"] = descriptive[columnName]["Q1:25%"]-descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Greater"] = descriptive[columnName]["Q3:75%"]+descriptive[columnName]["1.5rule"]
            descriptive[columnName]["Min"] = dataset[columnName].min()
            descriptive[columnName]["Max"] = dataset[columnName].max()
            descriptive[columnName]["Kurtosis"] = dataset[columnName].kurtosis()
            descriptive[columnName]["skew"] = dataset[columnName].skew()
            descriptive[columnName]["Var"] = dataset[columnName].var()
            descriptive[columnName]["Std"] = dataset[columnName].std()
        return descriptive

    def freqTable(columnName, dataset):
        freqTable = pd.DataFrame(columns = ["Unique_values", "Frequency", "Relative_Frequency", "Cumsum"])
        freqTable["Unique_values"] = dataset[columnName].value_counts().index
        freqTable["Frequency"] = dataset[columnName].value_counts().values
        freqTable["Relative_Frequency"] = freqTable["Frequency"]/103
        freqTable["Cumsum"] = freqTable["Relative_Frequency"].cumsum()
        return freqTable

    def outlier_columnNames(descriptive):
        lesser = []
        greater = []
        
        for columnName in quan:
            if(descriptive[columnName]["Min"] < descriptive[columnName]["Lesser"]):
                lesser.append(columnName)
            if(descriptive[columnName]["Max"] > descriptive[columnName]["Greater"]):
                greater.append(columnName)
        return lesser, greater

    def replacing_outliers(dataset, descriptive):
        for columnName in lesser:
            dataset[columnName][dataset[columnName] < descriptive[columnName]["Lesser"]] = descriptive[columnName]["Lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName] > descriptive[columnName]["Greater"]] = descriptive[c