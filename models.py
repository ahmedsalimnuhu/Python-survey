from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


import random

from django import forms

class Constants(BaseConstants):
    name_in_url = 'COP_Survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):


    network_member = models.StringField(
        choices=['Yes', 'No'],
        label  = '''Are you a member of another organization that promotes
         networking among professionals in your sector/field of work?''',
        widget = widgets.RadioSelect
    )

    whatsapp = models.StringField(
        choices=['Yes', 'No'],
        label = '''Do you belong to any WhatsApp group that consists of
         professionals/business owners in your sector/field of work?''',
        widget = widgets.RadioSelect
    )


    sun_member = models.StringField(
        choices= ['Yes', 'No'],
        label = '''Are you a member of the SUN Business Network''',

    )

    sun_join = models.StringField(
        choices=['I am a member', 'Yes', 'No', 'May be'],
        label = '''If you are not a member of the SUN Business Network, do you plan to join in future?
        '''
    )
    sun_year = models.StringField(
        choices=['2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 'I am not a member'],
        label='''
                       In which year did you join the SUN Business Network?
                       '''
    )


    sun_number = models.IntegerField(min=0, max=90,
        label='''
        How many people present today do you know from the SUN Business Network?
        '''
    )


    what_like = models.StringField(
        blank=True,
        label=''' What did you like about today's CoP meeting[select all that apply]''',
        widget =widgets.forms.CheckboxSelectMultiple(
            choices=[
                ['1', 'The topic of this meeting'], ['2', 'Presentations and discussion'],
                ['3', 'Interactions with other members'], ['4', 'Networking opportunity'],
                ['5', 'The Experiment'],
            ],
        )
    )

    attendfuture = models.IntegerField(min=0, max=100,
        label='''On a scale of 0[not likely] to 100[most likely], how likely
                    are you to attend future CoP meetings''',
        )


    improve = models.StringField(
        blank=True,
        label= ''' How can the Community of Practice (CoP) be improved [select all that apply]''',
        widget =widgets.forms.CheckboxSelectMultiple(
            choices =[
                ['1', 'Organize CoP meetings MORE frequently'], ['2', 'Organize CoP meetings LESS frequently'],
                ['3', 'Hold the CoP meeting for longer duration'], ['4', 'Hold the CoP meeting for SHORTER duration'],
                ['5', 'Organize the CoP meeting outside Nairobi'], ['6', 'Organize the CoP meeting at other more convenient location in Nairobi'],
                ['7', 'Organize the CoP meeting at other more convenient location INSIDE Nairobi'],
                ['8', 'Include more time for discussion'], ['9', 'Invite motivational speakers'],
                ['10', 'Provide copies of hand-outs and resources shared during the meeting'],
                ['11', 'Share list of meeting participants and their contact information '],
            ],
        )
    )

    otherimprove = models.StringField(
        label = '''You may suggest other ways of improving the CoP here. If not, please type NA '''
    )

    ifimproved = models.IntegerField(min=0, max=100,
        label='''If CoP meetings are improved as suggested above, how likely
         are you to attend future CoP meetings (using the same scale 0=not
          likely at all and 100=most likely)? '''

    )

    prize_one = models.IntegerField(
    label = ''' Suppose you have won a prize of 1,000,000KSH that you can claim
     immediately. However, you also have the option of waiting one YEAR to claim
      the prize. If you wait, you will receive more than 1,000,000 KSH. What is the 
      smallest amount of money in addition to the 1,000,000 KSH you would will like 
      to receive ONE YEAR from now to convince you to wait rather than claim the 
      prize now? Enter the number without comma(,)'''
    )

    prize_two = models.IntegerField(
        label = '''Now suppose you have won a prize of 1,000,000 KSH that you can 
        claim immediately or wait one MONTH to claim. If you wait, you will 
        receive more than 1,000,000 KSH. What is the smallest amount of
         money in addition to the 1,000,000 KSH you would have to receive one 
         MONTH from now to convince you to wait rather than claim the prize now?
        Enter the number without comma(,)'''
    )


    best_desc = models.StringField(
             choices=['Food processor and producer', 'Food processing input supplier',
             'Agricultural input supplier', 'Consulting and advising', 'Non-governmental not-for profit organization',
             'Investment company', 'Government representative' , 'Donor organization/Donor funded project',
             'Business and trade organization', 'Producer organization'],
             label= ''' Which of the following best describes type of your company / organization? ''',
             widget=widgets.RadioSelect
    )

    role = models.StringField(
        choices= ['Owner', 'Manager', 'Full-time Employee', 'Part-time Employee', 'Just a friend representing the manager/owner',
                  'Just a family member representing the owner/manager', 'Intern', 'Other (None of the above)'],
        label = 'What is your role in the company/organization you are representing today?',
        widget = widgets.RadioSelect

    )





    year_employed =  models.IntegerField(min=1950, max= 2019,
                  label = '''
                  In which year did you start working with this company or organization? If you're the owner, 
                  in which year did you establish this company? [Please indicate years in YYYY]
                  '''
    )

    total_employees = models.IntegerField(min=0,
                    label = '''Approximately how many employees does your company or organization have?'''

    )

    lab_exp = models.StringField(
            choices =['Yes', 'No'],
            label = 'Have you ever taken part in an economics or any social experiment?',
            widget = widgets.RadioSelect
    )

    salary = models.StringField(
           choices = ['Below 10,000', '11,000 to 20,000', '21,000 to 40,000', '41,000 to 60,000', '61,000 to 100,00', 'Above 100,000'],
           label ='Which of the following best describes the range of your monthly income in KSH',
           widget = widgets.RadioSelect
    )

    year_compjoined = models.StringField(
                    choices=['I am not a COP member', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 'I don`t know'],
                    label= '''
                    In which year did your business join the CoP. That is the year in which your company first
                     sent a represenative  to the CoP meeting.
                    '''
    )

    month_compjoined = models.StringField(
                    choices=['I am not a COP member', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December', 'Don`t know'],
                     label= '''
                        In which month did your business join the CoP. That is the month in which your company first
                         sent a representative to the CoP meeting.
                        '''
    )


    other_attendee = models.StringField(
                   choices=['Yes', 'No'],
                   label = 'Is anyone else from your company/organization attending this CoP meeting today',
                   widget = widgets.RadioSelect
    )

    first_time = models.StringField(
               choices =['Yes', 'No'],
               label= 'As an individual, is this your first time of attending a CoP meeting?',
               widget = widgets.RadioSelect
    )

    whenyear = models.StringField(
                choices=['This is my first time', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 'I don`t know'],
                label=''' If this is not the first time you are attending the CoP, in which year did you (as a person) first attend a CoP meeting?
                    '''
    )

    whenmonth = models.StringField(
        choices=['This is my first time', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
                 'September', 'October', 'November', 'December', 'Don`t know'],
        label=''' If this is not the first time you are attending the CoP, in which month did you  (as a person) first attend a CoP meeting?
                       '''
    )



    copfreq = models.IntegerField(min=0, max=60,
            label = '''
        How many CoP meetings have you attended so far including today's meeting?
        '''
    )

    whynot_attend= models.StringField(
        blank=True,
        label=''' Why have you not attended any CoP meeting in the past? [Select all that apply]''',
        widget=widgets.forms.CheckboxSelectMultiple(
            choices=[
               ['1', 'I have attended all past CoP meetings'],  ['2', 'Was not a member of CoP prior to this meeting'], ['3', 'Was not aware of any prior CoP meetings'],
                ['4', 'Time/day/location of the CoP meetings were not convenient'], ['5', 'Was not interested in the topics of previous CoP meetings'],
                ['6', 'No time to attend (I was very busy)'],  ['7', 'Did not see any value/benefit for me to attend CoP meetings '],['8', 'I am not a CoP member'], ['9', 'Other'],
            ],
        )
    )



    people_known = models.IntegerField(min=0, max=80,
                 label = '''
                 Approximately how many people at today's CoP meeting did you
                  know before today's meeting? (Please do not count people from your own 
                  company or organization who may be attending this meeting)
                 '''
    )



    inter_people = models.IntegerField(min=0, max=80,
                 label='''
                     Approximately how many people at today's CoP meeting did you
                      interact with? 
                     '''
    )




    interact_1 = models.StringField(
               choices= ['I didn`t know anyone before this meeting', 'Daily', 'At least once a week', '2-3 times a month',
                         'At least once a quarter', 'At least once every 6 months',
                          'At least once a year', 'Less frequently than every year',
                          'Never'],
               label= '''Think of one person (who is not from your company/organization) present at today’s CoP meeting whom you knew
                the most before today’s meeting.  How regularly do you interact with this person in a professional setting? ''',
               widget = widgets.RadioSelect
    )

    interact_2 = models.StringField(
               choices=['I didnt know anyone before this meeting', 'Daily', 'At least once a week', '2-3 times a month',
                'At least once a quarter', 'At least once every 6 months',
                 'At least once a year', 'Less frequently than every year',
                 'Never'],

               label=  '''How regularly do you interact with this person in a social setting''',
               widget = widgets.RadioSelect
    )


    ta_applied = models.StringField(
              choices=['Yes', 'No', 'Dont Know', 'Not Applicable'],
              label ='''
            Has your company ever APPLIED for technical assistance from GAIN?
            ''',
              widget = widgets.RadioSelect
    )

    ta_granted = models.StringField(
               choices=['Yes', 'No', 'Dont Know', 'Not Applicable'],
               label = '''
               Has your company ever RECEIVED technical assistance from GAIN?
               ''',
               widget = widgets.RadioSelect
    )
    fa_applied = models.StringField(
               choices=['Yes', 'No', 'Dont Know', 'Not Applicable'],
               label='''
                   Has your company ever APPLIED for financial assistance from GAIN?
                   ''',
               widget=widgets.RadioSelect
    )

    fa_granted = models.StringField(
              choices=['Yes', 'No', 'Dont Know', 'Not Applicable'],
              label='''
                   Has your company ever RECEIVED financial assistance from GAIN?
                   ''',
              widget=widgets.RadioSelect
    )

    inputs_purch = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable'],
               label = ''' 
               Have you ever purchased inputs from any person/business you met through the CoP? 
               ''',
               widget = widgets.RadioSelect
    )

    sale_prod = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable'],
               label = ''' 
               Have you ever sold products (inputs or output) to any person/business you met through 
                the CoP? 
                ''',
               widget = widgets.RadioSelect
    )

    tech_supp = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable'],
               label = ''' 
               Have you ever provided technical support, consulting or business advising to any person/business you met through the CoP? 
                ''',
               widget = widgets.RadioSelect
    )

    mentorship = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable/Not a member'],
               label = ''' 
               Have you ever provided mentorship to any person/business you met through the CoP? 
                   ''',
               widget = widgets.RadioSelect
    )

    mgt_prac = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable/Not a member'],
               label = '''
                
                Have you learned any new business management practices from a person/business you met through the CoP? ''',
               widget = widgets.RadioSelect
    )

    produc_tech = models.StringField(
               choices = ['Yes', 'No', 'Not Applicable/Not a member'],
               label = ''' Have you learned any new production practices from a person/business you met through the CoP? ''',
               widget = widgets.RadioSelect
    )

    gain_1 = models.StringField(
           choices=['Not at all', 'A little', 'Some', 'A lot'],
           label=''' How much do you know about the mission of GAIN? ''',
           widget=widgets.RadioSelect
    )

    gain_2 = models.StringField(
           choices= ['Not at all', 'A little', 'Some', 'A lot'],
           label= ''' How much do you know about the purpose of GAIN? ''',
           widget =  widgets.RadioSelect
    )

    gain_3 = models.StringField(
           choices=['Not at all', 'A little', 'Some', 'A lot'],
           label=''' How much do you know about the topic of today's meeting? ''',
           widget=widgets.RadioSelect
    )

    learn = models.StringField(
          choices=['Friend or colleague from another organization','Social media', 'GAIN Website', 'GAIN Newsletter, brochure or other printed materials',
                 'Newspaper or radio', 'Through another GAIN event', 'Through another event not organized by GAIN'],
          label=''' How did you first learn about the Community of Practice ? ''',
          widget=widgets.RadioSelect
    )

    other_org = models.StringField(
              choices=['Yes', 'No'],
              label=''' Are you a member of another organization that promotes networking
         among professionals in your sector/field of work? ''',
              widget=widgets.RadioSelect
    )



    reason_attended = models.StringField(
        blank = True,
        label = ''' What are the reasons for your participation at today's CoP event? [Select all that apply]''',
        widget=widgets.forms.CheckboxSelectMultiple(
        choices=[
            ['1', 'Training opportunity'], ['2', 'Networking'],  ['3', 'Learning opportunity'],
                ['4', 'New product ideas'], ['5', 'New business/investment ideas'], ['6', 'Funding opportunity'],
                 ['7', 'Mentorship'],
                ],
            )
        )

    benefits = models.StringField(
        blank = True,
        label = ''' Have you or your company/organization benefited from GAIN’s Community of Practice
         through any of the following: (select all that apply) ''',
        widget = widgets.forms.CheckboxSelectMultiple(
        choices =[
            ['1', 'New product development'], ['2', 'Expansion of market for existing products'],
               ['3', 'New grant funding opportunity'], ['4', 'Improvements in our technical knowledge/capacity'],
                 ['5', 'New business/investment ideas'], ['6', 'Have not benefited yet'],
                ],
        )

    )

    other_ben = models.StringField(
        label = '''
        Specify if other. Write 'NA' if none. 
        '''

    )

    risk_prep = models.StringField(
        choices = ['Fully prepared to take risks', 'I try to avoid taking risks'],
        label = '''
        How do you see yourself when it comes to taking risks?
        ''',
        widget= widgets.RadioSelect

    )

    religion = models.StringField(
        choices=['Very important', 'Important', 'Not so important', 'Not important at all', 'I do not belong to any faith/Not Applicable' ],
        label='''
           In your daily activities, how important is your religion/faith to you? 
           ''',
        widget=widgets.RadioSelect

    )

    betting = models.IntegerField(min=1, max=5,
        label = ''' Bet a day's income at the horse races (Similar to sports betting) ''')

    gamble = models.IntegerField(min=1, max=5,
        label = ''' 
            GAMBLE A MONTH'S INCOME at a CASINO?
            '''
    )

    carloan = models.IntegerField(min=1, max=5,
                                  label=''' 
            Co-sign A CAR LOAN FOR A FRIEND?
            '''
    )

    blue_chip= models.IntegerField(min=1, max=5,
        label = '''Invest 10% of your annual income in a BLUE CHIP STOCK (a stock
        with a long and good reputation of yielding good returns. An example is Safaricom stock) '''

        )

    speculative = models.IntegerField(min=1, max=5,
        label= ''' Invest 10% of your annual income in a VERY SPECULATIVE STOCK 
        (stock whose returns are not predictable. An example is Uchumi Supermarket stocks ) '''
        )

    treasury = models.IntegerField(min=0, max=10,
        label=''' 
             Invest 10% of your annual income in GOVERNMENT BONDS? (Also known as TREASURY BILLS. An example is
             M-Kiba)
            ''',
    )

    failing = models.IntegerField(min=1, max=5,
        label=''' Invest in a business that has a GOOD CHANCE of FAILING '''
    )

    lending = models.IntegerField(min=1, max=5,
        label= '''Lend A FRIEND an amount of money EQUIVALENT TO ONE MONTH'S INCOME''')

    spending = models.IntegerField(min=1, max=5,
        label= '''Spend MONEY impulsively without thinking about the consequences''')

    slotmachine = models.IntegerField(min=1, max=5,
            label ='''Take a day's income to play the SLOT MACHINE at a CASINO (An example is the
            Chinese slot machine)''')

    commission = models.IntegerField(min=1, max=5,
            label = '''Take a JOB where you get paid EXCLUSIVELY ON COMMISSION BASIS''')








