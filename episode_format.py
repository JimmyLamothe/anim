#takes an integer under 1000 and converts it to a three number string.
#INPUT: INTEGER
#OUTPUT: STRING
#EXCEPTION: Raises ValueError
def episode_format(episode):
    if episode < 10:
        return '00' + str(episode)
    if episode < 100:
        return '0' + str(episode)
    if episode < 1000:
        return str(episode)
    else:
        raise ValueError
