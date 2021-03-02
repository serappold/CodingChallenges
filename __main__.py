from itertools import permutations
import sys

__author__ = 'Scott Rappold'
__maintainer__ = 'Scott Rappold'
__email__ = 'rappold.scott@gmail.com'

def main():
    print(next_largest_without_permutations(sys.argv[1]))

def next_largest(l):
  listing = []
  sequence = [int(i) for i in str(l)]

  for iteration in permutations(sequence):
    
    #convert over to string
    s = [str(i) for i in iteration] 
    res = int("".join(s))

    if res >= l:
      if res not in listing:
        #append unique numbers only
        listing.append(int("".join(s)))

  #sort to find next largest number
  listing.sort()

  if listing.index(l) == len(listing)-1:
    return -1
  else:
    return listing[(listing.index(l)+1)]  

def next_largest_without_permutations(l):
  #convert number to string
  number_string = str(l)
  
  #loop through each number from length-2 to 0 step -1
  for i in range(len(number_string)-2, -1,-1):
    #grab current number
    current_number = number_string[i]
    #grab the number 1 position to the right of current_number
    right_of_current = number_string[i+1]
    
    if current_number < right_of_current:
      #list of all numbers to the right of current position and sort
      temp = sorted(number_string[i:])
      
      #grab the next largest number after the current number based on indexed position
      next = temp[temp.index(current_number)+1]
      
      #remove from list the 'next' value
      temp.remove(next)
      #join list back together
      temp = ''.join(temp)

      return int(number_string[:i]+next+temp)
  return -1

#print(next_largest(12))
#print(next_largest(21))
#print(next_largest(12345678))
#print(next_largest(34535762))
#print(next_largest(45590051))
#print(next_largest(987654321))

#print(next_largest_without_permutations(12))
#print(next_largest_without_permutations(21))
#print(next_largest_without_permutations(12345678))
#print(next_largest_without_permutations(34535762))
#print(next_largest_without_permutations(45590051))
#print(next_largest_without_permutations(987654321))


if __name__ == '__main__':
    main()