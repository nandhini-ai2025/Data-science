class Univariate():
    def QuanQual(dataset):
        Quan=[]
        Qual=[]
        for columnName in dataset.columns:
            print(columnName)
            if(dataset["gender"].dtype=='O'):
                print("Qual")
                Qual.append(columnName)
            else:
                print("Quan")
                Quan.append(columnName)
                return Quan,Qual