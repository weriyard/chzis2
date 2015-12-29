from chzis.mainpage.views import Index
from chzis.congregation.views import CongregationMembers

urls = [
('/', Index),
('/congregation', CongregationMembers)

]