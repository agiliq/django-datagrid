from mylibrary.grids import SimpleGrid, RealGrid
from mylibrary.models import Book

def simple(request):
    books = Book.objects.all()
    return SimpleGrid(request, books).render_to_response("mylibrary/simple.html")


def real(request):
    books = Book.objects.all()
    return RealGrid(request, books).render_to_response("mylibrary/real.html")