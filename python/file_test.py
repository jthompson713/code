liked_songs = {
  'title': 'artist'
}

def write_liked_songs_to_file(liked_songs):
  file = open('liked_songs.txt', 'w')
  file.write('Bad Habits by Ed Sheeran\n')
  file.write('I\'m Just Ken by Ryan Gosling\n')
  file.write('Mastermind by Taylor Swift\n')
  file.write('Uptown Funk by Mark Ronson ft. Bruno Mars\n')
  file.write('Ghost by Justin Bieber\n')
  file.close()

write_liked_songs_to_file(liked_songs)
  