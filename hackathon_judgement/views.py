# -*- coding: utf-8 -*-
from otree.views import Page, WaitPage
from . import models
import random


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

    def get_form(self, *args, **kwargs):
        best_overall_choices = list(models.Constants.project_names)
        random.shuffle(best_overall_choices)
        best_design_choices = list(models.Constants.project_names)
        random.shuffle(best_design_choices)
        most_original_choices = list(models.Constants.project_names)
        random.shuffle(most_original_choices)

        default = super().get_form(*args, **kwargs)
        for i in ['1', '2', '3']:
            default['best_overall_{}'.format(i)].field.choices = [(None, '---------')] + [(choice, choice) for choice in best_overall_choices]
            default['best_design_{}'.format(i)].field.choices = [(None, '---------')] + [(choice, choice) for choice in best_design_choices]
            default['most_original_{}'.format(i)].field.choices = [(None, '---------')] + [(choice, choice) for choice in most_original_choices]

        return default

    def error_message(self, values):
        errs = []
        if len(set([values['best_overall_1'], values['best_overall_2'], values['best_overall_3']])) != 3:
            errs.append('Best Overall must have 3 distinct values')
        if len(set([values['best_design_1'], values['best_design_2'], values['best_design_3']])) != 3:
            errs.append('Best Design must have 3 distinct values')
        if len(set([values['most_original_1'], values['most_original_2'], values['most_original_3']]))!= 3:
            errs.append('Most Original must have 3 distinct values')
        return errs


class WaitForVotes(WaitPage):
    def after_all_players_arrive(self):
        self.group.calculate_winners()


class Results(Page):
    
    def vars_for_template(self):
        self.player.set_payoff()
        return {}


page_sequence = [
    Instructions,
    Vote,
    WaitForVotes,
    Results
]