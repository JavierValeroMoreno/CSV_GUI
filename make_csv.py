import pandas as pd

class CSV_List:
    def __init__(self, path:list = []):
        self.file_names = []
        self.file_dict = {}
        self.file_headers = {}
        for el in path:
            self.file_names.append(el.split("/")[-1])
            self.file_dict[el.split("/")[-1]] = pd.read_csv(el, header = 0)
            self.file_headers[el.split("/")[-1]] = self.file_dict[el.split("/")[-1]].columns
            

def make_csv(path):

    global_df :pd.DataFrame = pd.read_csv("{}/root-data-global.csv".format(path), header = 0)
    base_df :pd.DataFrame = pd.read_csv("{}/root-data-base.csv".format(path), header = 0)

    global_df = global_df.sort_values(by= ['image'])
    base_df = base_df.sort_values(by= ['image'])

    aux = base_df['image'].str.split(pat=".", expand = True)[0].str.split(pat="-",expand = True)

    aux = aux.rename(columns = {1:'codigo', 2:'fecha',3:'hora'})

    result = pd.concat([base_df, global_df[' depth'], aux[['codigo','fecha','hora']]], axis = 1)

 
    result.to_csv("{}/Datos.csv".format(path), index = False)
