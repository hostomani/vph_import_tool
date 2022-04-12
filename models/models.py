# -*- coding: utf-8 -*-

from odoo import models, fields, api
from xlrd import open_workbook
import xlrd
import base64
import io
import csv


class ImportTool(models.TransientModel):
    _name = 'import.tool'

    model_id = fields.Many2one('ir.model')
    model_name = fields.Char(related='model_id.model')
    product_category = fields.Many2one('product.category')
    file = fields.Binary()

    def import_data(self):
        csv_data = base64.b64decode(self.file)
        data_file = io.StringIO(csv_data.decode("utf-8"))
        data_file.seek(0)
        file_reader = []
        csv_reader = csv.reader(data_file, delimiter=',')
        file_reader.extend(csv_reader)
        print(file_reader)
        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'import.tool',
        }