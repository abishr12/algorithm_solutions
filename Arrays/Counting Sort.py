
# coding: utf-8

# In[1]:


def counting_sort(the_list, max_value):

  # list of 0's at indices 0...max_value
  num_counts = [0] * (max_value+1)

  # populate num_counts
  for item in the_list:
      num_counts[item] += 1

  # populate the final sorted list
  sorted_list = []

  # for each item in num_counts
  for item, count in enumerate(num_counts):

      # for the number of times the item occurs
      for time in range(count):

          # add it to the sorted list
          sorted_list.append(item)

  return sorted_list


# In[2]:


unsorted_scores = [37, 89, 41, 65, 91, 53]


# In[4]:


unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

counting_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE)
# returns [91, 89, 65, 53, 41, 37]

