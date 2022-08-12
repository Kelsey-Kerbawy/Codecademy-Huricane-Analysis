# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages : list):
    
    damages_updated = []
    for damage in damages:
        if damage == "Damages not recorded":
            damages_updated.append(damage)
        elif "M" in damage:
            damage = damage.strip("M")
            damage = float(damage)*1000000
            damages_updated.append(damage)
        elif "B" in damage:
            damage = damage.strip("B")
            damage = float(damage)*1000000000
            damages_updated.append(damage)
    
    return damages_updated

updated_damages = update_damages(damages)

# write your construct hurricane dictionary function here:
def dct_from_data(names:list,months:list,years:list,max_sustained_winds:list,areas_affected:list,damages:list,deaths:list):
    hurricane_dct = {}
    for ind in range(0,len(names)-1):
        hurricane_dct[names[ind]] = {
            'Name': names[ind],
            'Month': months[ind],
            'Year': years[ind],
            'Max Sustainted Wind': max_sustained_winds[ind],
            'Areas Affected': areas_affected[ind],
            'Damage': damages[ind],
            'Deaths': deaths[ind]
        }
    return hurricane_dct

hurricane_dct = dct_from_data(names,months,years,max_sustained_winds,areas_affected,updated_damages,deaths)
#print(hurricane_dct)



# write your construct hurricane by year dictionary function here:
def year_dct(hurricane_dct: dict):
  hurricanes_by_year= dict()
  for cane in hurricane_dct:
      current_year = hurricane_dct[cane]['Year']
      current_cane = hurricane_dct[cane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_cane]
      else:
          hurricanes_by_year[current_year].append(current_cane)
  return hurricanes_by_year

hurricanes_by_year = year_dct(hurricane_dct)
#print(hurricanes_by_year)


# write your count affected areas function here:
def count_affected_areas(hurricane_dct: dict):
    
    affected_areas = {}
    for cane in hurricane_dct:
        for area_affected in hurricane_dct[cane]['Areas Affected']:
            if area_affected not in affected_areas.keys():
                affected_areas[area_affected] = 1
            else:
                affected_areas[area_affected] += 1
    
    return affected_areas

affected_areas = count_affected_areas(hurricane_dct)
#print(affected_areas)


# write your find most affected area function here:
def find_max_area(affected_areas_dct : dict):
    max_area = 'Central America'
    max_area_count = 0
    for area in affected_areas_dct:
        if affected_areas_dct[area] > max_area_count:
            max_area_count = affected_areas_dct[area]
            max_area = area
    return max_area +": "+str(max_area_count)

max_area = find_max_area(affected_areas)
#print(max_area)


# write your greatest number of deaths function here:
def find_greatest_deaths(hurricane_dct : dict):    
    greatest_deaths = ''
    greatest_deaths_count = 0
    for cane in hurricane_dct:
        if hurricane_dct[cane]['Deaths'] > greatest_deaths_count:
            greatest_deaths_count = hurricane_dct[cane]['Deaths']
            greatest_deaths = hurricane_dct[cane]['Name']
    return "Greatest deaths " + greatest_deaths + ": " + str(greatest_deaths_count)

greatest_deaths = find_greatest_deaths(hurricane_dct)
#print(greatest_deaths)


# write your catgeorize by mortality function here:
def categorize_by_mortality(hurricane_dct:dict):
  mortality_scale = {0: 0,
                 1: 100,
                 2: 500,
                 3: 1000,
                 4: 10000}

  hurricanes_mortality = {0:[],1:[],2:[],3:[],4:[],5:[]}

  for cane in hurricane_dct:
    num_deaths = hurricane_dct[cane]['Deaths']
    if num_deaths == mortality_scale[0]:
      hurricanes_mortality[0].append(hurricane_dct[cane])
    elif num_deaths > mortality_scale[0] and num_deaths <= mortality_scale[1]:
      hurricanes_mortality[1].append(hurricane_dct[cane])
    elif num_deaths > mortality_scale[1] and num_deaths <= mortality_scale[2]:
      hurricanes_mortality[2].append(hurricane_dct[cane])
    elif num_deaths > mortality_scale[2] and num_deaths <= mortality_scale[3]:
      hurricanes_mortality[3].append(hurricane_dct[cane])
    elif num_deaths > mortality_scale[3] and num_deaths <= mortality_scale[4]:
      hurricanes_mortality[4].append(hurricane_dct[cane])
    elif num_deaths > mortality_scale[4]:
      hurricanes_mortality[5].append(hurricane_dct[cane])
  return hurricanes_mortality

hurricanes_mortality = categorize_by_mortality(hurricane_dct)
#print(hurricanes_mortality)


# write your greatest damage function here:
def find_greatest_damage(hurricane_dct):
  """Find the highest damage inducing hurricane and its total cost."""
  greatest_damage = 'Cuba I'
  greatest_damage_count = 0
  for cane in hurricane_dct:
    if hurricane_dct[cane]['Damage'] == "Damages not recorded":
      continue
    elif hurricane_dct[cane]['Damage'] > greatest_damage_count:
      greatest_damage = cane
      greatest_damage_count = hurricane_dct[cane]['Damage']
  return "Greatest damage: " + greatest_damage + ": " + str(greatest_damage_count)

greatest_damage = find_greatest_damage(hurricane_dct)
#print(greatest_damage)


# write your catgeorize by damage function here:
def categorize_by_damage(hurricane_dct:dict):
  damage_scale = {0: 0,
                 1: 100000000,
                 2: 1000000000,
                 3: 10000000000,
                 4: 50000000000}
  hurricanes_damage = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for cane in hurricane_dct:
    total_damage = hurricane_dct[cane]['Damage']
    if total_damage == "Damages not recorded":
      hurricanes_damage[0].append(hurricane_dct[cane])
    elif total_damage == damage_scale[0]:
      hurricanes_damage[0].append(hurricane_dct[cane])
    elif total_damage > damage_scale[0] and total_damage <= damage_scale[1]:
      hurricanes_damage[1].append(hurricane_dct[cane])
    elif total_damage > damage_scale[1] and total_damage <= damage_scale[2]:
      hurricanes_damage[2].append(hurricane_dct[cane])
    elif total_damage > damage_scale[2] and total_damage <= damage_scale[3]:
      hurricanes_damage[3].append(hurricane_dct[cane])
    elif total_damage > damage_scale[3] and total_damage <= damage_scale[4]:
      hurricanes_damage[4].append(hurricane_dct[cane])
    elif total_damage > damage_scale[4]:
      hurricanes_damage[5].append(hurricane_dct[cane])
  return hurricanes_damage

hurricanes_damage = categorize_by_damage(hurricane_dct)
#print(hurricanes_damage)