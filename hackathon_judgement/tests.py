import otree.api
from . import views


class PlayerBot(otree.api.Bot):

    def play_round(self):

        yield views.Instructions

        yield (
            views.Vote, {
                'best_overall_1': 'project_1',
                'best_overall_2': 'project_2',
                'best_overall_3': 'project_3',
                'best_design_1': 'project_2',
                'best_design_2': 'project_1',
                'best_design_3': 'project_3',
                'most_original_1': 'project_3',
                'most_original_2': 'project_1',
                'most_original_3': 'project_2',
        })

        yield views.Results

        assert self.group.best_overall == 'project_1'
        assert self.group.best_design == 'project_2'
        assert self.group.most_original == 'project_3'
        assert self.player.payoff == 9

        assert self.group.run_election({
            1: ['project_2'],
        }) == 'project_1'