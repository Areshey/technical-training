from odoo import api,models,fields


class BooksCopies(models.Model):
    _name = 'library.bookcopies'
    _description = 'book copies'
 #   _inherits="library.book"
    _inherits = {
    'library.book': 'books_id',
}
    
    book_ids= fields.Many2one("library.book",string="book", required=True, ondelete='cascade')
    reference=fields.Char(string="reference")
    

   #rental_ids = fields.One2many('library.rental', string='Rentals')