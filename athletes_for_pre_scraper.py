


def give_just_athletes(uncleaned_list):
  raw = uncleaned_list
  print('print raw', raw)
  just_athletes = []
  beginning_index = 0
  end_index = 0
  for row in raw:
    row.strip(",")
  for row in raw:
    if row == " ":
      raw.remove(row)
  for row in raw:
    if "Name" in row:
      beginning_index = raw.index(row) + 2
    elif 'NAME' in row:
      beginning_index = raw.index(row) + 2
    elif 'TEAM SCORES' in row:
      end_index = raw.index(row) - 1
    elif "Team Scores" in row:
      end_index = raw.index(row) - 1
    else: 
      None
  if end_index < beginning_index:
    for row in raw:
      if raw.index(row) >= beginning_index:
        just_athletes.append(row)
  else:
    for row in raw:
      if raw.index(row) >= beginning_index and raw.index(row) <= end_index:
        just_athletes.append(row)
      else:
        None
  for row in just_athletes:
    print(len(row))
    
  # ONLY COMMENT IN IF JUST ATHLETES IS NOT UNIFORM
  if len(just_athletes[-1]) < len(just_athletes[20]):
    just_athletes.remove(just_athletes[-1])
  # ONLY COMMENT IN IF STRANGE ERROR AT END
  # fix = ''
  # for row in just_athletes:
  #   if len(row) < 30:
  #     fix = row
  # just_athletes.remove(just_athletes[-1])
  # print(fix, just_athletes[-1])
  # just_athletes[-1] = just_athletes[-1] + fix
  return just_athletes

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def split(word):
    return [char for char in word]

def give_athletes(sample):
  sample = sample
  just_athletes = give_just_athletes(sample)
  print('just athletes: ')
  one_row_to_list = []
  for row in just_athletes:
    new_athlete = []
    place = ''
    name = ''
    age = ''
    school_list = []
    school = ''
    race_time = ''
    school_place = ''
    split = row.split()
    for i in split:
      if "#" in i:
        split.remove(i)
    if is_number(split[1]) == True:
      split.remove(split[1])
    print(split)
    if split == []:
      break
    print(split[0])
    avg_mile_index = 4
    place = split[0]
    name = split[1] + " " + split[2]
    age = split[3]
    for i in split[4:]:
      if '1' in i:
        None
      elif '2' in i:
        None
      elif '3' in i:
        None
      elif '4' in i:
        None
      elif '5' in i:
        None
      elif '6' in i:
        None
      elif '7' in i:
        None
      elif '8' in i:
        None
      elif '9' in i:
        None
      else:
        school_list.append(i)
        avg_mile_index += 1
    for i in school_list:
      school = school + i + ' '
    race_time = split[avg_mile_index + 1]
    try: school_place = split[avg_mile_index + 2]
    except IndexError:
      None
    new_athlete.append(place)
    new_athlete.append(name)
    new_athlete.append(age)
    new_athlete.append(school)
    new_athlete.append(race_time)
    new_athlete.append(school_place)
    one_row_to_list.append(new_athlete)
  for row in one_row_to_list:
    print(row)
  return one_row_to_list



