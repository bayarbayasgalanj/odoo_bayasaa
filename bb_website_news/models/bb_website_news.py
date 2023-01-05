# -*- coding: utf-8 -*-
from odoo import api, fields, models, tools, modules
import logging
_logger = logging.getLogger(__name__)

class BbWebsiteNews(models.Model):
    _name = 'bb.website.news'
    _inherit = ['mail.thread']
    _description = u'News board'
    _order = 'sequence'

    name = fields.Char('News')
    state = fields.Selection([('draft','Draft'),('done','Online')], 'State', default='draft', tracking=True)
    company_id = fields.Many2one('res.company', 'Company', default=lambda self:  self.env.user.company_id)
    user_ids = fields.Many2many('res.users', 'bb_website_user_rel', 'bb_id', 'user_id', u'View users')
    sequence = fields.Integer('Sequence', default=1)
    link = fields.Char('Link')
    
    def get_news(self):
        res = []
        try:
            res = self.env['bb.website.news'].search( [
                ('state','=','done')
                ,'|',('user_ids','=',False)
                ,('user_ids','in',[self.env.user.id])
                ]).mapped('name')
        except Exception as e:
            _logger.info('BbWebsiteNews %s'%(e))
        return res 

    def action_done(self):
        self.write({'state':'done'})

    def action_draft(self):
        self.write({'state':'draft'})
    
    def delete_line(self):
        self.user_ids = False
