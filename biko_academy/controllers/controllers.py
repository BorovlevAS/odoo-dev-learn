from odoo import http

class Academy(http.Controller):

    @http.route('/academy/academy/', auth='public', website=True)
    def index(self, **kw):
        Teachers = http.request.env['biko_academy.teachers']
        return http.request.render('biko_academy.index', {
            'teachers': Teachers.search([])
        })

    @http.route('/academy/<model("biko_academy.teachers"):teacher>/', auth='public', website=True)
    def teacher(self, teacher):
        return http.request.render('biko_academy.biography', {
            'person': teacher
        })