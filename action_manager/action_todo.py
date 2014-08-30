# -*- coding: utf-8 -*-
from openerp import models, fields


class ActionTodo(models.Model):
    _name = 'action.todo'
    name = fields.Char('Title', required=True)
    active = fields.Boolean('Active?', default=True)
