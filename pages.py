from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants

class  Risks(Page):
    form_model = 'player'
    form_fields = ['betting',
                   'gamble',
                   'carloan',
                   'blue_chip',
                   'speculative',
                   'treasury',
                   'failing',
                   'lending',
                   'spending',
                   'slotmachine',
                   'commission',
    ]



class CompanyInfo(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2


    form_model = 'player'
    form_fields = ['risk_prep',
                    'religion',
                   'prize_one',
                   'prize_two',
                   'best_desc',
                   'role',
                   'year_employed',
                    'total_employees',
                   'salary'

                    ]








class copattendance(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2

   # def error_message(self, values):
       # print('values is', values)
        #if values["year_compjoined'"] < values["year_compjoined"]:
         #   return 'It seems your company sent a representative before it joined the CoP. Please fix the error'

    form_model = 'player'
    form_fields = ['year_compjoined',
                   'month_compjoined' ,
                   'whenyear',
                   'whenmonth',
                   'copfreq',
                   'other_attendee',
                   'whynot_attend',
                   'network_member',
                   'whatsapp'
                   ]



class interactions(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
    form_model = 'player'
    form_fields = ['sun_member',
                   'sun_join',
                   'sun_year',
                   'sun_number',
                    'people_known',
                   'inter_people',
                   'interact_1',
                   'interact_2']

class assistance(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
    form_model = 'player'
    form_fields =['ta_applied',
                  'ta_granted',
                  'fa_applied',
                  'fa_granted']

class gain(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
    form_model ='player'
    form_fields =['gain_1',
                  'gain_2',
                  'gain_3',
                  ]

class moregain(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
    form_model ='player'
    form_fields =['learn',
                  'reason_attended',
                 'benefits',
                  'what_like',
                  'attendfuture',
                  'improve',
                  'otherimprove',
                  'ifimproved',

                 ]

class didyou(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2
    form_model ='player'
    form_fields =['inputs_purch',
                   'sale_prod',
                   'tech_supp',
                   'mentorship',
                   'mgt_prac',
                   'produc_tech']
class thanks(Page):
    def before_next_page(self):
        if self.request.POST.get('back'):
            if self.request.POST.get('back')[0] == '1':
                self._is_frozen = False
            self._index_in_pages -= 2
            self.participant._index_in_pages -= 2


page_sequence = [
    Risks, CompanyInfo, copattendance,  interactions, didyou,
     assistance, moregain, gain, thanks
]
