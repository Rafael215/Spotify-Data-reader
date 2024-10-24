
!git clone https://github.com/ucsd-cse8a-ss22024/SpotifyGroupProject.git

!unzip SpotifyGroupProject/spotify_dataset.zip

fn = 'spotify_songs.csv'

fn

"""Part 1"""

f = open(fn)

#function will return dict of artist as key and int as value representing number of times that artists name appears in the data set
def artist_count():
  artist_dict = dict()
  for line in f:
    sep = line.split(',')
    if sep[9] == 'rap': #rap songs only
      if sep[2] in artist_dict: #initializing or continuing to add number of times and artist has appeared
        artist_dict[sep[2]] += 1
      else:
        artist_dict[sep[2]] = 1
  return artist_dict

artist_count()

f = open(fn)
#myList = list()

def readSpotify(filename):
  global myList #make names list global for future dict functions
  myList = list()
  f.readline() #skip 'titles'
  for line in filename:
     sep = line.split(',')
     if sep[9] == 'rap': #only grab rap genre stuff
      #print(sep[2])
      myList.append(sep[2])
  return myList

import plotly.graph_objects as go #imports the plotly graph objects and names it as go

#calls the fuction that returns a list of artists
data = readSpotify(f)

#Create histogram
fig = go.Figure(data = [go.Histogram(x = data)])

#layout
fig.update_layout(
    title = "Histogram Example",
    xaxis_title = "Artist Names",
    yaxis_title = "Frequency"
)

#show the graph
fig.show()

"""Part 2"""

f = open(fn)
def readSpotifyPopularity(filename):
  global popularity #make it global for future dict functions
  popularity = list()
  f.readline()
  for line in filename:
     sep = line.split(',')
     if sep[9] == 'rap':
      popularity.append(sep[3]) #only grab popularity nunbers on rap genre songs
  return popularity

readSpotifyPopularity(f)

f = open(fn)
def readSpotifyYear(filename):
  global year
  year = list()
  count = 0
  f.readline()
  for line in filename:
     sep = line.split(',')
     if sep[9] == 'rap':
      year.append(sep[6][0:4]) #splice for only the year and not the months of the year 2019-12-12 = 2019 only
  return year
readSpotifyYear(f)

# will take in two lists and find the average popularity of all songs per year
def year_average(yearL, popL):
  total_dict = dict()
  count_dict = dict()
  global avg_dict
  avg_dict = dict()
  for i in range(len(yearL)): #iterate through each year
    if yearL[i] in total_dict: #initialize or add to a dict counting the total popularity score and another dict with the number of times a song was from a certain year
      total_dict[yearL[i]] += int(popL[i])
      count_dict[yearL[i]] += 1
    else:
      total_dict[yearL[i]] = int(popL[i])
      count_dict[yearL[i]] = 1
  for i in total_dict: #put the data together into a new dict with the year as a key and the average
    avg_dict[i] = total_dict[i] / count_dict[i]
  return avg_dict

year_average(year, popularity)

import plotly.graph_objects as go
dictin = year_average(year, popularity) # ADD THE RETURN DICTIONARY HERE
datayears = list()
dataAvgTrack = list()

# Turns the dictionary into 2 lists for x and y vals
for key in dictin:
  datayears.append(key)
  dataAvgTrack.append(dictin[key])

# orders the lists together by year
count = 1
while count >= 1:
  count = 0
  for i in range(0, len(datayears)-1):
    if datayears[i] > datayears[i+1]:
      count += 1
      temp = datayears[i]
      datayears[i] = datayears[i+1]
      datayears[i+1] = temp
      temp = dataAvgTrack[i]
      dataAvgTrack[i] = dataAvgTrack[i+1]
      dataAvgTrack[i+1] = temp



# assign and test
print(datayears)
print(dataAvgTrack)

years = datayears
average = dataAvgTrack

# create scatter plot
scatter = go.Scatter(x = years, y = average, mode = "lines")
fig = go.Figure(data = scatter)

# layout
fig.update_layout(
    title = "Scatter Plot Example",
    xaxis_title = "Years",
    yaxis_title = "Average Track Popularity"
)
fig.show()
