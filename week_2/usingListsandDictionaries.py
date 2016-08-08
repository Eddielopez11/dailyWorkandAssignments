# coding: utf-8
friends = ['pablo' , 'lili' , 'yesi' , 'cheetos' , 'omar' , 'vivi' , 'jasmin']
us_states = ['Texas' , 'Oklahoma' , 'Nevada' , 'Arizona' , 'California']
population_zip = {78207: '56,348', 78225: '13,553', 78201: '47,387', 78237: '36,273']
population_zip = {78207: '56,348', 78225: '13,553', 78201: '47,387', 78237: '36,273'}]
population_zip = {'78207': '56,348', '78225': '13,553', '78201': '47,387', '78237': '36,273'}
population_zip_year = {78207_2016: '56,348', 78207_2010: '50,348', 78207_2000: '49,348', 78225_2016: '13,553', 78225_2010: '11,553', 78225_2000: '9,553', 78201_2016: '47,387', 78201_2010: '42,387', 78201_2000: '39,387', 78237_2016: '36,273', 78237_2010: '34,273', 78237_2000: '29,273'}
population_zip_year = {78207-2016: '56,348', 78207-2010: '50,348', 78207-2000: '49,348', 78225-2016: '13,553', 78225-2010: '11,553', 78225-2000: '9,553', 78201-2016: '47,387', 78201-2010: '42,387', 78201-2000: '39,387', 78237-2016: '36,273', 78237-2010: '34,273', 78237-2000: '29,273'}
#changed to string because of math
# use quotes on numbers instead of str() because str will still do math
# and output the answer as a string
population_zip_year = {'78207-2016': '56,348', '78207-2010': '50,348', '78207-2000': '49,348', '78225-2016': '13,553', '78225-2010': '11,553', '78225-2000': '9,553', '78201-2016': '47,387', '78201-2010': '42,387', '78201-2000': '39,387', '78237-2016': '36,273', '78237-2010': '34,273', '78237-2000': '29,273'}
todays_date = "August 8, 2016"
get_ipython().magic('save usingListsandDictionaries 1-9')

# 6. I used first names only. I can see how that would be a problem though
#    as stated in the question, bigger lists would have duplicate names
#    and that wouldn't be any good. so maybe with full names that wont happen
#    as much. as for same full names, baybe just date of birth?

#7. I used the full name of the states because its easier to know what
#   exactly someone would be talking about without looking it up.
#   if i needed to model both, i would add a dictionaty and instead use their
#   abreiviations (us_states{TX: 'Texas'}) I personally dont know which two
#   letters are for what state so i would do it like that, so of course i would
#   have to look them up but anyone else viewing it would refer to the dict i
#   would have added

#8. I used integer but as you stated, and as we saw when entering the code
#   for that, it was literally subtracting the dates from the year, so im
#   going with string instead.

#9. I used integers as i had in question number 8, but as i saw python literally
#   uses it as math with dashes and other symbols, so i changed it

#10. I used August 8, 2016 just because its easy to read. I definetly see the
#   benefits of 2016-08-08 because if everyone used the standard, then everyone
#   would ilstantly recognize that date.
