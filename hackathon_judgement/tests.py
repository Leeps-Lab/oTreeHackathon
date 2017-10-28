import otree.api
from . import views
from .models import Constants


class PlayerBot(otree.api.Bot):

    def play_round(self):

        yield views.Instructions

        yield (
            views.Vote, {
                'best_overall_1': Constants.project_names[0],
                'best_overall_2': Constants.project_names[1],
                'best_overall_3': Constants.project_names[2],
                'best_overall_4': Constants.project_names[3],
                'best_overall_5': Constants.project_names[4],
                'best_design_1': Constants.project_names[0],
                'best_design_2': Constants.project_names[1],
                'best_design_3': Constants.project_names[2],
                'best_design_4': Constants.project_names[3],
                'best_design_5': Constants.project_names[4],
                'most_original_1': Constants.project_names[0],
                'most_original_2': Constants.project_names[1],
                'most_original_3': Constants.project_names[2],
                'most_original_4': Constants.project_names[3],
                'most_original_5': Constants.project_names[4],
        })

        assert self.group.best_overall == Constants.project_names[0]
        assert self.group.best_design == Constants.project_names[1]
        assert self.group.most_original == Constants.project_names[2]
        assert self.player.payoff == 6

        assert self.group.run_election({
            1: ['a', 'b', 'c'],
            2: ['d', 'a', 'b'],
            3: ['c', 'b', 'd'],
            4: ['d', 'f', 'a'],
            5: ['b', 'f', 'c'],
            6: ['a', 'b', 'c'],
        }) == 'd'

        assert self.group.run_election({
            1: ['bob', 'bill', 'sue'],
            2: ['sue', 'bob', 'bill'],
            3: ['sue', 'bob', 'bill'],
            4: ['bob', 'bill', 'sue'],
            5: ['sue', 'bob', 'bill'],
        }) == 'sue'