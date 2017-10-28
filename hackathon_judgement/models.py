# -*- coding: utf-8 -*-
from otree.api import models
from otree.constants import BaseConstants
from otree.models import BaseGroup, BasePlayer, BaseSubsession
from collections import defaultdict
import itertools

import math

doc = """
"""


class Constants(BaseConstants):
    name_in_url = 'hackathon_judgement'
    players_per_group = None
    num_rounds = 1
    project_names = [
        'project_1',
        'project_2',
        'project_3',
        'project_4',
        'project_5',
        'project_6',
        'project_7',
        'project_8',
    ]


class Subsession(BaseSubsession):

    def creating_session(self):
        self.group_randomly()


class Group(BaseGroup):
    best_overall = models.CharField(max_length=100, choices=Constants.project_names)
    best_design = models.CharField(max_length=100, choices=Constants.project_names)
    most_original = models.CharField(max_length=100, choices=Constants.project_names)

    def calculate_winners(self):
        votes_by_player = defaultdict(lambda: defaultdict(lambda: []))
        for player in self.get_players():
            for category in ['best_overall', 'best_design', 'most_original']:
                for rank in [1, 2, 3, 4, 5]:
                    vote = getattr(player, '{}_{}'.format(category, rank))
                    votes_by_player[category][player].append(vote)

        self.best_overall = self.run_election(votes_by_player['best_overall'])
        for player in self.get_players():
            for player in votes_by_player['best_design'].keys():
                if self.best_overall in votes_by_player['best_design'][player]:
                    votes_by_player['best_design'][player].remove(self.best_overall)
        self.best_design = self.run_election(votes_by_player['best_design'])
        for player in self.get_players():
            for player in votes_by_player['most_original'].keys():
                if self.best_overall in votes_by_player['most_original'][player]:
                    votes_by_player['most_original'][player].remove(self.best_overall)
                if self.best_design in votes_by_player['most_original'][player]:
                    votes_by_player['most_original'][player].remove(self.best_design)
        self.most_original = self.run_election(votes_by_player['most_original'])

    def run_election(self, votes):
        num_voters = len(votes.keys())
        plurality = math.ceil(num_voters / 2)
        candidates = set(itertools.chain(*votes.values()))

        votes_by_candidate = {
            candidate: sum([1 for ranks in votes.values() if candidate == ranks[0]])
            for candidate in candidates
        }

        for candidate in candidates:
            count = votes_by_candidate[candidate]
            if count >= plurality:
                return candidate

        candidates_by_vote = sorted([
            (count, candidate)
            for (candidate, count) in votes_by_candidate.items()
        ], key=lambda i: i[0], reverse=True)

        top_two = set([candidate for count, candidate in candidates_by_vote[0:2]])

        for ranks in votes.values():
            for dropout in candidates - top_two:
                if dropout in ranks:
                    ranks.remove(dropout)

        for voter in list(votes.keys()):
            if not votes[voter]:
                del votes[voter]

        candidates = top_two

        votes_by_candidate = {
            candidate: sum([1 for ranks in votes.values() if candidate == ranks[0]])
            for candidate in candidates
        }

        candidates_by_vote = sorted([
            (count, candidate)
            for (candidate, count) in votes_by_candidate.items()
        ], key=lambda i: i[0], reverse=True)

        return candidates_by_vote[0][1]


class Player(BasePlayer):
    best_overall_1 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_2 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_3 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_4 = models.CharField(max_length=100, choices=Constants.project_names)
    best_overall_5 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_1 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_2 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_3 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_4 = models.CharField(max_length=100, choices=Constants.project_names)
    best_design_5 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_1 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_2 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_3 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_4 = models.CharField(max_length=100, choices=Constants.project_names)
    most_original_5 = models.CharField(max_length=100, choices=Constants.project_names)

    def set_payoff(self):
        self.payoff = 0
        for category in ['best_overall', 'best_design', 'most_original']:
            winner = getattr(self.group, category)
            if getattr(self, '{}_1'.format(category)) == winner:
                self.payoff += 3
            if getattr(self, '{}_2'.format(category)) == winner:
                self.payoff += 2
            if getattr(self, '{}_3'.format(category)) == winner:
                self.payoff += 1