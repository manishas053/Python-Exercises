##################################################################################################
## Winnie-the-Pooh does not like physical activity. He wants to have a meal n times,              #
## traveling minimum possible distance. Help him to find this distance.                           #
## First line contains an integer n - number of visits.                                           #
## Second line contains an integer a - distance between Rabbit's and Owl's houses.                #
## Third line contains an integer b - distance between Rabbit's and Eeyore's houses.              #
## Fourth line contains an integer c - distance between Owl's and Eeyore's houses.                #
## Output one number - minimum distance in meters Winnie must go through to have a meal n times.  #
##################################################################################################

n = raw_input()
a = raw_input()
b = raw_input()
c = raw_input()
sum = 0
if n == 0:
    print "0"
else:
    m = min(a, min(b, c))
    sum = min(a, b) + (n-2)*m
    print sum
