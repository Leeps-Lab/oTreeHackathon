# -*- coding: utf-8 -*-
from otree.api import models
from otree.constants import BaseConstants
from otree.models import BaseGroup, BasePlayer, BaseSubsession

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
    pass


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
        pass