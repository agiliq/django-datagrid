from datagrid.grids import DataGrid, Column, NonDatabaseColumn


class SimpleGrid(DataGrid):
    name = NonDatabaseColumn("Hello")
    
class RealGrid(DataGrid):
    name = Column()
    publisher = Column()
    recommended_by = Column()
    
