# -*- coding: utf-8 -*-
from otree.api import models
from otree.constants import BaseConstants
from otree.models import BaseGroup, BasePlayer, BaseSubsession
from collections import defaultdict

doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'imperfect_monitoring'
    players_per_group = None
    num_rounds = 1
    project_names = [
        'foo',
        'bar',
        'baz',
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    best_overall = models.CharField(max_length=100, choices=Constants.project_names)
    best_design = models.CharField(max_length=100, choices=Constants.project_names)
    most_original = models.CharField(max_length=100, choices=Constants.project_names)

    def calculate_winners(self):
        votes = defaultdict(lambda: [])
        for player in self.get_players():
            for category in ['best_overall', 'best_design', 'most_original']:
                for rank in [1, 2, 3]:
                    vote = getattr(player, '{}_{}'.format(category, rank))
                    votes[player].append(vote)


class Player(BasePlayer):
    best_overall_1 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_2 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_3 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_1 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_2 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_3 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_1 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_2 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_3 = models.CharField(max_length=100, choices=Constants.project_names)

    def set_payoff(self):
        if self.id_in_group == 1:
            self.group.calculate_winners()

        self.payoff = 0
        for category in ['best_overall', 'best_design', 'most_original']:
            winner = getattr(self.group, category)
            if getattr(self, '{}_1'.format(category)) == winner:
                self.payoff += 3
            if getattr(self, '{}_2'.format(category)) == winner:
                self.payoff += 2
            if getattr(self, '{}_3'.format(category)) == winner:
                self.payoff += 1