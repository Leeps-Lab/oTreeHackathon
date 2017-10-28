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
        'best_overall_4',
        'best_overall_5',
        'best_design_1',
        'best_design_2',
        'best_design_3',
        'best_design_4',
        'best_design_5',
        'most_original_1',
        'most_original_2',
        'most_original_3',
        'most_original_4',
        'most_original_5',
    ]

    def best_overall_1_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_overall_2_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices
    
    def best_overall_3_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_overall_4_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_overall_5_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_design_1_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_design_2_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_design_3_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_design_4_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def best_design_5_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def most_original_1_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def most_original_2_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def most_original_3_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def most_original_4_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def most_original_5_choices(self):
        random.seed(self.participant.code)
        choices = list(models.Constants.project_names)
        random.shuffle(choices)
        return choices

    def error_message(self, values):
        errs = []
        for category in ['best_overall', 'best_design', 'most_original']:
            distinct = set([
                values['{}_{}'.format(category, rank)]
                for rank in [1, 2, 3, 4, 5]
            ])
            if len(distinct) != 5:
                errs.append('{} must have 5 distinct values'.format(' '.join(category.split('_')).title()))
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