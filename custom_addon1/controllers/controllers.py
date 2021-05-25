# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddon1(http.Controller):
#     @http.route('/custom_addon1/custom_addon1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addon1/custom_addon1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addon1.listing', {
#             'root': '/custom_addon1/custom_addon1',
#             'objects': http.request.env['custom_addon1.custom_addon1'].search([]),
#         })

#     @http.route('/custom_addon1/custom_addon1/objects/<model("custom_addon1.custom_addon1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addon1.object', {
#             'object': obj
#         })
