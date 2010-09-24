from datagrid.grids import DataGrid, Column, NonDatabaseColumn


class SimpleGrid(DataGrid):
    name = NonDatabaseColumn("Hello")
    
class RealGrid(DataGrid):
    name = Column()
    publisher = Column()
    recommended_by = Column()
    
class SortableGrid(DataGrid):
    name = Column(sortable = True)
    publisher = Column(sortable = True)
    recommended_by = Column(sortable = True)