from mylibrary.grids import SimpleGrid
from mylibrary.models import Book

def simple(request):
    books = Book.objects.all()
    return SimpleGrid(request, books).render_to_response("mylibrary/simple.html")
