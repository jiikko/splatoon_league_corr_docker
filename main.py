# -*- coding: utf-8 -*-

import splatoon_league_corr
import unittest

class BasicTestSuite(unittest.TestCase):
	"""calc_corr_number_of_games sample cases."""
	player = splatoon_league_corr.ika_data('e47935e347b60719','自分','plater')
	friend1 = splatoon_league_corr.ika_data('fcf07623cc12acb0','うっぽ','friend1')
	friend2 = splatoon_league_corr.ika_data('851d5ca015bdcb58','chanpon','friend2')
	friend3 = splatoon_league_corr.ika_data('fc7de84f3bfc13c9','sher','friend3')
	myteam = splatoon_league_corr.team_data(player,friend1,friend2,friend3)
	splatoon_league_corr.calc_corr_number_of_games('ikaWidgetCSV_x.tcsv', 'output', myteam, 50)
	
	def test_absolute_truth_and_meaning(self):
		assert True

if __name__ == '__main__':
	unittest.main()
