import uuid

from django.db import models
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
from django.urls import reverse


# Create your models here.

class Genre(models.Model):
    """Model to represent book genre"""
    name = models.CharField(
        max_length=200,
        unique=True,
        help_text="Enter your Genre(e.g. Science fiction, Poetry, etc.)"
    )

    def __str__(self):
        return self.name

    def get_absolute_path(self):
        """Returns the url to access a particular genre instance."""
        return reverse ('genre_detail', args=[str(self.id)])


    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='genre_name_case_insensitive_unique',
                violation_error_message = "Genre already exists (case insensitive match)"
            ),
        ]

class Language(models.Model):
    """Model representing a Language (e.g. English, French, Japanese, etc.)"""
    name = models.CharField(max_length=200, unique=True, help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)")

    def get_absolute_url(self):
        """Returns the url to access a particular language instance."""
        return reverse('language-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object (in Admin site etc.)"""
        return self.name

    class Meta:
        constraints = [
            UniqueConstraint(
                Lower('name'),
                name='language_name_case_insensitive_unique',
                violation_error_message = "Language already exists (case insensitive match)"
            ),
        ]


class Author(models.Model):
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ['pk']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.first_name}'


class Book(models.Model):
    title = models.CharField( max_length=200)
    # Foreign Key used because book can only have one author, but authors can have multiple books.
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter brief description for this Book")
    isbn = models.CharField('ISBN', max_length=13, unique=True,
        help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    # Genre class has already been defined so we can specify the object above.
    genre = models.ManyToManyField('Genre', help_text="Select a genre for this Book")
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True, help_text="Select the language of the book")

    def display_genre(self):
        """Create a string for the Genre. This is required to display genre in Admin."""
        return ', '.join(genre.name for genre in self.genre.all())

    display_genre.short_description = 'Genre'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', args=[self.id])

class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
        help_text='Unique ID for this particular book across the whole library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(
        help_text='Book availability',
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        max_length=1,
    )

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} ({self.book.title})'




