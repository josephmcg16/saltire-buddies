"""
py code for scottish university data

info from: https://www.scotland.org/study/scottish-universities
"""

# list of scottish unis as strings
names = [
    'University of St Andrews',
    'University of Glasgow',
    'University of Aberdeen',
    'University of Edinburgh',
    'University of Strathclyde',
    'Heriot-Watt University',
    'University of Dundee',
    'University of Stirling',
    'Edinburgh Napier University',
    'Robert Gordon University',
    'Glasgow Caledonian University',
    'University of Abertay Dundee',
    'Queen Margaret University',
    'University of the West of Scotland',
    'University of the Highlands and Islands',
]


def de_capitalize(uni_names):
    uni_names = [name.lower() for name in uni_names]  # make everything lower case
    return uni_names


names = de_capitalize(names)
# print(names)


# calculate the distance between the unis and assign a compatibility score
def distance(uni1, uni2):
    # work out the distance between them (easy enough?)
    return
