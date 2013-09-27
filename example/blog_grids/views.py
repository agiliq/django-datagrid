from datagrid.grids import *
from blog_grids.models import Employee

def grid_data_func(value):
    return value.upper() 

def slug_link_func(obj, value):
    # return  args[0]
    return 'http://google.com/404/'

def non_db_col_value(obj):
    return obj.title

class BlogGrid(DataGrid):
    created_by = Column(sortable=True, 
                        link=True, 
                        cell_clickable=True, 
                        css_class='red')
    
    created_on = DateTimeColumn("created on", 
                                format='d b, Y', 
                                sortable=True, 
                                link=False)
    
    created_on_since = DateTimeSinceColumn("created on ", 
                                           sortable=True, 
                                           db_field='created_on')
    
    slug = Column("Slug", 
                  sortable=False, 
                  link=False, 
                  link_func=slug_link_func, 
                  image_url='/site_media/blogango/images/date_icon.png')
    
    title = Column("Title", 
                   sortable=True, 
                   link=False, 
                   db_field='title', 
                   image_url='http://media.agiliq.com/images/terminal.png', 
                   image_width=20, 
                   image_height=20, 
                   image_alt='foo bar', 
                   data_func=grid_data_func)
    
    blog_title = NonDatabaseColumn("Second Title", sortable=True, link=True, data_func=non_db_col_value)
    col1 = NonDatabaseColumn(sortable=True, link=True, data_func=non_db_col_value)

def blog_grid(request):
    employees = Employee.objects.all()
    blog_grid = BlogGrid(request=request, queryset=employees, title='Blog Grid View')
    return blog_grid.render_to_response('blog_grid/blog_grid.html', {'blog_grid': blog_grid})
