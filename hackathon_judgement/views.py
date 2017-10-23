# -*- coding: utf-8 -*-
from otree.views import Page
from . import models


class Instructions(Page):
    pass


class Vote(Page):

    form_model = models.Player
    form_fields = [
        'best_overall_1',
        'best_overall_2',
        'best_overall_3',
        'best_design_1',
        'best_design_2',
        'best_design_3',
        'most_original_1',
        'most_original_2',
        'most_original_3',
    ]

    def error_message(self, values):
        errs = []
        if len(set([values['best_overall_1'], values['best_overall_2'], values['best_overall_3']])) != 3:
            errs.append('Best Overall must have 3 distinct values')
        if len(set([values['best_design_1'], values['best_design_2'], values['best_design_3']])) != 3:
            errs.append('Best Design must have 3 distinct values')
        if len(set([values['most_original_1'], values['most_original_2'], values['most_original_3']]))!= 3:
            errs.append('Most Original must have 3 distinct values')
        return errs


class Results(Page):

    def vars_for_template(self):
        self.player.set_payoff()
        return {}


page_sequence = [
    Instructions,
    Vote,
    Results
]