# -*- coding: utf-8 -*-
# from odoo import http


# class VphImportTool(http.Controller):
#     @http.route('/vph_import_tool/vph_import_tool/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vph_import_tool/vph_import_tool/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vph_import_tool.listing', {
#             'root': '/vph_import_tool/vph_import_tool',
#             'objects': http.request.env['vph_import_tool.vph_import_tool'].search([]),
#         })

#     @http.route('/vph_import_tool/vph_import_tool/objects/<model("vph_import_tool.vph_import_tool"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vph_import_tool.object', {
#             'object': obj
#         })
