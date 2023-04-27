class CSVexplorer():
    def __init__(self, filepath:str, ignoreRow = None, ignoreColumn = None):
        self.buffer = {}
        self.header = {}
        if ignoreRow == None: ignoreRow = []
        elif type(ignoreRow) == int: ignoreRow = [ignoreRow]
            
        from csv import reader
        with open(filepath) as f:
            row = 0
            column = 0
            _reader = reader(f, dialect = "excel")
            for rowNum, row in enumerate(_reader):
                if rowNum == ignoreRow or rowNum in ignoreRow:
                    continue
                elif rowNum == 0:
                    for col, item in enumerate(row):
                        self.header[col] = item
                        self.buffer[item] = []
                else:
                    for col, item in enumerate(row):
                        self.buffer[self.header[col]].append(item)
        
    def getHeader(self):
        return self.header
    
    def getColumn(self, col):
        if type(col) == int:
            return self.buffer[self.header[col]]
        else: return self.buffer[col]
    
    # Attemps to convert a column to a specified data type using the
    # default data class __init__ method
    def convertType(self, col, T = str):
        if hasattr(col, '__iter__') and type(col) != str:
            for _col in col:
                if type(_col) == int:
                    __col = self.header[_col]
                else: __col = _col
                for i, val in enumerate(self.buffer[__col]):
                    self.buffer[__col][i] = T(val)
        else:
            if type(col) == int:
                col = self.header[col]
            for i, val in enumerate(self.buffer[col]):
                self.buffer[col][i] = T(val)
    
    # Converts a column's container to a specified container type
    # Example usage: convertContainer(["x", "x1"], np.array) 
    def convertContainer(self, col, T = list):
        if hasattr(col, '__iter__') and type(col) != str:
            for _col in col:
                if type(_col) == int:
                    self.buffer[self.header[_col]] = T(self.buffer[self.header[_col]])
                else:
                    self.buffer[_col] = T(self.buffer[_col])
        else:
            self.buffer[col] = T(self.buffer[col])
            
    def __getitem__(self, col):
        if type(col) == int:
            return self.buffer[self.header[col]]
        else:
            return self.buffer[col]