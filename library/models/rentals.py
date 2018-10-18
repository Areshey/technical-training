# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')

    #nickname = fields.Char(related='partner.name', store=True)
    isbn = fields.Char(related='book_id.isbn')
    publisher_name=fields.Char(related="book_id.publisher_id.name",string="publisher Name")
    
    address = fields.Text(related='customer_id.address')
    
    
    
