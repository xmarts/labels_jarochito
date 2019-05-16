# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class LabelsPallets(models.Model):

	_name = 'labels.pallets'

	name = fields.Char( string = 'Nombre' )

	turn = fields.Selection( [('mat','Matutino'),('ves','Vespertino'),('noc','Nocturno')] , string = 'Turno' )

	pallet = fields.Many2one( 'pallets' , string = 'Tarima' )

	date = fields.Date( string = 'Fecha' )

	def _get_consecutivo_num(self, cr, uid, context=None):
		last_id = 0
		get_count = self.search(cr, uid, [(1, '=', 1)], order='id')
		if get_count:
			for item in self.browse(cr, uid, get_count, context):
				sec = item.consecutivo.split('-')
				sec_num = int(sec[1]) + 1
				last_id = sec_num
		else:
			last_id = 1
		prefijo = 'EST-'
		serie = last_id
		consecutivo = prefijo + str(serie).rjust(5, '0')
		return consecutivo

class Pallets(models.Model):

	_name = 'pallets'

	pallet_name = fields.Char( string = 'Tarima' )

	_rec_name = 'pallet_name'