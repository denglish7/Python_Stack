from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	context = {
		"baseball": League.objects.filter(sport="Baseball"),
		"women": League.objects.filter(name__contains="Womens'"),
		"hockey": League.objects.filter(sport__contains="Hockey"),
		"not_football": League.objects.exclude(sport="Football"),
		"conferences": League.objects.filter(name__contains="Conference"),
		"atlantic": League.objects.filter(name__contains="Atlantic"),
		"Dallas": Team.objects.filter(location="Dallas"),
		"Raptors": Team.objects.filter(team_name="Raptors"),
		"City": Team.objects.filter(location__contains="City"),
		"starts_with_T": Team.objects.filter(team_name__startswith="T"),
		"teamsAZ": Team.objects.order_by('location'),
		"teamsZA": Team.objects.order_by('-team_name'),
		"cooper": Player.objects.filter(last_name="Cooper"),
		"joshua": Player.objects.filter(first_name="Joshua"),
		"cooper_no_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"alexander_or_wyatt": Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt"),
		"ASC": Team.objects.filter(league__name="Atlantic Soccer Conference"),
		"BPplayers": Player.objects.filter(curr_team__team_name="Penguins", curr_team__location="Boston"),
		# "players": Player.objects.filter(curr_team__league__name = 'International Collegiate Baseball Conference'),
		# "players":Player.objects.filter(curr_team__league__name='American Conference of Amateur Football', last_name='Lopez')
					# Player.objects.filter(curr_team__league__sport="Football"),
					# Team.objects.filter(curr_players__first_name="Sophia"),
					# League.objects.filter(teams__curr_players__first_name="Sophia"),
					# Player.objects.filter(last_name="Anderson").exclude(curr_team__location="Phoenix", curr_team__team_name="Rays"),

# Team.objects.filter(all_players__first_name = "Samuel", all_players__last_name="Evans")
# Player.objects.filter(all_teams__location="Manitoba", all_teams__team_name="Tiger-Cats"),
# Player.objects.filter(all_teams__location="Wichita").exclude(curr_team__location="Wichita")
# Team.objects.filter(all_players__first_name="Jacob", all_players__last_name="Gray").exclude(location="Oregon")
# Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
# Team.objects.annotate(num_players=Count('all_players')).filter(num_players__gte=12),
# Player.objects.annotate(num_teams=Count('all_teams')).order_by('num_teams'),
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),


	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")
