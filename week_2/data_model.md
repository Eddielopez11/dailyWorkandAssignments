# data_model.md

# question 1
i would make a library catalog as a dictionary so that it can have multiple
sections including a very important check-out/check-in
not completely sure how but something like:

library_books = {'checkout': ['harry potter and the sorcerer stone - sci1010' ,
'harry potter and the chamber of secrets - sci1011'] , 'checkin': [harry potter
and the prisoner of askaban - sci1012]}

checkout
del library_books['checkout'][0]
library_books['currently_checkout'] += ['*name of book*']

checkin
del library_books['checkin'][0] *or whatever position the book is currently in*
library_books['checkout'] += ['harry potter and the prisoner of askaban -
sci1012']

#question 2
coordinates = ['6,3' , '8,9' , '22,4' , '2,5']

#question 3
  *just a list for one persons many social media accounts*
socialmedia_profiles = {'facebook': 'eddieiscool', 'snapchat': 'eddiel93',
'instagram': 'eddiel209'}

  *for a social medias users*
socialmedia_users = {'eddie209'; 'id:123234', 'eddieiscool': 'id123789',
'eddiel93': 'id:456123'}

if there is a dicitonary, there would be unique usernames and just in case
there would be same usernames, they would all have unuque id's

#question 4
chessboard = {'occupied space': ['a2-pawn', 'b2-pawn', 'b1-knight']
'unocupied space': ['c3', 'c4', 'd4', 'f5']}

so there would be a grid with rows and columns listed with letters a-h, followed
by numbers 1-8. with a code that would "move" a listed item from occupied to
unocupied

#question 5

prison_inmates = ['joseph jay', 'steven still', 'jimmy john', 'tray tiger']
