from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import traceback


class BookListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            title1=request.data.get('title','')
            author=request.data.get('author','')
            isbn=request.data.get('isbn',None)
            published_date=request.data.get('published_date',None)

            bd=Book(
                title=title1,
                author=author,
                isbn=isbn,
                published_date=published_date,
            )

            bd.save()
            return Response('saved')
        except Exception as e:
            print(e)
            traceback.print_exc()


    def get(self,request):
        books_data=Book.objects.all()
        print(f'{books_data=}')
        data=[]
        for book in books_data:
            book_dict={
                'ID':book.id,

                'title':book.title,
                'author':book.author,
                'isbn':book.isbn,
                'bookImage': book.bookImage,
                'published_date':book.published_date,
            }
            data.append(book_dict)
        return Response(data)
    
    def put(self, request, book_id):
        try:
            book = Book.objects.filter(id=book_id).first()
            print(f'{book=}')

            print(f'{book.title=}')
            if not book:
                return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

            book.title = request.data.get('title', book.title)
            book.author = request.data.get('author', book.author)
            book.isbn = request.data.get('isbn', book.isbn)
            book.published_date = request.data.get('published_date', book.published_date)
            book.bookImage = request.data.get('bookImage', book.bookImage)

            book.save()

            return Response({'message': 'Book updated successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            return Response({'error': 'An error occurred while updating the book.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, book_id):
        try:
            book = Book.objects.filter(id=book_id)
            if not book:
                return Response({'error': 'Book not found.'}, status=status.HTTP_404_NOT_FOUND)

            book.delete()
            return Response({'message': 'Book deleted successfully.'}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error: {e}")
            traceback.print_exc()
            return Response({'error': 'An error occurred while deleting the book.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    
