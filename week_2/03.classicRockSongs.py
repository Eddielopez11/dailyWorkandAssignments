import csv
import collections

classic_rock_header = []
classic_songs = []

with open('classic-rock-song-list.csv', 'rU', encoding='latin-1') as classic_rock_csv:
    csv_reader = csv.reader(classic_rock_csv)
    classic_rock_header = next(csv_reader)
    for row in csv_reader:
        classic_songs.append(row)


print(classic_rock_header)
print(len(classic_songs))
print(classic_rock_header[2])
print('-----')


spy = {}

for song in classic_songs:
    if not song[2]:
        continue
    elif song[2] in spy:
        spy[song[2]] += 1
    else:
        spy[song[2]] = 1

most_songs = 0
most_spy = None

for (yr, cnt) in spy.items():
    if cnt > most_songs:
        most_songs = cnt
        most_spy = yr

print('{yr} produced the most songs with {num} released that year.'.format(yr=most_spy,
 num=most_songs))
print('-----')

ams = {}

for artist in classic_songs:
    if not artist[1]:
        continue
    elif artist[1] in ams:
        ams[artist[1]] += 1
    else:
        ams[artist[1]] = 1

most_artist = 0
most_ams = None

for (art, numb) in ams.items():
    if numb > most_artist:
        most_artist = numb
        most_ams = art

print('{artist} had the most songs in the list with {numbsongs}.'.format(artist=most_ams, numbsongs=most_artist))
print('-----')

yms = {}

for song in classic_songs:
    if not song[2]:
        continue
    elif song[2] in yms:
        yms[song[2]].append(song[0])
    else:
        yms[song[2]] = [song[0]]

print(yms)
print('-----')

snames = {}
wpsn = []
nwpsn = []
z = "!@#$%^&*()-_=+[],./?;:''\""

for name in classic_songs:
    if z in name:
        name = name.replace(z, '')
        continue
    else:
        nwpsn.append([name])


print(nwpsn)
