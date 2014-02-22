from manager.models import Player
from manager.models import PlayerSkills
from manager.models import PlayerStats
from manager.models import PlayerType
from manager.models import Race
from manager.models import Skill
from manager.models import SkillCategory
from manager.models import Team
from manager.models import Coach
from django.contrib import admin

admin.site.register(Player)
admin.site.register(PlayerSkills)
admin.site.register(PlayerStats)
admin.site.register(PlayerType)
admin.site.register(Race)
admin.site.register(Skill)
admin.site.register(SkillCategory)
admin.site.register(Team)
admin.site.register(Coach)
